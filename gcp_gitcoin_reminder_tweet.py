import requests
from requests_oauthlib import OAuth1
import os
import functions_framework
import json


consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
token_secret = os.environ.get("TOKEN_SECRET")

payload = {"text": "Public Goods are Good"}


def connect_to_oauth(consumer_key, consumer_secret, acccess_token, 
                     token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, acccess_token, token_secret)
    return url, auth


@functions_framework.cloud_event
def hello_pubsub(cloud_event):

    url, auth = connect_to_oauth(
        consumer_key, consumer_secret, access_token, token_secret
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