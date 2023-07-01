import webbrowser
import requests

# Replace with your own Client ID and Client Secret
CLIENT_ID = '109977'
CLIENT_SECRET = 'e9728006c1d1bcdba5da14b32434d02acfc2ebdb'

# URL to authorize your application
AUTH_URL = 'https://www.strava.com/oauth/authorize'

# URL to exchange the authorization code for an access token
TOKEN_URL = 'https://www.strava.com/oauth/token'

# Redirect URI for authorization flow (must match the settings of your Strava API application)
REDIRECT_URI = 'http://localhost:8501'

# Open the authorization URL in a browser window
auth_url = f'{AUTH_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=read_all'
webbrowser.open(auth_url)

# After the user authorizes the application, Strava will redirect to the specified REDIRECT_URI with an authorization code

# Retrieve the authorization code from the URL of the redirected page
authorization_code = input('377128e8285ce7d31c3cc30f7aeacadcea718b84')

# Exchange the authorization code for an access token
token_data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'code': authorization_code,
    'grant_type': '54e18dedf11f27ac08c7366c678d2023a73bfd39'
}
response = requests.post(TOKEN_URL, data=token_data)
access_token = response.json()['access_token']

print('Access token:', access_token)
