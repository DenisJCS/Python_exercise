#1 checking equal or not equal
#True
my_list = [4, 7, 10, 15, 20, 25, 30, 35, 40, 45]
condition1 = my_list[0] == 4
condition2 = my_list[2] < 15
condition3 = my_list[5] >=25
condition4 = my_list[-1] !=10
condition5 = my_list[6] <=32
#False
condition6 = my_list[0] == 5
condition7 = my_list[4] <=1
condition8 = my_list[2] - my_list[1] != 3
condition9 = my_list[5] <= my_list[4]
condition10 = my_list[-1]<= my_list[-2]

print(condition1)
print(condition2)
print(condition3)
print(condition4)
print(condition5)
print(condition6)
print(condition7)
print(condition8)
print(condition9)
print(condition10)

print("\nChecking with registers")
car = 'Mercedes'
print(car == 'Mercedes')
print(car == 'mercedes'.title())
print(car)

#3 Using AND/OR
print("\nnew exercise ")
my_list = [4, 7, 10, 15, 20, 25, 30, 35, 40, 45]
statment1 = my_list[0]==4 and my_list[1]<3
statment2 = my_list[-1] !=40 and my_list[2]==11
statment3 = my_list[4]>15 and my_list[2] == 11
statment4 = my_list[6] != 10 and my_list[-2] > 42
statment5 = my_list[8] != 10 or my_list[0]>10
statment6 = my_list[-3] <20 or my_list[-4] == 30
statment7 = my_list[0] == 4 or my_list[5] <=10
statment8 = my_list[3] >=15 or my_list[-8] != 15
print(statment1)
print(statment2)
print(statment3)
print(statment4)
print(statment5)
print(statment6)
print(statment7)
print(statment8)
