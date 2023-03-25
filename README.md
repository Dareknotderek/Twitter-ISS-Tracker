# ISS Position Twitter Bot
This Python script tweets the International Space Station's (ISS) relative position every 15 minutes using the Tweepy library for interacting with the Twitter API and the 'requests' library for fetching the ISS location data.

## Installation
First, clone the repository:

``` 
git clone https://github.com/dareknotderek/twitter-iss-tracker.git
cd iss_position_twitter_bot
```

Install the required libraries:

``` 
pip install tweepy
pip install requests
```

## Configuration
Create a `config.py` (format provided in `config.py`) file in the project directory with your Twitter API credentials. Replace the placeholders with your own credentials obtained from the Twitter Developer Dashboard.

## Usage
To run the script, execute the following command:

```
python twitter-iss-tracker.py
```

This script will now tweet the ISS's relative position every 15 minutes.
