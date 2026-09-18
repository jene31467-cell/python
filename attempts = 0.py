# attempts = 0
# password = 1111
# while attempts < 3:
#     answer = input('do you agree? (yes/no): ')
#     email = input("put your email: ")
#     password = input("enter a password ")
#     if answer == 'yes' and '@' in email:
#         print('glad we are on same page')
#         break
#          attempts += 1
# else:
#     print('3 strikes and you are out')

# username = "Jane"
# password = 12345
# attempts = 4
# while attempts > 0:
    # user_name = input("enter username: ")
    # if user_name == username:
    #     print("good job! ")

    #     if input ("password ") == password:
    #         attempts -= 1
    #         print("hahaha keep trying!")
    #     else:
    #         print("successfull!!")
    #         break
    # # else:
    #     attempts -=1
    #     if attempts > 0:
    #         print("cooked!!! ")
    #     else:
    #         print("kicked out!!! ")

# words = ['sky', 'apple', 'rythm', 'fly', 'orange']

# for word in words:
#     for letter in word:
#         if letter.lower() in 'aeiou':
#             print(f"'{word}' contains the vowel '{letter}'")
#             break
#         else:
#             print(f"'{word}' has no vowels")

# for num in range(40, 20, -10):
#     print(num)

numbers = list(range(2, 11, 2))
print(numbers)