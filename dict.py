#dictionary: left side is key and right side is the value
# person = {
#     "name": "Ene",
#     "age": 25,
#     "job": "Geologist"
# }
# person["age"] = 29 #replace a value in the dictionary!!
# print(person)
#go into person and give me the value belonging to the key
# print(person["age"])

# () → call a function

# [] → access an item in a dictionary

# {} → create a dictionary

# del person["job"]
# print(person)


# # student = {
#     "name": "Jenny",
#     "age": 16,
#     "course": "Biology",
#     "school": "RSU"
# }
# print(student["name"])
# print(student["course"])
# student["age"] = int(input("Enter new age: "))
# print(student["age"])

# student["grade"] = input("Enter grade: ")

# key = input("what information do you want to add? ")
# value = input("what is the value? ")
# student[key] = value
# student["favorite food"] = "plantain"
 
# print(student)
# print(student["name"])
# print(student["course"])
# student["age"] = int(input("Enter new age: "))
# print(student["age"])

# student["grade"] = input("Enter grade: ")

# key = input("what information do you want to add? ")
# value = input("what is the value? ")
# student[key] = value
# student["favorite food"] = "plantain"

# print(student)

# student = {
#     "name": "Jenny",
#     "age": 16,
#     "course": "Biology",
#     "school": "RSU"
# }

# while True: 
#     key = input("what would you add? ")
#     if key:
#         print("well done!! ")
#         break

# value = input("what do you say? ")

# if value:
#     student[key] = value
#     print("point valid!! ")
# else:
#     print("you must enter a value")

# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("phone"))
# print("="*9, "STUDENT INFORMATION", "="*9)
# for key, value in student.items():
#     print(f"{key.capitalize()} : {value}")
          
# print("="*15)

# students = {
#     "ST001": {
#         "name": "Jenny",
#         "age": 16,
#         "course": "Biology"
#     },

#     "ST002": {
#         "name": "David",
#         "age": 18,
#         "course": "Physics"
#     }
# }

# print(students["ST001"]["name"])
# print(students["ST002"]["course"])
# students["ST001"]["age"] = 17
# print(students["ST001"]["age"])
# students["ST002"]["course"] = "chemistry"
# print(students["ST002"]["course"])

# students["ST003"] = {
#     "name": "Sarah",
#     "age": 20,
#     "course": "mathematics"
# }
# print(students)
# student_id = input("Enter student ID: ")
# if student_id == students:
#     print("ID not found")
# else:
#     print("logged in")

students = {
    "ST001": {
        "name": "Jenny",
        "age": 17,
        "course": "Biology"
    },

    "ST002": {
        "name": "David",
        "age": 18,
        "course": "Chemistry"
    },

    "ST003": {
        "name": "Sarah",
        "age": 20,
        "course": "Mathematics"
    }
}

# student_id = input("Student ID: ")
# if student_id in students:

#     print("="*30)
#     # print("ID found")
# # else: 
# #     print("ID not found")
#     for key, value in students[student_id].items():
#         print(f"{key.title()}: {value}")
#         print("="*30)
# else:
#     print("student not found! ")


while True: 

    student_id = input("Student ID: ")

    if student_id == "exit":
        print("goodbye! ")
        break
    if student_id in students:
        print(students[student_id])
    else:
        print("student not found! ")