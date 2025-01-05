while True:
    user_input1 = input("Enter any number (or 'q' to stop):")
    
    if user_input1.lower() == 'q':
        break
    num1 = float(user_input1)

    user_input2 = input("Enter any number (or 'q' to stop):")
    if user_input2.lower() == 'q':
        break
    num2 = float(user_input2)
    if num2 == 0:
        print("Division by 0 not allowed")
    else:
        print(num1/num2) 






