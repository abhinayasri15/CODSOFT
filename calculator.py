from time import sleep

# Function to run the calculator application
def calculator():
    print("\t\t\t CALCULATOR APPLICATION\t\t\t")
    while True:
        print("\n")
        print("OPERATIONS")
        print("1. ADDITION (+)")
        print("2. SUBTRACTION (-)")
        print("3. MULTIPLICATION (*) ")
        print("4. DIVISION (/)")
        print("5. MODULO DIVISION (%)")
        print("6. EXIT APPLICATION")
        print("\n")
        
        # Taking input from the user for choice
        user_choice = int(input("Enter your choice : "))
        
        if user_choice == 1:
            # Addition operation
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"{num1} + {num2} = ", num1 + num2)
            sleep(1)
        
        elif user_choice == 2:
            # Subtraction operation
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"{num1} - {num2} = ", num1 - num2)
            sleep(1)
        
        elif user_choice == 3:
            # Multiplication operation
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"{num1} * {num2} = ", num1 * num2)
            sleep(1)
        
        elif user_choice == 4:
            # Division operation
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if num2 == 0:
                print("Error! Division by zero cannot be done.")
                sleep(1)
            else:
                print(f"{num1} / {num2} = ", num1 / num2)
                sleep(1)
        
        elif user_choice == 5:
            # Modulo operation
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"{num1} % {num2} = ", num1 % num2)
            sleep(1)
        
        elif user_choice == 6:
            # Exit the application
            print("Exiting Calculator")
            break
        
        else:
            # Invalid choice
            print("Invalid choice! Please enter a valid operation.")
            sleep(1)

# Start the Calculator application
if __name__ == "__main__":
    calculator()
