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

def double(x): 

    return x * 2 

  

numbers = [1, 2, 3, 4, 5] 

doubled_numbers = map(double, numbers) 

  

print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10] 