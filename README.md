# GITCOIN REMINDERS TWITTER BOT

[Gitcoin Reminders](https://twitter.com/gitcoinreminder) is a Twitter bot that tweets reminders about [Gitcoin](https://gitcoin.co) crowdfund related events so you never miss them: Gitcoin Grants rounds,...

It is built using Django for the Admin panel and the REST API, Cloud functions, Cloud Scheduler, and Twitter API version 2.

## Overview

The goal of this bot is to engage with the public conversation in Twitter on starting and ending dates for Gitcoin grants applications/rounds.

This bot parses events from an API that provides Gitcoin events and Tweets them out as follows (following the requirements from [Kevin Owocki](https://twitter.com/owocki))

- It tweets daily about the event starting date until the last 24 hours such as 
`X days until EVENT starts` then
- It tweets hourly about the event starting date until the last hour such as 
`Y hours until EVENT starts` then
- It tweets every 10 minutes about the event starting date until the last 10 minutes such as `Z minutes until EVENT starts`

Once the start date is in the past it tweets in a similar way for the end date.

## Admin Panel
The admin scales to different bots

## REST API

## Cloud Functions

## Cloud Scheduler

After setting up the Cloud Functions, we set up the Cloud Scheduler to determine how often the bot will tweet. 
For this we set up a job and how often it must run.

Daily reminders: `0 18 * * *` - Every day at 18:00 UTC
Hourly reminders:`0 */1 * * *` - Every hour
Minute reminders: `*/10 * * * *` - Every 10 minutes

## Bot

The account for the bot uses a unique handle, profile picture and background that describes the bot's purpose **Gitcoin Reminders**
The bio sets clearly that is a bot.

For this project, we required a [developer account](https://developer.twitter.com) and the creation of a Project and an App with which we generated the credentials required to use the Twitter API. 

The Twitter free tier is enough for this project as it covers the [manage Tweets endpoints](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/introduction)

To authenticate on behalf of the bot account, we used [twurl](https://github.com/twitter/twurl) which is an OAUth-enable curl for the Twitter API.

_twurl_can be easily installed using RubyGems:
`gem install twurl`

With the Twitter App we generated a consumer key and secret. 
Once we had the consumer key and its secret the bot account authorized the developer twitter account to make API request with that consumer key and secret by introducing in the terminal:
`twurl authorize --consumer-key key --consumer-secret secret`

This returns an URL that we needed to open up in a browser and authenticated to Twitter with the bot account getting a **PIN**.
Then entered the returned PIN back into the terminal. 

From there everything is authorized to make requests with the Twitter API using the consumer key, consumer secret, access token and token secret. 

[Go here](https://twitter.com/gitcoinreminder) to start following Gitcoin Reminders

## Tech Stack

This project is built using [Python](https://www.python.org/), [Django](https://www.djangoproject.com/), [Django REST Framework](https://www.django-rest-framework.org), [Google Cloud Functions](https://cloud.google.com/functions), [Cloud Scheduler](https://cloud.google.com/scheduler), [Docker](https://www.docker.com), and the [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/introduction).

## License

The code is licensed under a MIT License.












