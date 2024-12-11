import login_register
import auth

def customer_panel(user):
    while True:
        print("\nCustomer Panel")
        print("1. Post a service")
        print("2. View my posted services")
        print("3. View service providers")
        print("4. Make a payment for a service")
        print("5. Logout")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            service_name = input("Enter service name: ")
            price = input("Enter service price: ")
            datetime = input("Enter service date and time: ")
            user.post_service(service_name, price, datetime)
        elif choice == "2":
            services = user.get_posted_services()
            if services:
                print("Your Posted Services:")
                for idx, service in enumerate(services, start=1):
                    print(f"{idx}. Name: {service['name']}, Price: {service['price']}, Date & Time: {service['datetime']}")
            else:
                print("You have not posted any services yet.")
        elif choice == "3":
            print("Service Providers:")
            for sp in auth.users["ServiceProvider"]:
                print(f"Name: {sp._name}, Business: {sp._businessName}, Rating: {sp.rating}")
        elif choice == "4":
            services = user.get_posted_services()
            if services:
                print("Your Posted Services:")
                for idx, service in enumerate(services, start=1):
                    print(f"{idx}. Name: {service['name']}, Price: {service['price']}, Date & Time: {service['datetime']}")
                index = int(input("Enter the index of the service you want to pay for: ")) - 1
                user.make_payment(index)
            else:
                print("You have no services to make payments for.")
        elif choice == "5":
            print("Logging out...")
            import login_register
            login_register.main()
            break
        elif choice == "6":
            print("Exiting application.")
            exit()
        else:
            print("Invalid choice. Please try again.")
