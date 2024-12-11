class User:
    def __init__(self, user_id, name, email, phone, address, user_type):
        self.__userID = user_id  # Private variable
        self._name = name  # Protected variable
        self.email = email  # Public variable
        self.phone = phone  # Public variable
        self.address = address  # Public variable
        self._userType = user_type  # Protected variable

    def register(self):
        pass

    def login(self):
        pass

    def update_profile(self):
        pass

    def logout(self):
        pass
    
class Customer(User):
    def __init__(self, user_id, name, email, phone, address):
        super().__init__(user_id, name, email, phone, address, "Customer")
        self._posted_services = []  # List to store services posted by the customer

    def post_service(self, service_name, price, datetime):
        """Post a new service."""
        service = {"name": service_name, "price": price, "datetime": datetime}
        self._posted_services.append(service)
        print(f"Service '{service_name}' posted successfully!")

    def get_posted_services(self):
        """Get the list of posted services."""
        return self._posted_services

    def make_payment(self, service_index):
        """Process payment for a specific service."""
        if 0 <= service_index < len(self._posted_services):
            service = self._posted_services[service_index]
            print(f"Processing payment for service: {service['name']}, Amount: {service['price']}")
            # Payment logic can be added here
            print("Payment successful!")
        else:
            print("Invalid service index.")

    
class Booking(User):
    def __init__(self, user_id, booking_id, service_id, date, time, status):
        super().__init__(user_id, None, None, None, None, None)
        self.bookingID = booking_id  # Public variable
        self._serviceID = service_id  # Protected variable
        self.date = date  # Public variable
        self.time = time  # Public variable
        self._status = status  # Protected variable

    def confirm_booking(self):
        pass

    def cancel_booking(self):
        pass


class Payment(Booking):
    def __init__(self, user_id, booking_id, payment_id, amount, method, status):
        super().__init__(user_id, booking_id, None, None, None, None)
        self.paymentID = payment_id  # Public variable
        self._amount = amount  # Protected variable
        self.method = method  # Public variable
        self._status = status  # Protected variable

    def process_payment(self):
        pass

    def refund(self):
        pass
    
class ServiceProvider(User):
    def __init__(self, user_id, provider_id, business_name, description, rating, review_count):
        super().__init__(user_id, None, None, None, None, "ServiceProvider")
        self.providerID = provider_id  # Public variable
        self._businessName = business_name  # Protected variable
        self.description = description  # Public variable
        self.rating = rating  # Public variable
        self._reviewCount = review_count  # Protected variable
        self._gigs = []  # List to store gigs

    def add_gig(self, gig_name, price, availability):
        """Add a new gig."""
        gig = {"name": gig_name, "price": price, "availability": availability}
        self._gigs.append(gig)
        print(f"Gig '{gig_name}' added successfully!")

    def get_gigs(self):
        """Get the list of gigs."""
        return self._gigs

    def view_customer_requests(self, customer_services):
        """View all customer requests (posted services)."""
        for idx, service in enumerate(customer_services, start=1):
            print(f"{idx}. Name: {service['name']}, Price: {service['price']}, Date & Time: {service['datetime']}")


class Service(ServiceProvider):
    def __init__(self, provider_id, service_id, name, description, price, availability):
        super().__init__(None, provider_id, None, None, None, None)
        self.serviceID = service_id  # Public variable
        self._name = name  # Protected variable
        self.description = description  # Public variable
        self.price = price  # Public variable
        self._availability = availability  # Protected variable

    def update_details(self):
        pass
    
class Admin(User):
    def __init__(self, user_id, name, email, password, user_type="Admin"):
        super().__init__(user_id, name, email, None, None, user_type)
        self.password = password  # Admin-specific attribute

    def manage_users(self, user_list, action, user_id=None, new_data=None):
        """Manage users by deleting or altering user data."""
        if action == "delete":
            user_list[:] = [user for user in user_list if user._userID != user_id]
            print(f"User with ID {user_id} has been deleted.")
        elif action == "update" and user_id and new_data:
            for user in user_list:
                if user._userID == user_id:
                    user.email = new_data.get("email", user.email)
                    user.phone = new_data.get("phone", user.phone)
                    print(f"User with ID {user_id} has been updated.")
                    break
        else:
            print("Invalid action or missing parameters.")

    def view_all_services(self, customers):
        """View all posted services."""
        for customer in customers:
            if isinstance(customer, Customer):
                for service in customer.get_posted_services():
                    print(f"Service: {service['name']}, Posted by: {customer._name}")

    
    
class Review(Service):
    def __init__(self, user_id, service_id, review_id, rating, comments):
        super().__init__(None, service_id, None, None, None, None)
        self.reviewID = review_id  # Public variable
        self._rating = rating  # Protected variable
        self.comments = comments  # Public variable

    def submit_review(self):
        pass

    def edit_review(self):
        pass
