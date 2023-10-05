```python
import os
from twilio.rest import Client

# Your Twilio account sid and auth token
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

def send_sms(to, body):
    message = client.messages.create(
        body=body,
        from_='+12345678901',  # Your Twilio phone number
        to=to
    )
    return message.sid

def send_booking_confirmation(to, bookingDetails):
    body = f"Booking Confirmation: {bookingConfirmation}. Details: {bookingDetails}"
    return send_sms(to, body)

def send_payment_receipt(to, paymentDetails):
    body = f"Payment Receipt: {paymentReceipt}. Details: {paymentDetails}"
    return send_sms(to, body)

def send_registration_confirmation(to, userDetails):
    body = f"Registration Confirmation: {registrationConfirmation}. Welcome, {userDetails['first_name']}!"
    return send_sms(to, body)

def send_donation_confirmation(to, donationDetails):
    body = f"Donation Confirmation: {donationConfirmation}. Details: {donationDetails}"
    return send_sms(to, body)
```