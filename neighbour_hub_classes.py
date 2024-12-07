# Base User Class
class User:
    def __init__(self, user_id, name, email, phone, address, user_type, password):
        self.user_id = user_id  # Unique identifier for the user
        self.name = name  # Name of the user
        self.email = email  # Email address of the user
        self.phone = phone  # Phone number of the user
        self.address = address  # Address of the user
        self.user_type = user_type  # Type of user (e.g., regular user, service provider)
        self.password = password  # Password for authentication
        self.is_logged_in = False  # Login status

    def register(self):
        """Simulate user registration."""
        print(f"User {self.name} registered successfully with email: {self.email}")

    def login(self, password):
        """Simulate user login by verifying the password."""
        if self.password == password:
            self.is_logged_in = True
            print(f"User {self.name} logged in.")
        else:
            print("Invalid password.")

    def update_profile(self, name=None, email=None, phone=None, address=None):
        """Update user profile information."""
        if name: self.name = name
        if email: self.email = email
        if phone: self.phone = phone
        if address: self.address = address
        print(f"User profile updated for {self.name}.")

    def logout(self):
        """Simulate user logout."""
        self.is_logged_in = False
        print(f"User {self.name} logged out.")


# Booking Class
class Booking:
    def __init__(self, booking_id, user, service_id, date, time, status="Pending"):
        self.booking_id = booking_id  # Booking identifier
        self.user = user  # Associated user
        self.service_id = service_id  # ID of the booked service
        self.date = date  # Booking date
        self.time = time  # Booking time
        self.status = status  # Booking status

    def confirm_booking(self):
        """Confirm the booking."""
        self.status = "Confirmed"
        print(f"Booking {self.booking_id} confirmed for {self.user.name}.")

    def cancel_booking(self):
        """Cancel the booking."""
        self.status = "Cancelled"
        print(f"Booking {self.booking_id} cancelled for {self.user.name}.")


# Payment Class
class Payment:
    def __init__(self, payment_id, booking, amount, method, status="Pending"):
        self.payment_id = payment_id  # Payment identifier
        self.booking = booking  # Associated booking
        self.amount = amount  # Payment amount
        self.method = method  # Payment method
        self.status = status  # Payment status

    def process_payment(self):
        """Process the payment."""
        self.status = "Paid"
        print(f"Payment {self.payment_id} of {self.amount} processed using {self.method}.")

    def refund(self):
        """Refund the payment."""
        self.status = "Refunded"
        print(f"Payment {self.payment_id} has been refunded.")


# ServiceProvider Class (inherits from User)
class ServiceProvider(User):
    def __init__(self, user_id, name, email, phone, address, user_type, password, provider_id, business_name, description, rating=0, review_count=0):
        super().__init__(user_id, name, email, phone, address, user_type, password)
        self.provider_id = provider_id  # Service provider identifier
        self.business_name = business_name  # Business name
        self.description = description  # Business description
        self.rating = rating  # Average rating
        self.review_count = review_count  # Number of reviews

    def list_service(self):
        """Simulate listing a service."""
        print(f"Service listed by {self.business_name}.")

    def manage_bookings(self):
        """Simulate managing bookings."""
        print(f"{self.business_name} is managing bookings.")


# Service Class
class Service:
    def __init__(self, service_id, name, description, price, availability, provider):
        self.service_id = service_id  # Service identifier
        self.name = name  # Service name
        self.description = description  # Service description
        self.price = price  # Service price
        self.availability = availability  # Availability status
        self.provider = provider  # Associated service provider

    def update_details(self, name=None, description=None, price=None, availability=None):
        """Update service details."""
        if name: self.name = name
        if description: self.description = description
        if price: self.price = price
        if availability is not None: self.availability = availability
        print(f"Service details updated for {self.name}.")


# Messaging Class
class Messaging:
    def __init__(self, message_id, sender, receiver, content, timestamp):
        self.message_id = message_id  # Message identifier
        self.sender = sender  # Sender of the message
        self.receiver = receiver  # Receiver of the message
        self.content = content  # Message content
        self.timestamp = timestamp  # Timestamp of the message

    def send_message(self):
        """Send a message."""
        print(f"Message from {self.sender.name} to {self.receiver.name}: {self.content}")

    def receive_message(self):
        """Receive a message."""
        print(f"Message received by {self.receiver.name}: {self.content}")


# Review Class
class Review:
    def __init__(self, review_id, user, service, rating, comments):
        self.review_id = review_id  # Review identifier
        self.user = user  # User who submitted the review
        self.service = service  # Service being reviewed
        self.rating = rating  # Rating score
        self.comments = comments  # Review comments

    def submit_review(self):
        """Submit a review."""
        print(f"Review submitted for {self.service.name} by {self.user.name}: Rating {self.rating}, Comments: {self.comments}")

    def edit_review(self, new_rating, new_comments):
        """Edit an existing review."""
        self.rating = new_rating
        self.comments = new_comments
        print(f"Review updated: Rating {self.rating}, Comments: {self.comments}")
