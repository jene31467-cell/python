class User:
    def __init__(self, is_active, commission_rate):
        self.is_active = is_active
        self.commission_rate - commission_rate
def calculate_payout(user, amount):
    if user is not None:
        if user.is_active:
            if amount > 0:
                # Main "Happy Path" logic buried 3 tabs deep
                payout = amount * user.commission_rate
                return payout
            else:
                return "Invalid amount"
        else:
            return "Account inactive"
    else:
        return "No user found"

test_user = User(is_active=True, comission_rate=0.15)
print(calculate_payout(test_user, 100))

for twist_number in range(3):
        print("grinding twist number " + str(twist_number + 1))

for age_over in range(6):
        print((age_over +1 ))

for count in range(9):
        print("grind " + str(count +2))

weight = 2.0
while weight < 1.5:
        weight = weight + 0.5
        print("current weight:" + str(weight))

for num in range(1, 6):
    if num == 9:
        break  # Loop ends immediately when num reaches 3
    print(num)

print("Loop finished")

target = 'active'
user_statuses = ['pending', 'inactive', 'active', 'suspended']
for status in user_statuses:
    if status == target: 
        print("target found!")
        
age_str = input("How old are you? ")
if age_str.isdigit():
    age = int(age_str)
    print(f"You are {age} years old.")
else:
    print("That's not a valid age!")

# s = set("banana")
# print(len(s))

# x = [1, 2]
# print(x, append(3))