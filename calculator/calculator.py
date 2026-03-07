num1 = int(input("Insert first number: "))  
num2 = int(input("Insert second number: "))  
operation = input("What operation do you want to do? (+, -, *, /): ")

def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '/':
            return num1 / num2
        case '*':
            return num1 * num2

if num2 == 0 and operation == "/":
    print(f"You cannot divide by 0")
else:
    print(f"This is your result: {calculate(num1, num2, operation)}")
