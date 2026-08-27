# my_dict = {
#     'a' : 10,
#     'b' : 20,
#     'c' : 20,
#     'a' : 40
# }
# print(my_dict) #ordered
# #keys are unique
# #values allow duplicates
# print(my_dict['b']) #not indexed
# my_dict['c'] = 80
# print(my_dict)

# user = {'id':1, 'age':30, 'city': "Berlin"}
#access a dictionary

# print(user['id'])
# print(user.get('name', 'unknow'))
# #checks
# print('age' in user)
# print('name' not in user)

# #view objects
# print(user.keys())
# print(user.values())
# print(user.items)

#looping

# for u in user:
#     print(u, user[u])

# for key, value in user.items():
#     print(key, value)

    #add, remove, update
# user['name'] = 'john' #add
# user['age'] = 35 #update
# user.update({'age': 40, 'city': "paris"})
# print(user)

# age = user.pop('age')
# print(user)
# print("removed age:",age)
#creation
# user = {'id': None,
#         'age': None,
#         'name': None,
#         'city': None
#         }
# user = dict.fromkeys(['id', 'name', 'age', 'city'], None)
# print(user)



#epresenting a single rows
# row = {
#     'id': 101,
#     'name': 'john',
#     'country': 'DE',
#     'age': 29,
#     'status': "active"
# }

# #mapping translations to friendly values
# status_map = {
#     "01": "open",
#     "02": "in progress",
#     "03": "done"
# } 

# #turninng short abbreviations into full readable names
# country_map = {
#     "DE": "Germany",
#     "FR": "France",
#     "IN": "India"
# }

# #storing environment variables andconfiguration 
# # store system setting like host, port, and usernames in one clean place
# system_conn = {
#     "DB_HOST": "prod-db.comapny.com",
#     "DB_PORT": 5432,
#     "DB_USER": "admin_user",
#     "DB_NAME": "analytics_warehouse"
# }

#challenge: keep only string values and convert them to uppercase
user = {'id': 2, "name": "Jane", "age": 30, "city": "Berlin"}

user_str = {
    key.upper(): value#expression
    for key, value in  user.items() #loop
    if isinstance(value, str)#filter
}


print(user_str)