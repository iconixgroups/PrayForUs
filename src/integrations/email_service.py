```python
import sendgrid
from sendgrid.helpers.mail import Mail

def sendEmail(email, subject, message):
    message = Mail(
        from_email='no-reply@prayforus.in',
        to_emails=email,
        subject=subject,
        plain_text_content=message)

    try:
        sg = sendgrid.SendGridAPIClient('SENDGRID_API_KEY')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

def registrationConfirmation(userDetails):
    email = userDetails['email']
    subject = 'Welcome to PrayForUs.in'
    message = f"Hello {userDetails['first_name']},\n\nThank you for registering at PrayForUs.in. We are excited to have you with us.\n\nBest,\nPrayForUs Team"
    sendEmail(email, subject, message)

def bookingConfirmation(bookingDetails):
    email = bookingDetails['userDetails']['email']
    subject = 'Your Service Booking Confirmation'
    message = f"Hello {bookingDetails['userDetails']['first_name']},\n\nYour booking for {bookingDetails['service_type']} on {bookingDetails['date_time']} has been confirmed.\n\nBest,\nPrayForUs Team"
    sendEmail(email, subject, message)

def donationConfirmation(donationDetails):
    email = donationDetails['userDetails']['email']
    subject = 'Your Donation Confirmation'
    message = f"Hello {donationDetails['userDetails']['first_name']},\n\nThank you for your generous donation of {donationDetails['amount']}.\n\nBest,\nPrayForUs Team"
    sendEmail(email, subject, message)
```