# Base User Class
class User:
    def __init__(self, user_id, name, email, phone, address, user_type, password):
        # Initialize the user attributes
        self.userID = user_id  # Unique identifier for the user
        self.name = name  # Name of the user
        self.email = email  # Email address of the user
        self.phone = phone  # Phone number of the user
        self.address = address  # Address of the user
        self.userType = user_type  # Type of user (e.g., regular user or service provider)
        self.password = password  # User's password for login authentication
        self.is_logged_in = False  # Indicates whether the user is logged in (default: False)

    def register(self):
        """Method to simulate user registration."""
        # This simulates registering a user by printing a success message
        print(f"User {self.name} registered successfully with email: {self.email}")

    def login(self, password):
        """Login method to verify password and login user."""
        # Check if the provided password matches the stored password
        if self.password == password:
            self.is_logged_in = True  # Set the user as logged in
            print(f"User {self.name} logged in.")
        else:
            print("Invalid password.")  # If password doesn't match, show error

    def update_profile(self, name=None, email=None, phone=None, address=None):
        """Update the user's profile with new information."""
        # Only update attributes if new values are provided
        if name: self.name = name
        if email: self.email = email
        if phone: self.phone = phone  # Update phone number
        if address: self.address = address  # Update address
        print(f"User profile updated for {self.name}.")

    def logout(self):
        """Logout the user by setting 'is_logged_in' to False."""
        self.is_logged_in = False
        print(f"User {self.name} logged out.")


# Booking Class
class Booking:
    def __init__(self, booking_id, user, service_id, date, time, status="Pending"):
        # Initialize booking details
        self.__bookingID = booking_id  # Private booking ID
        self.__user = user  # Associated user (private)
        self.serviceID = service_id  # ID of the booked service
        self.date = date  # Date of the booking
        self.time = time  # Time of the booking
        self.status = status  # Booking status (default: Pending)

    def confirm_booking(self):
        """Confirm the booking and change status."""
        self.status = "Confirmed"  # Change status to "Confirmed"
        print(f"Booking {self.__bookingID} confirmed for {self.__user.name}.")

    def cancel_booking(self):
        """Cancel the booking and change status."""
        self.status = "Cancelled"  # Change status to "Cancelled"
        print(f"Booking {self.__bookingID} cancelled for {self.__user.name}.")


# Payment Class
class Payment:
    def __init__(self, payment_id, booking, amount, method, status="Pending"):
        # Initialize payment details
        self.__paymentID = payment_id  # Private payment ID
        self.__booking = booking  # Associated booking (private)
        self.amount = amount  # Payment amount
        self.method = method  # Payment method (e.g., credit card, PayPal)
        self.status = status  # Payment status (default: Pending)

    def process_payment(self):
        """Process the payment and change status."""
        self.status = "Paid"  # Change payment status to "Paid"
        print(f"Payment {self.__paymentID} of {self.amount} processed using {self.method}.")

    def refund(self):
        """Refund the payment and change status."""
        self.status = "Refunded"  # Change status to "Refunded"
        print(f"Payment {self.__paymentID} has been refunded.")


# ServiceProvider Class (Inherits from User)
class ServiceProvider(User):
    def __init__(self, user_id, name, email, phone, address, user_type, password, provider_id, business_name, description, rating, review_count):
        # Initialize a service provider by inheriting from User and adding additional attributes
        super().__init__(user_id, name, email, phone, address, user_type, password)  # Call the parent constructor
        self.__providerID = provider_id  # Private provider ID
        self.businessName = business_name  # Business name (public)
        self.description = description  # Business description (public)
        self.rating = rating  # Service rating (public)
        self.reviewCount = review_count  # Number of reviews (public)

    def list_service(self):
        """Method to simulate listing a service by the provider."""
        print(f"Service listed by {self.businessName}.")

    def manage_bookings(self):
        """Method to simulate managing bookings for the service provider."""
        print(f"{self.businessName} is managing bookings.")


# Service Class
class Service:
    def __init__(self, service_id, name, description, price, availability, provider):
        # Initialize service details
        self.__serviceID = service_id  # Private service ID
        self.name = name  # Service name (public)
        self.description = description  # Service description (public)
        self.price = price  # Service price (public)
        self.availability = availability  # Availability status (public)
        self.__provider = provider  # Associated service provider (private)

    def update_details(self, name=None, description=None, price=None, availability=None):
        """Method to update the service details."""
        if name: self.name = name  # Update service name if provided
        if description: self.description = description  # Update service description if provided
        if price: self.price = price  # Update price if provided
        if availability is not None: self.availability = availability  # Update availability if provided
        print(f"Service details updated for {self.name}.")


# Messaging Class
class Messaging:
    def __init__(self, message_id, sender, receiver, content, timestamp):
        # Initialize message details
        self.__messageID = message_id  # Private message ID
        self.__sender = sender  # Sender of the message (private)
        self.__receiver = receiver  # Receiver of the message (private)
        self.content = content  # Message content (public)
        self._timestamp = timestamp  # Message timestamp (protected)

    def send_message(self):
        """Send a message from sender to receiver."""
        print(f"Message from {self.__sender.name} to {self.__receiver.name}: {self.content}")

    def receive_message(self):
        """Receive a message by the receiver."""
        print(f"Message received by {self.__receiver.name}: {self.content}")


# Review Class
class Review:
    def __init__(self, review_id, user, service, rating, comments):
        # Initialize review details
        self.__reviewID = review_id  # Private review ID
        self.__user = user  # Associated user (private)
        self.__service = service  # Associated service (private)
        self.rating = rating  # Rating provided by the user (public)
        self.comments = comments  # Comments provided by the user (public)

    def submit_review(self):
        """Submit a review for a service."""
        print(f"Review submitted for {self.__service.name} by {self.__user.name}: Rating {self.rating}, Comments: {self.comments}")

    def edit_review(self, new_rating, new_comments):
        """Edit an existing review."""
        self.rating = new_rating  # Update the rating
        self.comments = new_comments  # Update the comments
        print(f"Review updated: Rating {self.rating}, Comments: {self.comments}")
