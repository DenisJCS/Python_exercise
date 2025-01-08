# Progaram will give answer based on entered age.

while True:
    age = input("Enter you age (or enter 'q' to quit) :")
    
    if age == 'q':
        break
    age = int(age)
    if age == 0 and age <= 5:
        print(f"Your age {age} you go to kindergarder")
    elif age>=6 and age <=13:
        print(f"You are {age} and you go to first class or 5 grade")
    elif age>13 and age <18:
        print(f"You are{age} and need to prepare to exam")
    else:
        print(f"You are adult , good buy ! :)")


# How to created alphabet and sort it 
a = 'qwertyuiopasdfghjklzxcvbnm'

print(*sorted(a))
