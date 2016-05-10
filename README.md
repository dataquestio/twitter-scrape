# Twitter Scrape

Scrape tweets from twitter into a DB.  Convert the DB to a CSV file.

## Installation

* `pip install -r requirements.txt`

## Setup

* Create a file called `private.py`.
* Sign up for a Twitter [developer account](https://dev.twitter.com/).
* Create an application [here](https://apps.twitter.com/).
* Set the following keys in `private.py`.  You can get these values from the app you created:
    * `TWITTER_KEY`
    * `TWITTER_SECRET`
    * `TWITTER_APP_KEY`
    * `TWITTER_APP_SECRET`
* Set the following key in `private.py`.
    * `CONNECTION_STRING` -- use `sqlite:///tweets.db` as a default if you need to.  It's recommended to use postgresql, but not necessary.

## Usage

* `python scrape.py` to scrape.  Use `Ctrl + C` to stop.
* `python dump.py` to generate `tweets.csv`, which contains all the tweet data that was scraped.
* If you want to edit behavior, change settings in `settings.py`.