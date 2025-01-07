# defining function that perform arithmetic_operation

def perform_operation(num1: float, num2: float, operation: str):
    if operation == 'add':                # defining the parameters
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'Error: division by zero is not allowed'
        else:
            return num1 / num2
    else:
        return 'Error: invalid operation'

# provided main.py for Testing from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation(add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

