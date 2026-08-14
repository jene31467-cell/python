#create an application that recieves an email from users, validate the email, if it is invalid log anerror in a file. if it is valid, clean and structure the email. log each step of the progam
# 
#  

def write_log(message):
    with open(r"C:\main\python\app.log", "a") as file:
        file.write(message + "\n")

def is_valid_email(email):
    return "@" in email and "." in email

def clean_and_split_email(email):
    email = email.strip().lower()
    username, domain = email.split("@")
    return {
        "username": username,
        "domain": domain
    }

#orchestrator function
def process_user_email(email):
    write_log("App started")
    email = input("Please enter your email: ")
    is_valid_email(email)
    if not is_valid_email(email):
        write_log(f"invalid email recieved: {email}")
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed email: {clean_email} ")
    write_log("App stopped")

email = input("Please enter your email: ")
process_user_email(email)