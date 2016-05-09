TRACK_TERMS = ["trump", "clinton", "sanders"]
CONNECTION_STRING = "postgresql://vik@localhost:5432/twitter"

try:
    from private import *
except Exception:
    pass