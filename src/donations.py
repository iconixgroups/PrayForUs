```python
from src.integrations.payment_gateway import processPayment
from src.integrations.email_service import sendEmail
from src.user_profile import userDetails
from src.setup import DonationSchema

donationDetails = {}

def makeDonation():
    print("Select from suggested amounts or enter custom amount")
    donationDetails['amount'] = input()
    
    print("Choose one-time or recurring")
    donationDetails['frequency'] = input()
    
    DonationSchema.validate(donationDetails)
    
    processPayment(userDetails['email'], donationDetails['amount'])
    
    sendEmail(userDetails['email'], 'donationConfirmation', donationDetails)
```