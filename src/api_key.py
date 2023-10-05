# src/api_key.py

```python
# Importing required libraries
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY')
TWILIO_API_KEY = os.getenv('TWILIO_API_KEY')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
CALENDAR_API_KEY = os.getenv('CALENDAR_API_KEY')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
STREAM_API_KEY = os.getenv('STREAM_API_KEY')
SEGMENT_API_KEY = os.getenv('SEGMENT_API_KEY')
VERCEL_API_KEY = os.getenv('VERCEL_API_KEY')
```
