# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits =["pear", "pineapple", "kiwi", "orange"]

# TODO: Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count >= 1:
    print(count)
    count -=1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers

m =1 
for m in range(10):
    print(m**2)


#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors = ["navy", "burgundy", "pink", "red", " purple", "grey"]
# TODO: Use a for loop to select and print 3 random colors from the list
for random_color in range(3):
    
    random_color = random.choice(colors) 
    print(random_color) 
    

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
a= int(input("enter first number"))
b= int(input("enter second number"))
operation = input ("insert an operation of your choice, -, +, *, /")
while true:
   
   if operation == "+":
        print (a+b)
        result = a + b
   elif operation == "-":
        print (a-b)
        result = a - b
   elif operation == "*":
       print (a*b)
       result = a * b
   elif b != 0 and operation == "/":
        print (a / b)
   else:
    print("Error: Division by zero")

# TODO: Import the custom module and use its functions
import math_operations

print(math_operations.add(5,8))
print(math_operations.subtract(5,8))
print(math_operations.multiply(5,8))
print(math_operations.divide(5,0))





# TODO: Use a while loop to create a simple calculate
print(result)