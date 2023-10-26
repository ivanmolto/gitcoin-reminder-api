import requests
from requests_oauthlib import OAuth1
import os
import json

# Set environment variables in the cloud function
# 'consumer_key'='<consumer_key>'
# 'consumer_secret'='<consumer_secret>'
# 'access_token'='<access_token>'
# 'access_token_secret'='<access_token_secret>'

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")


def gitcoin_reminder():
    reminder = requests.get("https://").json()
    return reminder["reminder"]


def format_reminder(reminder):
    return {"text": "{}".format(reminder)}


def connect_to_oauth(
        consumer_key, 
        consumer_secret, 
        acccess_token, 
        access_token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(
        consumer_key,
        consumer_secret, 
        acccess_token,
        access_token_secret)
    return url, auth


def main():
    reminder = gitcoin_reminder()
    payload = format_reminder(reminder)
    url, auth = connect_to_oauth(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    request = requests.post(
        auth=auth, url=url, json=payload, headers={
            "Content-Type": "application/json"}
    )

    if request.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(
                request.status_code,
                request.text)
        )
    print("Response code: {}".format(request.status_code))

    # Saving the response as JSON
    json_request = request.json()
    print(json.dumps(json_request, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()


"""
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There is an issue with the key or secret entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
) """
