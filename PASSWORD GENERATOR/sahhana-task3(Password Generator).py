# --------------------------------------------
# PASSWORD GENERATOR
# Internship Project
# --------------------------------------------

# Import required modules
import random
import string

# Function to generate password
def generate_password():

    print("\n========== PASSWORD GENERATOR ==========\n")

    # Get password length from the user
    try:
        length = int(input("Enter the password length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    # Characters to be used in the password
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    # Generate the password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    # Display the generated password
    print("\nGenerated Password:")
    print(password)


# Main Program
while True:

    generate_password()

    # Ask if the user wants another password
    choice = input("\nDo you want to generate another password? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using the Password Generator!")
        break