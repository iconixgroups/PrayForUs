```python
from datetime import datetime
from src.integrations.payment_gateway import processPayment
from src.integrations.user_authentication import authenticateUser

class ServiceBooking:
    def __init__(self):
        self.bookingDetails = {}

    def bookService(self, userDetails, serviceType, dateTime, specialInstructions):
        if not authenticateUser(userDetails):
            return "User authentication failed"

        self.bookingDetails['serviceType'] = serviceType
        self.bookingDetails['dateTime'] = self.validateDateTime(dateTime)
        self.bookingDetails['specialInstructions'] = specialInstructions

        paymentStatus = processPayment(userDetails['paymentDetails'])

        if paymentStatus == "Success":
            return "Service booked successfully"
        else:
            return "Payment failed. Please try again."

    def validateDateTime(self, dateTime):
        try:
            validDateTime = datetime.strptime(dateTime, '%Y-%m-%d %H:%M:%S')
            return validDateTime
        except ValueError:
            return "Invalid date/time format. Please use 'YYYY-MM-DD HH:MM:SS'"

serviceBooking = ServiceBooking()
```