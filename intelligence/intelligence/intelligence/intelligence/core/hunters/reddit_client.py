"""
VERIDEX Reddit Client
Handles Reddit API connection.
"""

import os
import praw


class RedditClient:
    def __init__(self):
        self.client = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
        )

    def connection(self):
        return self.client
