from neighbour_hub_classes import User, ServiceProvider, Service, Booking, Payment, Review, Messaging

# User-friendly interface for NeighbourHub
def main_menu():
    """Displays the main menu options for the user."""
    print("\n=== NeighbourHub System ===")
    print("1. Register User")
    print("2. Login User")
    print("3. Register Service Provider")
    print("4. Add Service")
    print("5. Book Service")
    print("6. Process Payment")
    print("7. Submit Review")
    print("8. Send Message")
    print("9. View Users")
    print("10. View Services, Bookings, and Messages")
    print("11. Logout")  # Added logout option
    print("0. Exit")
    print("===========================\n")

def get_user_input(prompt, input_type=str):
    """Helper function to safely get user input and handle errors."""
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input! Please enter a {input_type.__name__}.")

# Authentication for users
def authenticate_user(users, user_type):
    """Authenticates a user based on email, password, and user type."""
    email = input(f"Enter {user_type.capitalize()} Email: ")
    password = input(f"Enter {user_type.capitalize()} Password: ")
    
    # Find the user with matching email, password, and user type
    user = next((u for u in users if u.email == email and u.password == password and u.userType == user_type), None)
    
    if user:
        print(f"Login successful! Welcome, {user.name}.")
        return user
    else:
        print(f"Invalid credentials or not a registered {user_type}. Please try again.")
        return None


