# match_case_calculator.py

def main():
    # Prompt the user to enter two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Prompt for the operation
    operation = input("Choose the operation (+, -, *, /): ").strip()

    # Perform calculation using match-case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation. Please choose one of +, -, *, /.")

if __name__ == "__main__":
    main()
