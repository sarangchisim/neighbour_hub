from neighbour_hub_classes import User, ServiceProvider, Admin

# Predefined admin user
users = {
    "Admin": [Admin("0", "Admin", "zero@gmail.com", "123zero", "Admin")],
    "Customer": [],
    "ServiceProvider": []
}

def authenticate_user(email, password, user_type):
    """Authenticate user based on email, password, and user type."""
    if user_type in users:
        for user in users[user_type]:
            if user.email == email and user.password == password:
                return user
    return None

def register_user(name, email, phone, password, user_type):
    """Register a new user."""
    if user_type not in users:
        print("Invalid user type.")
        return False

    # Ensure no duplicate emails
    for user in users[user_type]:
        if user.email == email:
            print("Email already registered. Please try logging in.")
            return False

    if user_type == "Customer":
        new_user = User(None, name, email, phone, None, "Customer")
    elif user_type == "ServiceProvider":
        new_user = ServiceProvider(None, None, name, None, 0, 0)
    else:
        print("Invalid user type.")
        return False

    new_user.password = password
    users[user_type].append(new_user)
    print(f"Successfully registered {name} as {user_type}!")
    return True