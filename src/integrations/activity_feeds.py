```python
import stream

# Initialize Stream client
client = stream.connect('STREAM_API_KEY', 'STREAM_API_SECRET')

# Function to update activity feed
def updateActivityFeed(userDetails, activity):
    # Get user feed
    user_feed = client.feed('user', userDetails['id'])

    # Add activity to the feed
    activity_data = {
        'actor': userDetails['id'],
        'verb': activity['verb'],
        'object': activity['object'],
        'foreign_id': activity['foreign_id'],
        'time': activity['time'],
        'message': activity['message']
    }
    user_feed.add_activity(activity_data)

# Example usage
# userDetails = {'id': 'user1'}
# activity = {
#     'verb': 'book',
#     'object': 'service:mass',
#     'foreign_id': 'booking1',
#     'time': '2022-01-01T00:00:00',
#     'message': 'Booked a mass service'
# }
# updateActivityFeed(userDetails, activity)
```