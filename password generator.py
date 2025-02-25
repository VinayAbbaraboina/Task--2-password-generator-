import random
import string

def generate_password(length, complexity):
    # Define possible characters based on complexity level
    if complexity == 'low':
        characters = string.ascii_lowercase
    elif complexity == 'medium':
        characters = string.ascii_letters  # Includes lowercase and uppercase
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits  # Includes letters and digits
    elif complexity == 'very high':
        characters = string.ascii_letters + string.digits + string.punctuation  # All letters, digits, and punctuation
    elif complexity == 'strong':
        characters= string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation  
    else:
        raise ValueError("Invalid complexity level. Choose from 'low', 'medium', 'high', 'very high', 'strong'.")
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main function
def main():
    # Prompt the user for input
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity level ('low', 'medium', 'high', 'very high', 'strong'): ").lower()

    # Generate password
    password = generate_password(length, complexity)
    
    # Display the password
    print(f"Your generated password is: {password}")

# Run the program
if __name__ == "__main__":
    main()
