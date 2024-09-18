# Lambda function is used to creat small function
# It take only one line 
# Here example with usinf map() - this will apply expession to each argument
numbers = [1, 2, 3, 4, 5] 

squared = list(map(lambda x: x ** 2, numbers)) 

print(squared)  # Output: [1, 4, 9, 16, 25] 
