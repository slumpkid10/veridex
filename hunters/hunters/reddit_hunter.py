"""
Reddit Hunter
Scans Reddit for opportunities.
"""

from hunters.base_hunter import BaseHunter


class RedditHunter(BaseHunter):
    def __init__(self):
        super().__init__("Reddit")

    def scan(self):
        print("🔍 Scanning Reddit...")
