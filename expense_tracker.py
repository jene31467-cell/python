#!/usr/bin/env python3
"""A small, strict command-line expense tracker.

Expenses are stored locally in expenses.json next to this file.  The program
uses Decimal for all calculations so money is never added as binary floats.
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import date, datetime
from decimal import Decimal, InvalidOperation, ROUND_CEILING, ROUND_HALF_UP
from pathlib import Path
from typing import Any


DATA_FILE = Path(__file__).with_name("expenses.json")
MONEY_QUANTUM = Decimal("0.01")
MAX_TEXT_LENGTH = 80


@dataclass
class Expense:
    expense_id: int
    expense_date: str
    category: str
    description: str
    amount: str

    @property
    def money(self) -> Decimal:
        return Decimal(self.amount)

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Expense":
        required = {"expense_id", "expense_date", "category", "description", "amount"}
        if not required.issubset(raw):
            raise ValueError("an expense is missing one or more required fields")

        expense = cls(
            expense_id=int(raw["expense_id"]),
            expense_date=str(raw["expense_date"]),
            category=str(raw["category"]),
            description=str(raw["description"]),
            amount=str(raw["amount"]),
        )

        if not expense.money.is_finite() or expense.money <= 0:
            raise ValueError("an expense amount must be positive")
        datetime.strptime(expense.expense_date, "%Y-%m-%d")
        if not expense.category or not expense.description:
            raise ValueError("an expense has empty text")
        return expense


def money(value: Decimal) -> Decimal:
    """Round a Decimal to cents using normal financial rounding."""

    return value.quantize(MONEY_QUANTUM, rounding=ROUND_HALF_UP)


def format_money(value: Decimal) -> str:
    return f"${money(value):,.2f}"


def load_expenses() -> list[Expense]:
    if not DATA_FILE.exists():
        return []

    try:
        raw_data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        if not isinstance(raw_data, list):
            raise ValueError("the data file must contain a list")
        return [Expense.from_dict(item) for item in raw_data]
    except (OSError, json.JSONDecodeError, TypeError, ValueError, InvalidOperation) as error:
        raise RuntimeError(
            f"Could not read {DATA_FILE.name}. Fix or remove the file, then try again. "
            f"Details: {error}"
        ) from error


def save_expenses(expenses: list[Expense]) -> None:
    temporary_file = DATA_FILE.with_suffix(".tmp")
    payload = [asdict(expense) for expense in expenses]
    try:
        temporary_file.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        temporary_file.replace(DATA_FILE)
    except OSError as error:
        if temporary_file.exists():
            temporary_file.unlink()
        raise RuntimeError(f"Could not save expenses: {error}") from error


def prompt_non_empty(label: str, max_length: int = MAX_TEXT_LENGTH) -> str:
    while True:
        value = input(label).strip()
        if not value:
            print("This field cannot be empty. Please try again.")
        elif len(value) > max_length:
            print(f"Please keep this field to {max_length} characters or fewer.")
        else:
            return value


def prompt_decimal(
    label: str,
    *,
    minimum: Decimal = Decimal("0"),
    allow_zero: bool = True,
) -> Decimal:
    while True:
        raw_value = input(label).strip().replace(",", "")
        try:
            value = money(Decimal(raw_value))
        except (InvalidOperation, ValueError):
            print("Enter a valid number, for example 24.50.")
            continue

        if not value.is_finite():
            print("Enter a finite number.")
        elif value < minimum or (not allow_zero and value == 0):
            if allow_zero:
                print(f"Enter a number of at least {minimum}.")
            else:
                print(f"Enter a number greater than {minimum}.")
        else:
            return value


def prompt_date() -> str:
    while True:
        raw_date = input(f"Date (YYYY-MM-DD, Enter for {date.today()}): ").strip()
        if not raw_date:
            return date.today().isoformat()
        try:
            parsed = datetime.strptime(raw_date, "%Y-%m-%d").date()
            if parsed > date.today():
                print("Future dates are not allowed.")
            else:
                return parsed.isoformat()
        except ValueError:
            print("Use a real date in YYYY-MM-DD format.")


def prompt_yes_no(label: str) -> bool:
    while True:
        answer = input(label).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please answer yes or no.")


def display_expenses(expenses: list[Expense], heading: str = "Expenses") -> None:
    print(f"\n--- {heading} ---")
    if not expenses:
        print("No expenses found.")
        return

    print(f"{'ID':>4}  {'Date':<10}  {'Category':<18}  {'Description':<30}  {'Amount':>12}")
    print("-" * 82)
    for expense in sorted(expenses, key=lambda item: (item.expense_date, item.expense_id), reverse=True):
        print(
            f"{expense.expense_id:>4}  "
            f"{expense.expense_date:<10}  "
            f"{expense.category[:18]:<18}  "
            f"{expense.description[:30]:<30}  "
            f"{format_money(expense.money):>12}"
        )
    print(f"\nShowing {len(expenses)} expense(s).")


def add_expense(expenses: list[Expense]) -> None:
    print("\n--- Add Expense ---")
    amount = prompt_decimal("Amount: $", minimum=Decimal("0.01"), allow_zero=False)
    category = prompt_non_empty("Category: ")
    description = prompt_non_empty("Description: ")
    expense_date = prompt_date()
    next_id = max((expense.expense_id for expense in expenses), default=0) + 1
    expense = Expense(
        expense_id=next_id,
        expense_date=expense_date,
        category=category,
        description=description,
        amount=str(amount),
    )
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense #{expense.expense_id} saved: {format_money(amount)} for {description}.")


def search_expenses(expenses: list[Expense]) -> None:
    print("\n--- Search Expenses ---")
    query = prompt_non_empty("Search category, description, date, or amount: ").lower()
    matches = [
        expense
        for expense in expenses
        if query
        in " ".join(
            [
                expense.category,
                expense.description,
                expense.expense_date,
                expense.amount,
            ]
        ).lower()
    ]
    display_expenses(matches, f"Search results for '{query}'")
    if matches:
        print(f"Matching spending: {format_money(sum((item.money for item in matches), Decimal('0')))}")


def show_total_spending(expenses: list[Expense]) -> None:
    total = sum((expense.money for expense in expenses), Decimal("0"))
    print("\n--- Total Spending ---")
    print(f"Total: {format_money(total)}")
    print(f"Number of expenses: {len(expenses)}")


def show_category_spending(expenses: list[Expense]) -> None:
    totals: defaultdict[str, Decimal] = defaultdict(lambda: Decimal("0"))
    for expense in expenses:
        totals[expense.category] += expense.money

    print("\n--- Spending by Category ---")
    if not totals:
        print("No expenses found.")
        return

    overall = sum(totals.values(), Decimal("0"))
    print(f"{'Category':<24}  {'Amount':>12}  {'Share':>8}")
    print("-" * 50)
    for category, total in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        percentage = (total / overall * Decimal("100")).quantize(Decimal("0.1"))
        print(f"{category[:24]:<24}  {format_money(total):>12}  {percentage:>6.1f}%")
    print("-" * 50)
    print(f"{'Total':<24}  {format_money(overall):>12}")


def create_savings_plan(expenses: list[Expense]) -> None:
    print("\n--- Strict Savings Plan ---")
    print("This plan reserves savings first and sets a hard limit for all other spending.")
    if not prompt_yes_no("Would you like to create a savings plan? (yes/no): "):
        print("No savings plan created. You can create one the next time you exit.")
        return

    income = prompt_decimal("Monthly income: $", minimum=Decimal("0.01"), allow_zero=False)
    target = prompt_decimal("Savings goal: $", minimum=Decimal("0.01"), allow_zero=False)
    while True:
        raw_months = input("Deadline in months (whole number): ").strip()
        try:
            months = int(raw_months)
            if months < 1 or months > 120:
                raise ValueError
            break
        except ValueError:
            print("Enter a whole number from 1 to 120.")
    fixed = prompt_decimal("Essential monthly commitments: $", minimum=Decimal("0"))

    # Round savings upward so the final contribution cannot miss the goal by
    # a cent when the target is not evenly divisible by the deadline.
    monthly_savings = target / Decimal(months)
    monthly_savings = monthly_savings.quantize(MONEY_QUANTUM, rounding=ROUND_CEILING)
    strict_spending_limit = money(income - monthly_savings)
    flexible_limit = money(strict_spending_limit - fixed)

    print("\nPLAN RESULT")
    print(f"Required monthly savings:       {format_money(monthly_savings)}")
    print(f"Hard monthly spending limit:    {format_money(strict_spending_limit)}")
    print(f"Flexible spending after bills:  {format_money(flexible_limit)}")

    if flexible_limit < 0:
        shortfall = money(abs(flexible_limit))
        print(
            f"\nWARNING: This plan is not currently affordable. "
            f"Reduce commitments or increase income by at least {format_money(shortfall)} per month."
        )
    else:
        current_total = sum((expense.money for expense in expenses), Decimal("0"))
        remaining = money(flexible_limit - current_total)
        print("\nSTRICT MEASURES")
        print("1. Transfer the required savings amount on payday before discretionary spending.")
        print("2. Treat the spending limit as a hard ceiling; do not borrow to cover an overage.")
        print("3. Pause non-essential purchases immediately when 80% of the limit is reached.")
        print("4. If the limit is exceeded, cut the overage from next month's flexible spending.")
        print("5. Review spending every 7 days and adjust categories before the next purchase.")
        if current_total > flexible_limit:
            print(
                f"\nALERT: Current tracked spending is {format_money(current_total)}, "
                f"which exceeds the flexible limit by {format_money(current_total - flexible_limit)}."
            )
        else:
            print(f"\nRemaining flexible spending based on tracked expenses: {format_money(remaining)}")


def print_menu() -> None:
    print(
        "\n"
        "============================\n"
        "       EXPENSE TRACKER\n"
        "============================\n"
        "1. Add expense\n"
        "2. View expenses\n"
        "3. Search expenses\n"
        "4. Show total spending\n"
        "5. Show spending by category\n"
        "6. Exit\n"
    )


def run() -> None:
    try:
        expenses = load_expenses()
    except RuntimeError as error:
        print(f"\nERROR: {error}")
        return

    print(f"Loaded {len(expenses)} expense(s).")
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            search_expenses(expenses)
        elif choice == "4":
            show_total_spending(expenses)
        elif choice == "5":
            show_category_spending(expenses)
        elif choice == "6":
            create_savings_plan(expenses)
            print("\nGoodbye. Your expenses are stored locally.")
            break
        else:
            print("Invalid option. Choose a number from 1 to 6.")


if __name__ == "__main__":
    run()