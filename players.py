#Code below
#Exercise 4-10
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are: ")
print(my_foods)
print("\nMy friends favorite foods are:")
print(friend_foods)


my_dish = ['pizza', 'falafel', 'carrot cake']
#This doesn't work:
friend_dish = my_dish
my_dish.append('cannoli')
friend_dish.append('ice cream')
print("My favorite dishes are:")
print(my_dish)
print("\nMy friend's favorite dishes are:")
print(friend_dish)

print("The first three items in the list are :")
print(my_foods[0:3])
print("Three items from the middle of list are :")
print(my_foods[1:4])
print("The last three items in the list are :")
print(my_foods[-3:])

#Exercise 4-11
my_pizza = ['chicken', 'peperony', 'bacon ranch']
friends_pizza = my_pizza[:]
my_pizza.append('margarita')
friends_pizza.append('mushroom')
print(my_pizza)
print(friends_pizza)


print("My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friends_pizza:
    print(pizza)

print("My favorite foods are:")
for food in my_foods:
    print(food)
print("My friend's favorite foods are:")
for food in friend_foods:
    print(food)

#Tuples , кортежи
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)    
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


#Exercise 4-12
print("\nExcercise 4-13")
list_of_foods = ('fish', 'meat', 'vegies', 'cakes', 'soups')
for food in list_of_foods:
    print(food)


list_of_foods = ('fish', 'meat', 'vegies', 'cakes', 'soups')
print("Original menu:")
for foods in list_of_foods:
    print(foods)
list_of_foods = ('butter', 'meat', 'cream', 'cakes', 'beans')    
print("\nNew menu:")
for foods in list_of_foods:
    print(foods)

print('Well done Denis!')


