import tweepy
import requests
import time
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Set up Tweepy with your Twitter API credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()

    if data['message'] == 'success':
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        return f"The ISS is currently at coordinates (lat: {latitude}, lon: {longitude})"
    else:
        return "Error: Unable to fetch ISS position data."

def tweet_iss_position():
    position = get_iss_position()
    try:
        api.update_status(position)
        print(f"Tweeted: {position}")
    except tweepy.TweepError as e:
        print(f"Error: Unable to tweet. {e}")

# Tweet the ISS position every 15 minutes
while True:
    tweet_iss_position()
    time.sleep(15 * 60)
