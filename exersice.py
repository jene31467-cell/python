# for x in range(3):
#     for y in range(2):
#         for z in range(8):
#             print(f'({x}, {y}, {z})')

# colors = ['red', 'blue', 'green', 'pink']
# sizes = ['L',  'XL', 'S']
# for color in colors:
#     for size in sizes:
#         print(f'{color} - Size {size}')

# years = [2026, 2027]
# months = ['January', 'February']
# days = range(1, 31)

# for y in years:
#     for m in months:
#         for d in days:
#             print(f'report_{y}_{m}_{d}.csv')

# tables = ['customers', 'orders', 'products', 'prices']
# columns = ['id', 'create_date']
# for t in tables:
#     for c in columns:
#         print(f'Select count(*) From {t} Where {c} is null;')

# i = 1
# while i <= 4:
#     print(i)
#     i += 1
# count = 1
# while count <= 10:
#     print(count)
#     count += 3

# answer = ''
# while answer != 'yes':
#     answer = input('do you agree?')
# print('thank you')

# while True:
#     answer = input('do you agree?')
#     if answer == 'yes':
#         break
# print('Thank you')
# while True:
#     x = input('type')
#     if x == 'stop':
#         break

# while True:
#     print('im unstoppable')

attempts = 0
while attempts < 3:
    answer = input('do you agree? (yes/no): ')
    if answer == 'yes':
        print('glad we are on same page')
        break
    attempts += 1
else:
    print('3 strikes and you are out')
        
