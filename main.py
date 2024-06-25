#This program makes calculations with answer 7
names = ["Peter", "John", "andrew", "Matthew"]
print("One of the twelfe diciples of Jesus was "+ names[0])
print("One of the twelfe diciples of Jesus was "+ names[1])
print("One of the twelfe diciples of Jesus was "+ names[2])
print("One of the twelfe diciples of Jesus was "+ names[3])
print("One of the twelfe diciples of Jesus was "+ names[-2].upper())

cars = ["Mercedes", "Audi", "BMW", "Porsche"]
print("If I had a chance by most comfortble car I would choose "+ cars[0])
print("I want to have in my garage all cars except "+ cars[2])
print("One of the universal suv I would love to have is "+ cars[-3]+ " rs6")
print("For being on status and sport I would buy 911s "+ cars[3])

cars[2] = "Lamborgini"
print(cars)
print("If I had a chance by most comfortble car I would choose "+ cars[0])
print("I want to have in my garage all cars except "+ cars[2])
print("One of the universal suv I would love to have is "+ cars[-3]+ " rs6")
print("For being on status and sport I would buy 911s "+ cars[3])
cars.append("Fiat")
print(cars)

motorcicles= []
motorcicles.append('honda')
motorcicles.append('triumph')
motorcicles.append('ducati')
print(motorcicles)
motorcicles.insert(4,"kawasaki")
print(motorcicles)

del motorcicles[-1]
print(motorcicles)

popped_motorcicles = motorcicles.pop(0)
print(motorcicles)
print(popped_motorcicles)

motorcicles = ["honda", "suziki", "ducati"]
last_owned = motorcicles.pop(1)
print("Last motorcicle I owned was "+ last_owned.title()+ ".")

motorcicles.insert(1, last_owned)
print(motorcicles)

too_expencive = "honda"
motorcicles.remove(too_expencive)
print(motorcicles)
print("\n A " + too_expencive.title() + " is too expencive for me " +" ." )




people_in_my_guests = ["August", "David", "Jesus", "Isaac Nueton"]
print(people_in_my_guests)
print("Dear friend , I would love to invite you in my house this week " +people_in_my_guests[0])
print("Dear friend , I would love to invite you in my house this week " +people_in_my_guests[1])
print("Dear friend , I would love to invite you in my house this week " +people_in_my_guests[2])     
print("Dear friend , I would love to invite you in my house this week " +people_in_my_guests[3]) 

popped_guest = people_in_my_guests.pop(0)
print(people_in_my_guests)
print(popped_guest)
people_in_my_guests.insert(0, "Julius Ceasar")
people_in_my_guests.insert(2, "Donald Trump")
people_in_my_guests.append("Victor Hugo")
print(people_in_my_guests)
print("Dear "+people_in_my_guests[0] , "I would love to invite you in my house this week ")
print("Dear "+people_in_my_guests[1] , "I would love to invite you in my house this week ")
print("Dear "+people_in_my_guests[2] , "I would love to invite you in my house this week ")     
print("Dear "+people_in_my_guests[3] , "I would love to invite you in my house this week ")
print("Dear "+people_in_my_guests[4] , "I would love to invite you in my house this week ")
print("Dear "+people_in_my_guests[5] , "I would love to invite you in my house this week ") 
print("Will not able to come : "+popped_guest)
#Do not have enough seats , so remove four people !!!
popped_guest_one  = people_in_my_guests.pop(0)
popped_guest_two = people_in_my_guests.pop(1)
popped_guest_three = people_in_my_guests.pop(2)
popped_guest_four = people_in_my_guests.pop(-1)
print(people_in_my_guests)
print("Dear "+ popped_guest_one +" I am sorry I do not have enough seat , maybe next time")
print("Dear "+ popped_guest_two +" I am sorry I do not have enough seat , maybe next time")
print("Dear "+ popped_guest_three +" I am sorry I do not have enough seat , maybe next time")
print("Dear "+ popped_guest_four +" I am sorry I do not have enough seat , maybe next time")
#Message to guest who will come
print("Dear " + people_in_my_guests[0]+ "invitation still in power , see ya at 8pm . ")
print("Dear " + people_in_my_guests[1]+ "invitation still in power , see ya at 8pm . ")
#Will not come due to absens of seats
print("Removed from the list: " + popped_guest_one + ", " + popped_guest_two +", "+ popped_guest_three +", "+ popped_guest_four  )



cars_models = ['bmw', 'audi', 'suzuki', 'piego', 'rheno']
print("Here is the original list:")
print(cars_models)
print("\nHere is the sorted list:")
print(sorted(cars_models))
print("\nHere is the original list again:")
print(cars_models)
print(cars_models)
cars_models.reverse()
print(cars_models)
len(cars_models)
print(len(cars_models))
