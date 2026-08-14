# import math
# #built in function(just calling)
# print(len("python"))

# #function from lib
# number = 4.2
# print(math.ceil(number))

# #user defined function(define first then call the function)
# def greet():
#     print('hello')
# greet()

#parameters are names used in function definition that describe what data the function expects

#arguments are actual values passed in a funtion call that are assigned to paramters
# case_rule = "lower" #global variable
# def clean_file(name): #parameter
#     cleaned = name.strip()#local variable
#     if case_rule == "lower":
#         cleaned = cleaned.lower()
#     # print("Raw:", name)
#     print("cleaned:", cleaned)

# clean_file('munA')
# clean_file('JASmine')
#global variable is created outside the function and can be accessed anywhere
#local variable is created inside the function and can be accessed only inside the function
#a global variable controls behavior withut changing the function

# def clean_name(first_name, last_name, country):
#     first = first_name.strip().title()
#     last = last_name.strip().title()
#     full_name = first + " " + last
#     print(full_name, "from", country)

# # clean_name('MarIa', 'joHN', 'SA') #positional arguments
# clean_name(country= "SA", first_name= "MarIa", last_name= "joHN") #keyword argument
#positional arguments arevalues passed to a function based on their order
#keyword arguments arevalues passed to the function base on their names

#mixed arguments
# clean_name("maRIa", last_name= "joHN", country= "SA")

#default parameter is parameter that hasalready a value so if you dont pass anything in, python uses that value automatically 

#deafault
# def clean_name(first_name, last_name, country="n/a"):
#     first = first_name.strip().title()
#     last = last_name.strip().title()
#     full_name = first + " " + last
#     print(full_name, "from", country)
# clean_name('MarIa', 'joHN')

# *args and **kwargs allow functions to accept an unknown number of arguments

#calc the total of values
# *args is a type tuple used to pass similar values like numbers and strings
# def total(*args):
#     print(sum(args))
# total(1, 2)
# total(10, 5, 8, 9, 0, 5, 3 )
# total(1, 2, 3)

#create user profile
#**kwargs is a dictionanry and can take nultiple parameters
#works only with keyword arguments
# def create_user(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# create_user(first_name = "June",
#             last_name = "May",
#            age = 14,
#             country = "Morocco" )

# def clean_file(name): #parameter
#     # if not name: 
#     #     return None
#     # else: 
#         lo_cleaned = name.strip().title()#local variable
#         up_cleaned = name.strip().upper()
#         return lo_cleaned, up_cleaned

# clean_name = clean_file('juLIAN')
# print(clean_name)

#task: store application log messages in a file
#action functions
# def write_log(message):
#     with open(r"c:\main\python\app.log", "a") as file:
#         file.write(message + "\n")

# # write_log("app started")
# # write_log("user logged in")
# write_log("app stopped")

#transformation function
#task : clean email addresses amd splis the into structured data (username and domain)

# def clean_and_split_email(email):
#     cl_email = email.strip().lower()
#     #sara@gmail.com
#     username, domain = cl_email.split("@")
#     return {"username": username, 
#             "domain": domain}

# print(clean_and_split_email("SARA@gmaiL.COM"))

#VALIDATION FUNCTION: validates a condition and returns a boolean result (true or false)
#Task: check whether the password meets the minimum requirement of 8 characters

# def is_valid_password(password):
#     return len(password) >= 8

# print(is_valid_password("1234567893736hiw"))

# #check is an email address has a basic format

# def email_checker(email):
#     return "@" in email and "." in email

# print(email_checker("saraGMAIL.COM"))

#orchestrator function controls program flow by calling other functions in correct order.
  
#write functions that are easy to read and understand