import login_register
import auth

def service_provider_panel(user):
    while True:
        print("\nService Provider Panel")
        print("1. Add a gig")
        print("2. View my gigs")
        print("3. View customer requests")
        print("4. Deliver a customer service request")
        print("5. Logout")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            gig_name = input("Enter gig name: ")
            price = input("Enter gig price: ")
            availability = input("Enter availability: ")
            user.add_gig(gig_name, price, availability)
        elif choice == "2":
            gigs = user.get_gigs()
            if gigs:
                print("Your Gigs:")
                for idx, gig in enumerate(gigs, start=1):
                    print(f"{idx}. Name: {gig['name']}, Price: {gig['price']}, Availability: {gig['availability']}")
            else:
                print("You have not listed any gigs yet.")
        elif choice == "3":
            customer_services = []
            for customer in auth.users["Customer"]:
                customer_services.extend(customer.get_posted_services())
            if customer_services:
                print("Customer Requests:")
                user.view_customer_requests(customer_services)
            else:
                print("No customer requests available.")
        elif choice == "4":
            customer_services = []
            for customer in auth.users["Customer"]:
                customer_services.extend(customer.get_posted_services())
            if customer_services:
                print("Customer Requests:")
                for idx, service in enumerate(customer_services, start=1):
                    print(f"{idx}. Name: {service['name']}, Price: {service['price']}, Date & Time: {service['datetime']}")
                index = int(input("Enter the index of the service you want to deliver: ")) - 1
                if 0 <= index < len(customer_services):
                    service = customer_services[index]
                    print(f"Delivering service: {service['name']} for {service['price']} scheduled at {service['datetime']}")
                else:
                    print("Invalid service index.")
            else:
                print("No customer requests available.")
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
