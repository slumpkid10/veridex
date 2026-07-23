"""
VERIDEX Reddit Filter
"""

from hunters.reddit_keywords import KEYWORDS


class RedditFilter:

    def match(self, title):

        title = title.lower()

        for keyword in KEYWORDS:
            if keyword in title:
                return True

        return False
