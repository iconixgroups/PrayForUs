import googleanalytics as ga

# Initialize the Google Analytics client
client = ga.Client('UA-XXXXX-Y')

# Define the shared dependencies
userDetails = {}
churchDetails = {}
paymentDetails = {}
bookingDetails = {}
eventDetails = {}
donationDetails = {}
adminDetails = {}

# Define the function to track usage data and events
def trackAnalytics(event_name, event_details):
    # Create a new session
    session = client.session()

    # Track the event
    session.event(event_name, event_details)

# Track user registration
def trackUserRegistration(userDetails):
    trackAnalytics('User Registration', userDetails)

# Track church listing
def trackChurchListing(churchDetails):
    trackAnalytics('Church Listing', churchDetails)

# Track service booking
def trackServiceBooking(bookingDetails):
    trackAnalytics('Service Booking', bookingDetails)

# Track event registration
def trackEventRegistration(eventDetails):
    trackAnalytics('Event Registration', eventDetails)

# Track donation
def trackDonation(donationDetails):
    trackAnalytics('Donation', donationDetails)

# Track church admin registration
def trackAdminRegistration(adminDetails):
    trackAnalytics('Church Admin Registration', adminDetails)