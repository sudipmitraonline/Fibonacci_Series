"""
Fibonacci Number Calculating System
Developed by Sudip Mitra
30-10-2019
sudipmitraonline@gmail.com
Contact : 7003720931
"""
print("Fibonacci Number Calculating System \n Developed by Sudip Mitra\n")

def fibonacci(value) :
    #Fibonacci Number calculating function
    if value < 0 :
        print("Wrong Input ! Number can't be less than '0'.")
    elif value == 1 :
        return 0
    elif value == 2:
        return 1
    else :
        return fibonacci(value - 1) + fibonacci(value - 2)

print("Enter the 'n'th term to find fibonacci number :")
user_input = int(input()) #To read user input
print("The calculated fibonacci number is :", fibonacci(user_input))

input()