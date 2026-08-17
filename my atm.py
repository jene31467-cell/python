# print("="*12, "MY BANK ATM", "="*12)
# #create a dictionary conataining the accounts, the account numver is a key.
# # accounts = {
# #     "1001234567": { 
# #         "name": "Ene",
# #         "balance": 50000
# # #     }, 
# # #     "2056789012": {
# # #         "name": "Jane",
# # #         "balance": 2000
# # #     }
# # }

# sender_account = "1001234567"


# recipient_account = input("Enter recipient account number: ")

# if recipient_account in accounts:
#     amount = float(input("Enter amount: "))

#     sender_balance = accounts[sender_account]["balance"]
#     recipient_balance = accounts[recipient_account]["balance"]

#     print("sender balance: ", sender_balance)
#     print("Transfer amount: ", amount)
#     print("Recipient balance: ",  recipient_balance)

#     if amount <= sender_balance:

#         #remove money from sender
#         accounts[sender_account]["balance"] -= amount

#         #add money to recipient
#         accounts[recipient_account]["balance"] += amount

#         print("\nTransfer successful! ")
#         print("="*12, "RECEIPT", "="*12)
#         print("Transaction: Transfer")
#         print("From: ", sender_account)
#         print("To: ", recipient_account)
#         print("Amount: $", amount)
#         print("Balance: $", accounts[sender_account]["balance"])
#         print("Status: SUccess")
#         print("="*19)
#     else:
#         print("Insufficient balance")
# else:
#     print("Recipient account does not exist! ")

def write_receipt(message):
    with open(r"C:\main\python\receipts.txt", "a") as file:
        file.write(message + "\n")
        
sender_account = "1001234567"
sender_balance = 50000
while True:
    recipient_account = input("Enter recipient account number: ")

    if len(recipient_account) == 10 and recipient_account.isdigit():
        print("valid account! ")
        break
    else:
        print("Account number cannot be more than 10 digits")
amount = float(input(" Enter amount: "))
if amount <= sender_balance:
    sender_balance -= amount
    print("Transfer successful! ")
    print("From: ", sender_account)
    print("To: ", recipient_account)
    print("Amount: $", amount)
    print("Balance: $", sender_balance)
else:
    print("insufficient balance!")