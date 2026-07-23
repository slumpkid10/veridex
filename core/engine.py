"""
VERIDEX Core Engine
"""

from hunters.reddit_hunter import RedditHunter


class VeridexEngine:
    def __init__(self):
        self.status = "READY"
        self.reddit = RedditHunter()

    def start(self):
        print("🚀 VERIDEX Engine Started")
        self.reddit.scan()
