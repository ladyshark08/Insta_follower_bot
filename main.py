import time

from InstaFollower import InstaFollower

SIMILAR_ACCOUNT = "https://www.instagram.com/englandcricket/followers/"
USERNAME = "olumideadams1855"
PASSWORD = "Test123!"

account = InstaFollower()
account.login(USERNAME, PASSWORD)
time.sleep(2)
# account.find_followers()
