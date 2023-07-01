import webbrowser
import requests


API_URL = 'https://www.strava.com/api/v3'

headers = {'Authorization': f'Bearer {"377128e8285ce7d31c3cc30f7aeacadcea718b84"}'}
response = requests.get(f'{API_URL}/athlete/activities', headers=headers)

if response.status_code == 200:
    activities = response.json()
    if activities:
        latest_activity = activities[0]
        print('Latest Activity:', latest_activity)
    else:
        print('No activities found.')
else:
    print('Error:', response.text)
