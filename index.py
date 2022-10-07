print("WHAT MATHEMATICAL PROBLEM DO YOU WANT TO SOLVE?")

print(f"""
***Quick Help***

> Type Addition - To 'add' two numbers
> Type Subtraction - To 'minus' a number from the other
> Type Multiplication - To 'multiply' two numbers
> Type Division - To 'divide' two numbers
> Type Modulus - To check for the 'remainder'. The first number must be higher.
""")
problem = input().capitalize()

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if problem == "Addition":
    print(str(number1) + " + " + str(number2) + " = " + str(number1 + number2))

elif problem == "Subtraction":
    print(str(number1) + " - " + str(number2) + " = " + str(number1 - number2))

elif problem == "Multiplication":
    print(str(number1) + " * " + str(number2) + " = " + str(number1 * number2))

elif problem == "Division":
    print(str(number1) + " / " + str(number2) + " = " + str(number1 / number2))

elif problem == "Modulus":
    print(str(number1) + " % " + str(number2) + " = " + str(number1 % number2))

else:
    print("Invalid Entry")
