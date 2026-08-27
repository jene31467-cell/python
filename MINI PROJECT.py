#create an application that recieves an email from users, validate the email, if it is invalid log anerror in a file. if it is valid, clean and structure the email. log each step of the progam
# 
#  

# def write_log(message):
#     with open(r"C:\main\python\app.log", "a") as file:
#         file.write(message + "\n")

# def is_valid_email(email):
#     return "@" in email and "." in email

# def clean_and_split_email(email):
#     email = email.strip().lower()
#     username, domain = email.split("@")
#     return {
#         "username": username,
#         "domain": domain
#     }

# #orchestrator function
# def process_user_email(email):
#     write_log("App started")
#     email = input("Please enter your email: ")
#     is_valid_email(email)
#     if not is_valid_email(email):
#         write_log(f"invalid email recieved: {email}")
#     else:
#         clean_email = clean_and_split_email(email)
#         write_log(f"Processed email: {clean_email} ")
#     write_log("App stopped")

# email = input("Please enter your email: ")
# process_user_email(email)
balance = 700
correct_pin = 1235

# def write_log(message):
#     with open(r"C:\main\python\app.log", "a") as file:
#         file.write(message + "\n")

card = input("insert your card! ")
pin = int(input("enter your pin: "))
if pin == correct_pin:
    print("correct pin ")

    amount = float(input("enter withdrawal amount: "))

    if amount <= balance:
        balance -= amount
        print("transaction successful! ")
        print("take your cash! ")
        print("remaining balance:", balance)
    else:
        print("insufficient balance. ")
else:
    print("incorrect pin!")



    


