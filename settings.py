TRACK_TERMS = ["trump", "clinton", "sanders"]
CONNECTION_STRING = "postgresql://vik@localhost:5432/twitter"
CSV_NAME = "tweets.csv"
TABLE_NAME = "election"

try:
    from private import *
except Exception:
    pass