# letters = ['a','b', 'c','d', 'e']
# numbers = [1, 2, 3,4, 5]
# comb = letters + numbers
# print(comb)
# comb = [letters, numbers]
# print(comb)
# numbers.extend(letters)
# letters.extend(numbers)
# print(letters)
# print(numbers)
# comb = list(zip(letters, numbers, 'height'))
# print(comb)

#iteration
# letters = ['a','b', 'c','d', 'e']
# new_list = []
# for l in letters:
#     new_list.append(l.upper())
#     print(new_list)


#enumerate
# letters = ['a','b', '
# numbers = [1, 2, 3, 4]
# print(list(zip(letters, numbers)))
# print(list(enumerate(letters, start = 1)))
# for value in enumerate(letters):
#     print(value)
# print(list(reversed(letters)))
# for l, n in zip(letters, numbers):
#     print(l,n)


#function map
# letters = ['a','b', 'c','d', 'e']
# print(list(map(str.upper, letters)))
# numbers = [1, 2, 3, 4]
# print(list(map(int, numbers)))

# names = ['maria ', 'john ']
# for n in map(str.strip, names):

#     print(n)','d', 'e']

#filter
# letters = ['a','b','', None, 'c', False]
# print(list(filter(bool, letters)))

# items = ['sql', '123', 'python', '42']
# # print(list(filter(str.isalpha,items)))

# for i in filter(str.isalpha, items):
#     print(i)

#lambda

# multiple = lambda x: x*2
# print(multiple(2))

# add =  lambda x, y: x + y
# print(add(1, 3))

# check = lambda i: i in 'python'
# print(check('w'))

# prices = ['$12.50', '$9.99', '$100.00']
#data transformation with .replace
#put it in lambda
#map the function to iterate to manipulate my data
# print(list(map(lambda p: float(p.replace('$', '')), prices)))

# prices = [120, 30, 300, 80]
# print(list(filter(lambda p: p >= 100, prices)))

# students = [['ane', 70],
#             ['rayna', 90],
#             ['anna', 74]
# ]
# # print(list(filter(lambda row: row[1] > 70, students)))
# # print(students[2][1] > 70)
# print(list(filter(lambda row: row[0].startswith('a'), students)))
# print(students[2][0].startswith('a'))

#list comprehension
domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.DATA.COM']
cleaned = [
    d.lower().replace('www.', '')
    for d in domains
    if '.' in d   
]
print(cleaned)