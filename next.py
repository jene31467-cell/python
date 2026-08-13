# my_list = [10, 11, 30, 10]
# print(my_list) #ordered #allow duplicate
# print(my_list[1]) #indexed
# my_list[3] = 40
# print(my_list) #mutable

# my_tuple = (10, 30, 20)
# print(my_tuple) #ordered #allows duplicates
# print(my_tuple[1]) #indexed
# # my_tuple[3] = 40 #im=umutable

# print(sorted(my_tuple))

# my_set = {10, 30, 20, 5, 0}
# print(my_set) #unordered 
# # .print(my_set[1]) #not indexed
# my_set.remove(20)
# print(my_set)

# a = {10, 30, 20, 5, 0}
# a.add(60)
# # print(a)
# # a.update('hi')
# a |= {1, 2}
# print(a)
# a.discard(30)
# # a.remove(100)
# print (a)

#mathematical operations

# a = {10, 30, 20, 50, 40}
# b = {30, 40, 50, 60}

# print(a.union(b))
# print(a | b)
# print(a.intersection(b))
# print(a ^ b)

# print(a.intersection(b))
# print(a.difference(b))
# print(a-b)
# print(b-a)
# print(a.symmetric_difference(b))

# a = {10, 30, 20, 50, 40}
# b = {30, 40, 50, 60}

a = {50, 60, 40}
b = {50, 60, 40}
# print(a.issubset(b))
# print(b.issubset(a))
print(a.isdisjoint(b))
print(b.isdisjoint(a))