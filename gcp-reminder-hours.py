import requests
from requests_oauthlib import OAuth1
from datetime import datetime
import os
import functions_framework
import json
import math


consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
token_secret = os.environ.get("TOKEN_SECRET")
api_url = os.environ.get("API_URL")


def call_to_actions():
    fact = requests.get(
        api_url).json()
    return fact["results"]


def format_call_to_action(fact):
    return {"text": "{}".format(fact)}


def connect_to_oauth(consumer_key,
                     consumer_secret,
                     acccess_token,
                     token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, acccess_token, token_secret)
    return url, auth


@functions_framework.cloud_event
def hello_pubsub(cloud_event):

    current_time_alt = datetime.utcnow()

    facts = call_to_actions()
    for fact in facts:
        start = True
        plural = " hours"

        start_date_str_year = int(fact["event_start_date"][:4])
        start_date_str_month = int(fact["event_start_date"][5:7])
        start_date_str_day = int(fact["event_start_date"][8:10])
        start_date_str_hours = int(fact["event_start_date"][11:13])
        start_date_str_minutes = int(fact["event_start_date"][14:16])
        start_date_str_seconds = int(fact["event_start_date"][17:19])
        start_date = datetime(start_date_str_year, start_date_str_month,
                              start_date_str_day, start_date_str_hours,
                              start_date_str_minutes, start_date_str_seconds)

        end_date_str_year = int(fact["event_end_date"][:4])
        end_date_str_month = int(fact["event_end_date"][5:7])
        end_date_str_day = int(fact["event_end_date"][8:10])
        end_date_str_hours = int(fact["event_end_date"][11:13])
        end_date_str_minutes = int(fact["event_end_date"][14:16])
        end_date_str_seconds = int(fact["event_end_date"][17:19])
        end_date = datetime(end_date_str_year, end_date_str_month,
                            end_date_str_day, end_date_str_hours,
                            end_date_str_minutes, end_date_str_seconds)

        if (current_time_alt < start_date):
            difference = start_date - current_time_alt
            if difference.days == 0:
                seconds_until = difference.seconds
                if seconds_until >= 3600:
                    hours_until = math.trunc(seconds_until / 3600)
                    start = True
                else:
                    exit()
            else:
                exit()
        elif (current_time_alt < end_date):
            difference = end_date - current_time_alt
            if difference.days == 0:
                seconds_until = difference.seconds
                if seconds_until >= 3600:
                    hours_until = math.trunc(seconds_until / 3600)
                    start = False
                else:
                    exit()
            else:
                exit()
        else:
            exit()

        if (hours_until > 1):
            plural = " hours"
        else:
            plural = " hour"

        if start is True:
            status = " starts"
        else:
            status = " closes"

        fact = fact["cta_text"]
        suffix_time = str(hours_until) + plural + " until " + fact + status
        payload = format_call_to_action(suffix_time)

        url, auth = connect_to_oauth(
            consumer_key, consumer_secret, access_token, token_secret
        )
        request = requests.post(
            auth=auth,
            url=url,
            json=payload,
            headers={"Content-Type": "application/json"}
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
