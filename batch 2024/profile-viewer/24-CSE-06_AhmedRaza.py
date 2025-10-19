# Simple Profile Viewer Program

# Step 1: Create some dummy users (stored in a dictionary)
users = {
    1: {"name": "Ahmed Khan", "age": 20, "email": "ahmed@example.com"},
    2: {"name": "Sara Ali", "age": 22, "email": "sara@example.com"},
    3: {"name": "Bilal Ahmed", "age": 19, "email": "bilal@example.com"},
    4: {"name": "Fatima Noor", "age": 21, "email": "fatima@example.com"},
    5: {"name": "Zain Malik", "age": 23, "email": "zain@example.com"}
}

# Step 2: Ask the user to enter a user ID
try:
    user_id = int(input("Enter user ID (1–5): "))

    # Step 3: Check if the ID exists
    if user_id in users:
        profile = users[user_id]
        print("\n--- User Profile ---")
        print(f"Name: {profile['name']}")
        print(f"Age: {profile['age']}")
        print(f"Email: {profile['email']}")
    else:
        print("No user found with that ID. Please try again.")

except ValueError:
    print("Invalid input! Please enter a number only.")
