import os

def perform_calculation():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return
        
        equation = f"{num1} {operation} {num2} = {result}"
        print("Result:", equation)
        
        with open("equations.txt", "a") as file:
            file.write(equation + "\n")
        
    except ValueError:
        print("Invalid input. Please enter numerical values.")

def print_previous_calculations():
    if not os.path.exists("equations.txt"):
        print("No previous calculations found.")
        return
    
    with open("equations.txt", "r") as file:
        content = file.read()
        if content:
            print("Previous calculations:")
            print(content)
        else:
            print("No previous calculations found.")

def main():
    while True:
        print("\nSimple Calculator Application")
        print("1. Perform a calculation")
        print("2. Print previous calculations")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            perform_calculation()
        elif choice == '2':
            print_previous_calculations()
        elif choice == '3':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
