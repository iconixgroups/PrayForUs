```python
import os

# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the directories for the different modules
USER_REGISTRATION_DIR = os.path.join(BASE_DIR, 'user_registration.py')
USER_PROFILE_DIR = os.path.join(BASE_DIR, 'user_profile.py')
CHURCH_LISTINGS_DIR = os.path.join(BASE_DIR, 'church_listings.py')
SERVICE_BOOKING_DIR = os.path.join(BASE_DIR, 'service_booking.py')
EVENTS_REGISTRATION_DIR = os.path.join(BASE_DIR, 'events_registration.py')
DONATIONS_DIR = os.path.join(BASE_DIR, 'donations.py')
CHURCH_ADMIN_REGISTRATION_DIR = os.path.join(BASE_DIR, 'church_admin_registration.py')

# Define the directories for the different integrations
PAYMENT_GATEWAY_DIR = os.path.join(BASE_DIR, 'integrations', 'payment_gateway.py')
SMS_PROVIDER_DIR = os.path.join(BASE_DIR, 'integrations', 'sms_provider.py')
EMAIL_SERVICE_DIR = os.path.join(BASE_DIR, 'integrations', 'email_service.py')
MAPPING_API_DIR = os.path.join(BASE_DIR, 'integrations', 'mapping_api.py')
CALENDAR_API_DIR = os.path.join(BASE_DIR, 'integrations', 'calendar_api.py')
USER_AUTHENTICATION_DIR = os.path.join(BASE_DIR, 'integrations', 'user_authentication.py')
ACTIVITY_FEEDS_DIR = os.path.join(BASE_DIR, 'integrations', 'activity_feeds.py')
ANALYTICS_DIR = os.path.join(BASE_DIR, 'integrations', 'analytics.py')

# Define the directories for the frontend
REACT_APP_DIR = os.path.join(BASE_DIR, 'frontend', 'react_app.py')
NEXTJS_APP_DIR = os.path.join(BASE_DIR, 'frontend', 'nextjs_app.py')
TYPESCRIPT_APP_DIR = os.path.join(BASE_DIR, 'frontend', 'typescript_app.py')
TAILWIND_APP_DIR = os.path.join(BASE_DIR, 'frontend', 'tailwind_app.py')
REACT_QUERY_APP_DIR = os.path.join(BASE_DIR, 'frontend', 'react_query_app.py')
AXIOS_APP_DIR = os.path.join(BASE_DIR, 'frontend', 'axios_app.py')
CYPRESS_APP_DIR = os.path.join(BASE_DIR, 'frontend', 'cypress_app.py')
VERCEL_APP_DIR = os.path.join(BASE_DIR, 'frontend', 'vercel_app.py')

# Define the directories for the setup and API key
INSTALLATION_GUIDE_DIR = os.path.join(BASE_DIR, 'installation_guide.py')
API_KEY_DIR = os.path.join(BASE_DIR, 'api_key.py')

# Import the modules
import USER_REGISTRATION_DIR
import USER_PROFILE_DIR
import CHURCH_LISTINGS_DIR
import SERVICE_BOOKING_DIR
import EVENTS_REGISTRATION_DIR
import DONATIONS_DIR
import CHURCH_ADMIN_REGISTRATION_DIR

# Import the integrations
import PAYMENT_GATEWAY_DIR
import SMS_PROVIDER_DIR
import EMAIL_SERVICE_DIR
import MAPPING_API_DIR
import CALENDAR_API_DIR
import USER_AUTHENTICATION_DIR
import ACTIVITY_FEEDS_DIR
import ANALYTICS_DIR

# Import the frontend
import REACT_APP_DIR
import NEXTJS_APP_DIR
import TYPESCRIPT_APP_DIR
import TAILWIND_APP_DIR
import REACT_QUERY_APP_DIR
import AXIOS_APP_DIR
import CYPRESS_APP_DIR
import VERCEL_APP_DIR

# Import the setup and API key
import INSTALLATION_GUIDE_DIR
import API_KEY_DIR
```