# Main execution logic
def main():
    # Lists to store users, service providers, services, bookings, and messages
    users = []  # Customers and admins
    providers = []  # Service Providers
    services = []  # List of services
    bookings = []  # List of bookings
    messages = []  # List of messages
    logged_in_user = None  # The currently logged-in user

    while True:
        main_menu()  # Display the main menu to the user
        choice = get_user_input("Select an option: ", int)  # Get the user's menu choice

        if choice == 1:
            # Register User
            user_id = get_user_input("Enter User ID: ", int)
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            password = input("Create a Password: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")
            user_type = input("Enter User Type (customer/admin): ").lower()
            if user_type not in ["customer", "admin"]:
                print("Invalid user type! Please enter 'customer' or 'admin'.")
                continue
            user = User(user_id, name, email, phone, address, user_type, password)
            user.register()  # Register the user
            users.append(user)  # Add the user to the users list

        elif choice == 2:
            # Login User
            user_type = input("Enter User Type (customer/admin): ").lower()
            if user_type not in ["customer", "admin"]:
                print("Invalid user type! Please enter 'customer' or 'admin'.")
                continue
            logged_in_user = authenticate_user(users, user_type)  # Authenticate the user
            if not logged_in_user:
                continue  # If login fails, return to the menu


        elif choice == 3:
            # Register Service Provider
            provider_id = get_user_input("Enter Provider ID: ", int)
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            password = input("Create a Password: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")
            business_name = input("Enter Business Name: ")
            description = input("Enter Business Description: ")
            rating = get_user_input("Enter Rating (0.0 - 5.0): ", float)
            review_count = get_user_input("Enter Number of Reviews: ", int)
            provider = ServiceProvider(provider_id, name, email, phone, address, "provider", provider_id, business_name, description, rating, review_count, password)
            print(f"Service Provider {name} registered successfully!")
            providers.append(provider)

        elif choice == 4:
            # Add Service (only providers can add services)
            if not providers:
                print("No service providers registered yet!")
                continue

            provider_id = get_user_input("Enter Provider ID to Add Service: ", int)
            provider = authenticate_user(providers, "Service Provider")  # Authenticate the provider
            if not provider or provider.providerID != provider_id:
                print("Authentication failed or provider ID mismatch!")
                continue

            service_id = get_user_input("Enter Service ID: ", int)
            name = input("Enter Service Name: ")
            description = input("Enter Service Description: ")
            price = get_user_input("Enter Service Price: ", float)
            availability = get_user_input("Is the service available? (1 for Yes, 0 for No): ", int) == 1

            service = Service(service_id, name, description, price, availability, provider)
            print(f"Service {name} added successfully!")
            services.append(service)

        elif choice == 5:
            # Book Service (only users can book services)
            if not users or not services:
                print("No users or services available for booking!")
                continue

            user = authenticate_user(users, "User")  # Authenticate the user
            if not user:
                continue

            booking_id = get_user_input("Enter Booking ID: ", int)
            service_id = get_user_input("Enter Service ID: ", int)
            date = input("Enter Booking Date (YYYY-MM-DD): ")
            time = input("Enter Booking Time (HH:MM AM/PM): ")
            service = next((s for s in services if s.serviceID == service_id), None)

            if not service:
                print(f"No service found with ID {service_id}!")
                continue

            booking = Booking(booking_id, user, service_id, date, time)
            booking.confirm_booking()  # Confirm the booking
            bookings.append(booking)

        elif choice == 6:
            # Process Payment
            if not bookings:
                print("No bookings available for payment!")
                continue

            payment_id = get_user_input("Enter Payment ID: ", int)
            booking_id = get_user_input("Enter Booking ID: ", int)
            amount = get_user_input("Enter Payment Amount: ", float)
            method = input("Enter Payment Method: ")
            booking = next((b for b in bookings if b.bookingID == booking_id), None)

            if not booking:
                print(f"No booking found with ID {booking_id}!")
                continue

            payment = Payment(payment_id, booking, amount, method)
            payment.process_payment()  # Process the payment

        elif choice == 7:
            # Submit Review
            if not users or not services:
                print("No users or services available for reviews!")
                continue

            user = authenticate_user(users, "User")  # Authenticate the user
            if not user:
                continue

            review_id = get_user_input("Enter Review ID: ", int)
            service_id = get_user_input("Enter Service ID: ", int)
            rating = get_user_input("Enter Rating (0.0 - 5.0): ", float)
            comments = input("Enter Review Comments: ")
            service = next((s for s in services if s.serviceID == service_id), None)

            if not service:
                print(f"No service found with ID {service_id}!")
                continue

            review = Review(review_id, user, service, rating, comments)
            review.submit_review()  # Submit the review

        elif choice == 8:
            # Send Message
            message_id = get_user_input("Enter Message ID: ", int)
            sender_email = input("Enter Sender Email: ")
            receiver_email = input("Enter Receiver Email: ")
            content = input("Enter Message Content: ")
            timestamp = input("Enter Timestamp (YYYY-MM-DD HH:MM): ")

            sender = next((u for u in users if u.email == sender_email), None)
            receiver = next((p for p in providers if p.email == receiver_email), None)

            if not sender:
                print(f"No user found with email {sender_email}!")
                continue
            if not receiver:
                print(f"No provider found with email {receiver_email}!")
                continue

            message = Messaging(message_id, sender, receiver, content, timestamp)
            message.send_message()  # Send the message
            messages.append(message)  # Store the message

        elif choice == 9:
            # View Users (before login)
            print("\n=== Users ===")
            for user in users:
                print(f"User ID: {user.userID}, Name: {user.name}, Email: {user.email}, Type: {user.userType}")
        
        elif choice == 10:
            # View Services, Bookings, and Messages (only after login)
            if not logged_in_user:
                print("Please log in first to view data.")
                continue

            print("\n=== View Data ===")
            print("1. View All Services")
            print("2. View All Bookings")
            print("3. View All Messages")
            data_choice = get_user_input("Select an option: ", int)

            if data_choice == 1:
                print("\n=== Services ===")
                for service in services:
                    print(f"Service ID: {service.serviceID}, Name: {service.name}, Price: {service.price}, Available: {service.isAvailable}")

            elif data_choice == 2:
                print("\n=== Bookings ===")
                for booking in bookings:
                    print(f"Booking ID: {booking.bookingID}, User: {booking.user.name}, Service: {booking.service.name}, Date: {booking.date}, Time: {booking.time}")

            elif data_choice == 3:
                print("\n=== Messages ===")
                for message in messages:
                    print(f"Message ID: {message.messageID}, Sender: {message.sender.name}, Receiver: {message.receiver.businessName}, Content: {message.content}, Timestamp: {message.timestamp}")

        elif choice == 11:
            # Logout
            if logged_in_user:
                logged_in_user = None  # Clear the logged-in user
                print("You have successfully logged out.")
            else:
                print("You are not logged in!")

        elif choice == 0:
            # Exit the application
            print("Exiting NeighbourHub system...")
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()  # Run the main function to start the program
