# ---------------------------------------
# Simple Calculator
# Performs basic arithmetic operations
# ---------------------------------------

# Get the first number from the user
num1 = float(input("Enter the first number: "))

# Get the second number from the user
num2 = float(input("Enter the second number: "))

# Display the available operations
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get the user's choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform the selected operation
if choice == "1":
    result = num1 + num2
    print("\nResult =", result)

elif choice == "2":
    result = num1 - num2
    print("\nResult =", result)

elif choice == "3":
    result = num1 * num2
    print("\nResult =", result)

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("\nResult =", result)
    else:
        print("\nError! Division by zero is not allowed.")

else:
    print("\nInvalid choice! Please select a valid operation.")