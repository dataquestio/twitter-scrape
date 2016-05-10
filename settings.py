TRACK_TERMS = ["trump", "clinton", "sanders", "hillary clinton", "bernie", "donald trump"]
CONNECTION_STRING = ""
CSV_NAME = "tweets.csv"
TABLE_NAME = "election"

try:
    from private import *
except Exception:
    pass