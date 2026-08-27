
# for items in range(1, 10, 2):
#     print(f"round: {items}")

# scores = [80, 50, 90]
# total = 0
# for score in scores:
#     total += score
# print("current total:",total)

# files = [' report.csv ', 'data.csv ', 'final.txt ']
# for file in files:
#     file = file.strip().lower().replace('.txt ', '.csv ')
#     print(f"processing {file}")

# for i in range(2,9):
#         print("*" * i)

# # for i in range(1,11):
#         print(f"7 * {i} = {7*i}")

# for i in range(1, 13):
#     for j in range(1, 13):
#             print(f"{i} * {j} = {i * j}")

# names = ['jane', 'maria', '', 'kuma']
# for name in names:
#     if name == '':
#         name = name.replace('', 'unknown')
#          #handle empty value
#     print(f'Name = {name}')

# days = ['mon', 'tues', 'wed', 'sun', 'thurs']
# weekends = ['sat',  'sun']
# for day in days:
#     if day in weekends:
#         continue
#     print(f'workday: {day}')

# emails = [
#     'data@gmail.com',
#     'me@gmail.com',
#     'drop that what;',
#     'shut@gmail.com'
# ]
# for email in emails:
#     if ';' in email:
#         print('SQL attack')
#         break
# #     print(f"processing email: {email}")

# items = [1,3,5,7]
# for i in items:
#     if i % 2 == 0:
#         print('even number found', i)
#         break
# else:
#     print('all numbers are odd')

# names = ['Kamara', 'Tuba', 'AB', 'Nuella']
# for name in names:
#     if name is None:
#         print('found missing name')
#         break
# else:
#     print('all names are available')

# files = ['data.csv',
#          'report.pdf',
#          'data.txt',
#          'report.csv']

# for file in files:
#     if not file.endswith('.csv'):
#         print('not all files are csv')
#     continue
# else:
#     print('all files are csv')

# file_list = ['report.csv',
#              'data.xlsx',
#              'summary.docx',
#              'report.csv',
#              'data.csv']

# seen = []
# duplicate = False
# for file in file_list:
#     if file in seen:
#         duplicate = True
#         break
#     seen.append(file)
# if duplicate:
#     print('duplicate found')
# else:
#     print('all files are unique')
