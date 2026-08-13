# person = ['Maria', 27, 'Data engineer', 'spain']

# name, *_, role, country = person

# print(country)
# print(name)

# person = ['Maria', 27, 'Data engineer', 'spain']
# *details, country = person
# print(country)

# numbers = [1,5, 9, 5, 2,3,4]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(len(numbers))

# print(all(numbers))
# print("All:", all([1, 0, 8]))
# print(any(numbers))

# print(any([0, 0]))
# print("count:", numbers.count(5))
# print("index:", numbers.index(4))

# print(3 not in numbers)
 

# letters = ['a','b', 'c', 'd']
# letters.insert(0, 'x')
# removed = letters.pop()
# # letters.pop()
# print(removed)

# letters[0] = 'y'
# letters[2] = 'h'
# print(letters)
#print(new_list) print(type(letters)) 

# original = ['a', 'b', 'c']
# original_copy = original.copy()
# original.pop()
# original_copy.append('z')
# print('original:', original)
# print('copy:', original_copy)
# import copy
# matrix = [
#     ['a', 'b'],
#     ['c', 'd'],
# ]
# matrix_copy = copy.copy(matrix)
# # matrix.pop()
# matrix_copy[0].append('z')
# matrix_copy[1].append('q')
# # print(matrix)
# print('original:', matrix)
# print('copy:', matrix_copy)


# import copy
# original = [
#     ['a', 'b'],
#     ['c', 'd'],
# ]
# copy1 = original 
# print('same object:', original is copy1, '\n')

# copy2 = original.copy()
# print('shared lists?', original[0] is copy2[0], '\n')

# copy3 = copy.deepcopy(original)
# print('shared lists?', original[0] is copy2[0], '\n')

letters  = ['a','b', 'c']
numbers = [1, 2, 3, 4, 'hi']
# comb = letters + numbers
# comb = [letters, numbers]
# print(comb)
# print(comb* 2)
# numbers.extend(letters)
# print(letters)
# print(numbers)
comb = list(zip(letters, numbers, 'hi'))
print(comb)