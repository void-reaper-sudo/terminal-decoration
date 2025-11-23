import random
import string
import time
input("Enter target IP: ")
def generate_password(length=8):
    """Generate a random 8-digit password consisting of digits."""
    return ''.join(random.choices(string.digits, k=length))

def main():
    user_count = 1  # Starting user number
    while True:
        password = generate_password()
        print(f"Username: User {user_count}:Password: {password}")
        user_count += 1
        time.sleep(1)  # Pause for 1 second before printing the next user

if __name__ == "__main__":
    main()
