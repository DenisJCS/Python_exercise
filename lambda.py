# Lambda function is used to creat small function
# It take only one line 
# Here example with usinf map() - this will apply expession to each argument
numbers = [1, 2, 3, 4, 5] 

squared = list(map(lambda x: x ** 2, numbers)) 

print(squared)  # Output: [1, 4, 9, 16, 25] 

#The filter() function creates a new list of elements for which the given lambda function returns True:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 

print(even_numbers)  # Output: [2, 4, 6, 8, 10] 


#Lambda function 
MAP function 

def double(x): 

    return x * 2 

  

numbers = [1, 2, 3, 4, 5] 

doubled_numbers = map(double, numbers) 

  

print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10] 

# Sample list of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Using map with a lambda function to get the length of each name
name_lengths = list(map(lambda x: len(x), names))

# Using map with a defined function to capitalize each name
def capitalize_name(name):
    return name.upper()

capitalized_names = list(map(capitalize_name, names))

# Print the results
print("Original names:", names)
print("Name lengths:", name_lengths)
print("Capitalized names:", capitalized_names)

# Try creating your own map function!
# Uncomment and modify the line below:
# your_result = list(map(lambda x: # Your function here, names))
# print("Your result:", your_result)

