#Write your function here
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

#Uncomment the line below when your function is done
#print(max_num([50, -10, 0, 75, 20]))
print(max_num([50, -10, 0, 75, 20]))

#Write your function here
def same_values(lst1, lst2):
  """Returns list where values equal"""
  new_list = []
  for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_list.append(index)
  return new_list

#Uncomment the line below when your function is done
#print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


#Write your function here
def reversed_list(lst1, lst2):
  """Checks two list"""
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

#Uncomment the lines below when your function is done
#print(reversed_list([1, 2, 3], [3, 2, 1]))
#print(reversed_list([1, 5, 3], [3, 2, 1]))
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


# Write your tenth_power function here:
def tenth_power(num):
  return num ** 10

# Uncomment these function calls to test your tenth_power function:
#print(tenth_power(1))
# 1 to the 10th power is 1
#print(tenth_power(0))
# 0 to the 10th power is 0
#print(tenth_power(2))
# 2 to the 10th power is 1024
print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))


# Write your square_root function here:
def square_root(num):
  return num ** 0.5
# Uncomment these function calls to test your square_root function:
#print(square_root(16))
# should print 4
#print(square_root(100))
# should print 10
print(square_root(16))
print(square_root(100))



# Write your win_percentage function here:
def win_percentage(wins, losses):
  return wins / (wins + losses) *100

# Uncomment these function calls to test your win_percentage function:
#print(win_percentage(5, 5))
# should print 50
#print(win_percentage(10, 0))
# should print 100
print(win_percentage(5, 5))
print(win_percentage(10, 0))

#The same one but improved 
def win_percentage( wins, losses):
  total_games = wins + losses
  ration_wons = wins / total_games
  return ration_wons * 100
print(win_percentage(5, 5))
print(win_percentage(10, 0))

# Write your average function here:
def average(num1, num2):
  total = num1 + num2
  return total / 2
# Uncomment these function calls to test your average function:
#print(average(1, 100))
# The average of 1 and 100 is 50.5
#print(average(1, -1))
# The average of 1 and -1 is 0
print(average(1, 100))
print(average(1, -1))


# Write your remainder function here:
def remainder(num1, num2):
  first = num1 * 2
  second = num2 / 2
  return first % second
# Uncomment these function calls to test your remainder function:
#print(remainder(15, 14))
# should print 2
#print(remainder(9, 6))
# should print 0
print(remainder(15, 14))
print(remainder(9, 6))

#Short version 
def remainder (num1 , num2):
  return (2 * num1) % (num2 /2)


# Write your first_three_multiples function here
def first_three_multiples(num):
  print(num)
  print(num*2)
  print(num *3)
  return num *3

# Uncomment these function calls to test your first_three_multiples function:
#first_three_multiples(10)
# should print 10, 20, 30, and return 30
#first_three_multiples(0)
# should print 0, 0, 0, and return 0
first_three_multiples(10)
first_three_multiples(0)



# Write your dog_years function here:
def dog_years(name, age):
  return name + ", you are " +str(age*7) + " years old in dog year"
  

# Uncomment these function calls to test your dog_years function:
#print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
#print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"
print(dog_years("Lola", 16))
print(dog_years("Baby", 0))
