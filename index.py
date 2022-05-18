
print("What mathematical problem do you want to solve?")

problem = input()

if problem == "Addition":
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print(str(number1) + " + " + str(number2) + " = " + str(number1 + number2))
    
elif problem == "Subtraction":
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print(str(number1) + " - " + str(number2) + " = " + str(number1 - number2))
    
elif problem == "Multiplication":
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print(str(number1) + " * " + str(number2) + " = " + str(number1 * number2))
    
elif problem == "Division":
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print(str(number1) + " / " + str(number2) + " = " + str(number1 / number2))
    
elif problem == "Modulus operand":
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print(str(number1) + " % " + str(number2) + " = " + str(number1 % number2))
    
else:
    print("Invalid Entry")
