```python
def installation_guide():
    print("PrayForUs.in Installation Guide\n")

    print("Step 1: Clone the repository")
    print("git clone https://github.com/yourusername/PrayForUs.in.git\n")

    print("Step 2: Navigate to the project directory")
    print("cd PrayForUs.in\n")

    print("Step 3: Install the required dependencies")
    print("pip install -r requirements.txt\n")

    print("Step 4: Set up your environment variables")
    print("Copy the .env.example file to a new file called .env and replace the placeholder values with your actual values for each variable.\n")

    print("Step 5: Run the application")
    print("python src/main.py\n")

    print("API Keys:")
    print("You will need to obtain API keys for the following services and add them to your .env file:")
    print("- Stripe or Braintree or RazorPay for payment processing")
    print("- Twilio for SMS notifications")
    print("- SendGrid or Mailgun for email notifications")
    print("- Google Maps API or Mapbox for mapping services")
    print("- Google Calendar or Apple Calendar for calendar integration")
    print("- JSON Web Tokens or OAuth for user authentication")
    print("- Stream or PubNub for activity feeds")
    print("- Segment or Google Analytics for analytics\n")

    print("Please refer to the individual service's documentation for instructions on how to obtain these keys.\n")

    print("Happy coding!")

installation_guide()
```