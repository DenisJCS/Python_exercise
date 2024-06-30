#code below
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    print(f"Adding {topping}.")
print("\nFinished making your pizza!")
#Using if statment in for in function
print("\n Using IF in functions")
for topping in requested_toppings:
    if topping == 'mushrooms':
        print("Sorry we run out of this")
    else:
        print(f"Adding {topping}.")
print("Finished making your pizza!")

#Using IN
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
     print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Two list 
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry we don't have {requested_topping}")
print("\nFinished making your pizza!")

#Exercise 5-8 page 103
names = ['Jake', 'admin', 'Alex', 'Dave', 'Paul', 'Charlie']
for name in names:
    if name == 'admin':
        print(f"Hello {name} would you like to see status reports?")
    else:
        print(f"Hello {name} thank you for logging in again! ")
#Exercise 5-8 Checking if list is empty
names = []
if names:
    for name in names:
        print(f"Hello user {name}")
else:
    print("We need to ind some users!")

# 5-10 Ckecking that user names are uniq
current_users = ['Madiso', 'Mendal', 'Charlie' ,'Bravo', 'Alfa']
new_users = ['Bravo', 'Elison', 'Charlie', 'Bane', 'Scot']
for user in new_users:
    if user in current_users:
        print(f"Name {user}is not available please choose other name")
    else:
     print(f"Name available , welcome {user}")
