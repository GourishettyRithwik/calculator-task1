# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("Simple CLI Calculator")
    print("Select operation: +, -, *, /")

    while True:
        op = input("Operation (+, -, *, / or 'q' to quit): ")
        if op == 'q':
            print("Goodbye!")
            break
        if op not in ['+', '-', '*', '/']:
            print("Invalid operation. Try again.")
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)

        print("Result:", result)

if __name__ == "__main__":
    calculator()