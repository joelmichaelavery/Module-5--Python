#Joel Avery
#11/8/22
#writes a series of conditional tests

car = 'subaru' #car is initialized to subaru
print("Is car == 'subaru'? I predict TRUE.")
#checks if car is a subaru output should be TRUE
print(car == 'subaru')

print("\nIs car == 'audi'? I predict FALSE.")
#checks if car is an audi output should be FALSE. 
print(car == 'audi')

print() #new line for space

age = 12 #initialized to 12

#conditionals to check for admission price based on age
if age < 4:
    price = 0 #price is zero is age is under 4
elif age < 18:
    price = 25 #price is 25 if age is under 18
elif age < 65:
    price = 40 #price is 40 if age is under 65

#elif block instead of else block to prevent malicious or false data. 
elif age >= 65:
    price = 20 #price is 20 for anyone over 65

#outputs admission price. 
print(f"Your admission cost is ${price}.\n")

#new conditional with only if statements
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!\n")

#section 5-3 Alien Colors 
alien_color = 'red' #assigned a variable alien_color and set to red

#writing an if statement that outputs based on the color of the alien. 
if alien_color == 'green':
    print("The player just earned 5 points.")
else: 
    print("The player earned no points")

if alien_color == 'green':
    print("The player just earned 5 points.")

if alien_color != 'green':
    print("The player just earned 10 points.")

#turn the above alien code into an if elif code. 
if alien_color == 'green':
    print("The player just earned 5 points.")
elif alien_color == 'yellow':
    print("The player just earned 10 points.")
elif alien_color == 'red':
    print("The player just earend 15 points.\n")

#stages of life with if-elif-else chain

age = 99 #created variable age. 

#write if-elif-else chain to output based on age
if age < 2:
    person = 'baby'

elif (age >= 2) and (age < 4):
    person = 'toddler'

elif (age >= 4) and (age < 13):
    person = 'kid'

elif (age >= 13) and (age < 20):
    person = 'teenager'

elif (age >= 20) and (age < 65):
    person = 'adult'

else: 
    person = 'elder'

print(f"The person is a/an {person}.\n")

#5-7 Favorite Fruit

favorite_fruits = ['Strawberry', 'Apple', 'Blueberries', 'Grapes', 'Grapefruit',
'Orange', 'Pomegranete']

if 'Strawberry' in favorite_fruits:
    print('Wow you really like strawberries.\n')


#5-8 Hello Admin 

usernames = ['admin', 'javery', 'dducan0603', 'joelmichaelavery', 'nqualls']

if usernames:
    for name in usernames:
        if name == 'admin':
            print("Hello Admin, would you like to see a status report?\n")
        else:
            print(f"Hello, {name} thank you for logging in again.\n")
else:
    print("We need to find some users!")

#new program to simulate how websites handle usernames
current_users = ['joelmichaelavery', 'dducan0603', 'admin', 'nqualls', 'javery']

new_users = ['joelmichaelavery', 'dducan0603', 'rock', 'bObama', 'DTrump']

for user in new_users:
    if user in current_users:
        print(f"I am sorry but the user name {user}, is already taken.\n" 
        "Please enter another name.\n")
    else: 
        print(f"The username {user} is available\n")