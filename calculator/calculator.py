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

print(f"This is your result: {calculate(num1, num2, operation)}")
