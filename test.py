import requests
import webbrowser

# Replace with the actual access token
access_token = '377128e8285ce7d31c3cc30f7aeacadcea718b84'

API_URL = 'https://www.strava.com/api/v3'

headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(f'{API_URL}/athlete/activities', headers=headers)


def get_user_data():
    if response.status_code == 200:
        activities = response.json()
        for activity in activities:
            # Access individual activity details
            activity_id = activity['id']
            activity_name = activity['name']
            activity_type = activity['type']
            # ... access other desired activity attributes

            return(f"Activity ID: {activity_id}")
    else:
        return ('Error:', response.text)


def get_user_data2():
    client_id = "109977"
    redirect_uri = "https://fitcoin.onrender.com"
    scope = "activity:read_all"  # Replace with the desired scope(s) from Strava API

    # Construct the authentication URL
    auth_url = f"https://www.strava.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"

    # Open the URL in the user's default browser
    webbrowser.open(auth_url)