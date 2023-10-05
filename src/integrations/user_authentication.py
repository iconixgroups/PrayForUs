```python
import jwt
from datetime import datetime, timedelta
from src.user_registration import userDetails

SECRET_KEY = "YOUR_SECRET_KEY"  # Replace with your secret key

def authenticateUser(email, password):
    user = userDetails.get(email)
    if not user or user['password'] != password:
        return None

    token = jwt.encode({
        'id': user['id'],
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, SECRET_KEY)

    return token

def verifyToken(token):
    try:
        payload = jwt.decode(token, SECRET_KEY)
        user = userDetails.get(payload['id'])
        if not user:
            raise jwt.InvalidTokenError
        return user
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
```