```python
import requests
from datetime import datetime
from src.user_profile import userDetails, bookingDetails

# Google Calendar API URL
CALENDAR_API_URL = "https://www.googleapis.com/calendar/v3/calendars/primary/events"

# User's access token (should be fetched dynamically)
ACCESS_TOKEN = "user_access_token"

def create_event(booking):
    """
    Create a new event in the user's Google Calendar for a booking.
    """
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Prepare the event data
    event_data = {
        "summary": f"{booking['service_type']} at {booking['church_name']}",
        "description": booking.get('special_instructions', ''),
        "start": {
            "dateTime": booking['date_time'].isoformat(),
            "timeZone": "Asia/Kolkata",
        },
        "end": {
            "dateTime": (booking['date_time'] + timedelta(hours=1)).isoformat(),
            "timeZone": "Asia/Kolkata",
        },
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 24 * 60},
                {"method": "popup", "minutes": 10},
            ],
        },
    }

    # Send the request to the Google Calendar API
    response = requests.post(CALENDAR_API_URL, headers=headers, json=event_data)

    # Check the response
    if response.status_code == 200:
        print("Event created successfully!")
    else:
        print(f"Failed to create event: {response.content}")

def integrate_bookings_with_calendar():
    """
    Integrate user's bookings with their Google Calendar.
    """
    for booking in bookingDetails:
        create_event(booking)
```
