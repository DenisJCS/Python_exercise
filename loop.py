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
