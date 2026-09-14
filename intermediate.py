attempts = 0
while attempts < 4:
    user_name = input('what is your name? ')
    if user_name == ' ':
        print('username cannot be empty')
        break
    attempts += 1
else:
    print('your attempts are out!')
