```python
import stripe
from src.user_registration import userDetails
from src.user_profile import paymentDetails

stripe.api_key = "your_stripe_api_key"

def processPayment(amount, currency="usd"):
    try:
        stripe.Charge.create(
            amount=amount,
            currency=currency,
            source=paymentDetails['card'],
            description=f"Charge for {userDetails['email']}"
        )
        return True
    except stripe.error.CardError as e:
        print(f"Card error: {e}")
        return False

def createCustomer():
    try:
        customer = stripe.Customer.create(
            email=userDetails['email'],
            source=paymentDetails['card']
        )
        return customer.id
    except stripe.error.InvalidRequestError as e:
        print(f"Invalid request error: {e}")
        return None

def updatePaymentMethod(customer_id):
    try:
        customer = stripe.Customer.modify(
            customer_id,
            source=paymentDetails['card']
        )
        return True
    except stripe.error.InvalidRequestError as e:
        print(f"Invalid request error: {e}")
        return False
```
