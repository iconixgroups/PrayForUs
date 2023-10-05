```python
from vercel import Client

def deploy_to_vercel():
    client = Client('your-vercel-token')

    # Define the project settings
    project_settings = {
        "name": "prayforus",
        "region": "sfo1",
        "framework": "nextjs",
        "public": False,
        "rootDirectory": "src/frontend",
        "build": {
            "env": {
                "REACT_APP_API_KEY": "your-api-key"
            }
        }
    }

    # Create the project
    project = client.create_project(project_settings)

    # Deploy the project
    deployment = client.create_deployment(project['id'], {
        "name": "prayforus-deployment",
        "files": [
            {"file": "src/main.py", "data": open("src/main.py").read()},
            {"file": "src/user_registration.py", "data": open("src/user_registration.py").read()},
            {"file": "src/user_profile.py", "data": open("src/user_profile.py").read()},
            {"file": "src/church_listings.py", "data": open("src/church_listings.py").read()},
            {"file": "src/service_booking.py", "data": open("src/service_booking.py").read()},
            {"file": "src/events_registration.py", "data": open("src/events_registration.py").read()},
            {"file": "src/donations.py", "data": open("src/donations.py").read()},
            {"file": "src/church_admin_registration.py", "data": open("src/church_admin_registration.py").read()},
            {"file": "src/integrations/payment_gateway.py", "data": open("src/integrations/payment_gateway.py").read()},
            {"file": "src/integrations/sms_provider.py", "data": open("src/integrations/sms_provider.py").read()},
            {"file": "src/integrations/email_service.py", "data": open("src/integrations/email_service.py").read()},
            {"file": "src/integrations/mapping_api.py", "data": open("src/integrations/mapping_api.py").read()},
            {"file": "src/integrations/calendar_api.py", "data": open("src/integrations/calendar_api.py").read()},
            {"file": "src/integrations/user_authentication.py", "data": open("src/integrations/user_authentication.py").read()},
            {"file": "src/integrations/activity_feeds.py", "data": open("src/integrations/activity_feeds.py").read()},
            {"file": "src/integrations/analytics.py", "data": open("src/integrations/analytics.py").read()},
            {"file": "src/frontend/react_app.py", "data": open("src/frontend/react_app.py").read()},
            {"file": "src/frontend/nextjs_app.py", "data": open("src/frontend/nextjs_app.py").read()},
            {"file": "src/frontend/typescript_app.py", "data": open("src/frontend/typescript_app.py").read()},
            {"file": "src/frontend/tailwind_app.py", "data": open("src/frontend/tailwind_app.py").read()},
            {"file": "src/frontend/react_query_app.py", "data": open("src/frontend/react_query_app.py").read()},
            {"file": "src/frontend/axios_app.py", "data": open("src/frontend/axios_app.py").read()},
            {"file": "src/frontend/cypress_app.py", "data": open("src/frontend/cypress_app.py").read()},
            {"file": "src/frontend/vercel_app.py", "data": open("src/frontend/vercel_app.py").read()},
            {"file": "src/installation_guide.py", "data": open("src/installation_guide.py").read()},
            {"file": "src/setup.py", "data": open("src/setup.py").read()},
            {"file": "src/api_key.py", "data": open("src/api_key.py").read()}
        ]
    })

    print(f"Deployment URL: {deployment['url']}")

deploy_to_vercel()
```