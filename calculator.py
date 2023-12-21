import math
from operator import add, subtract, divide, multiply, square_root
def calc():
    result =0
    while True:
        print("Last result " + str(result))
        #first number
        if result == 0:
            num1 = float(input("Enter first number: "))
        if result != 0:
            num1 = result
           #operator
        operator = input("Operator:  ").lower() #converts every input to lowercase
        if operator == 'c': #resets the calculator
            print('Calculator cleared')
            calc()
        elif operator == "sqrt":
            print(math.sqrt(num1))
            calc()
        elif operator.isdigit(): #disallows error messages to pop-out
            print("ValueError")
            print("Operator can't be a digit")
            calc()

        #number2
        num2 = float(input("Enter Second number: "))
        if operator == '+':
            result = (add(num1,num2))
        elif operator == '-':
            result = (subtract(num1, num2))
        elif operator == '//':
            result = (divide(num1, num2))
        elif operator == '*':
            result = (multiply(num1, num2))



#calc()
