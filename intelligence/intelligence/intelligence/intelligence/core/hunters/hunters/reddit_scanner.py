"""
VERIDEX Reddit Scanner
Scans selected subreddits.
"""

from hunters.reddit_client import RedditClient


class RedditScanner:
    def __init__(self):
        self.reddit = RedditClient().connection()

    def scan(self, subreddit_name):
        subreddit = self.reddit.subreddit(subreddit_name)

        for post in subreddit.new(limit=10):
            print(post.title)
