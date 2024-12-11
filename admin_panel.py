import login_register
import auth

def admin_panel(admin):
    while True:
        print("\nAdmin Panel")
        print("1. Manage Customers")
        print("2. Manage Service Providers")
        print("3. View and Manage All Services")
        print("4. Logout")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            manage_users("Customer", admin)
        elif choice == "2":
            manage_users("ServiceProvider", admin)
        elif choice == "3":
            view_and_manage_services(admin)
        elif choice == "4":
            print("Logging out...")
            login_register.main()
            break
        elif choice == "5":
            print("Exiting application.")
            exit()
        else:
            print("Invalid choice. Please try again.")

def manage_users(user_type, admin):
    """Function to manage customers or service providers."""
    users = auth.users[user_type]
    if not users:
        print(f"No {user_type}s to manage.")
        return

    print(f"Managing {user_type}s:")
    for idx, user in enumerate(users, start=1):
        print(f"{idx}. Name: {user._name}, Email: {user.email}, Phone: {user.phone}")
    
    action = input("Choose an action: (delete/update/exit): ").lower()
    if action == "delete":
        index = int(input("Enter the index of the user to delete: ")) - 1
        if 0 <= index < len(users):
            user_to_delete = users.pop(index)
            print(f"Deleted {user_to_delete._name}.")
        else:
            print("Invalid index.")
    elif action == "update":
        index = int(input("Enter the index of the user to update: ")) - 1
        if 0 <= index < len(users):
            user = users[index]
            new_email = input(f"Enter new email for {user._name} (or press Enter to keep current): ")
            new_phone = input(f"Enter new phone for {user._name} (or press Enter to keep current): ")
            if new_email:
                user.email = new_email
            if new_phone:
                user.phone = new_phone
            print(f"Updated {user._name}'s information.")
        else:
            print("Invalid index.")
    elif action == "exit":
        print("Exiting user management.")
    else:
        print("Invalid action.")

def view_and_manage_services(admin):
    """Function to view and manage all services."""
    customers = auth.users["Customer"]
    services = []
    for customer in customers:
        for service in customer.get_posted_services():
            services.append((service, customer._name))
    
    if not services:
        print("No services available.")
        return

    print("All Posted Services:")
    for idx, (service, customer_name) in enumerate(services, start=1):
        print(f"{idx}. Service: {service['name']}, Price: {service['price']}, Date & Time: {service['datetime']}, Posted by: {customer_name}")
    
    action = input("Do you want to delete a service? (yes/no): ").lower()
    if action == "yes":
        index = int(input("Enter the index of the service to delete: ")) - 1
        if 0 <= index < len(services):
            service, customer_name = services.pop(index)
            for customer in customers:
                if customer._name == customer_name:
                    customer.get_posted_services().remove(service)
            print(f"Deleted service '{service['name']}' posted by {customer_name}.")
        else:
            print("Invalid index.")
    else:
        print("Returning to Admin Panel.")
