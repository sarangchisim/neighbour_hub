import auth  
import customer_panel
import service_provider_panel
import admin_panel

def display_login():
    print("Welcome to Neighbour Hub! Please log in.")
    user_type = input("Enter user type (Customer/ServiceProvider/Admin): ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    return user_type, email, password

def display_register():
    print("New to Neighbour Hub? Register here.")
    user_type = input("Enter user type (Customer/ServiceProvider): ")
    name = input("Enter your full name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")
    return user_type, name, email, phone, password

def main():
    while True:
        print("\nNeighbour_Hub Login/Register Interface")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user_type, email, password = display_login()
            user = auth.authenticate_user(email, password, user_type)
            if user:
                print(f"Logged in as {user_type}.")
                if user_type == "Customer"|"customer":
                    customer_panel.customer_panel(user)
                elif user_type == "ServiceProvider"|"serviceprovider":
                    service_provider_panel.service_provider_panel(user)
                elif user_type == "Admin"|"admin":
                    admin_panel.admin_panel(user)
            else:
                print("Invalid email or password. Please try again.")
        elif choice == "2":
            user_type, name, email, phone, password = display_register()
            if user_type in ["Customer", "ServiceProvider"]:
                auth.register_user(name, email, phone, password, user_type)
            else:
                print("Invalid user type. Registration failed.")
        elif choice == "3":
            print("Exiting Neighbour Hub. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()