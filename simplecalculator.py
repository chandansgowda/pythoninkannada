def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is undefined."

def main():
    print("Simple Calculator")
    print("Select an Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. End the Program")

    while True:
        try:
            operation = int(input("\nEnter choice (1/2/3/4/0): "))
            if operation == 0:
                print("Ending the program.")
                break
            
            if operation in (1, 2, 3, 4):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operation == 1:
                    print("Result:", add(num1, num2))
                elif operation == 2:
                    print("Result:", subtract(num1, num2))
                elif operation == 3:
                    print("Result:", multiply(num1, num2))
                elif operation == 4:
                    print("Result:", divide(num1, num2))
            else:
                print("Invalid option! Please choose a valid operation.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
