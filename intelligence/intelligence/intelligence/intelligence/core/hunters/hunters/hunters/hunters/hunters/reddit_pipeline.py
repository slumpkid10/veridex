"""
VERIDEX Reddit Pipeline
"""

from hunters.reddit_scanner import RedditScanner
from hunters.reddit_filter import RedditFilter
from intelligence.normalizer import Normalizer
from intelligence.opportunity_queue import OpportunityQueue
from intelligence.decision_engine import DecisionEngine
from intelligence.opportunity import Opportunity
from core.logger import Logger


class RedditPipeline:

    def __init__(self):
        self.scanner = RedditScanner()
        self.filter = RedditFilter()
        self.normalizer = Normalizer()
        self.queue = OpportunityQueue()
        self.decision = DecisionEngine()

    def process_post(self, title, client="Unknown", budget=None):

        if not self.filter.match(title):
            return None

        data = {
            "title": title,
            "client": client,
            "budget": budget,
            "description": title,
        }

        normalized = self.normalizer.normalize("Reddit", data)

        opportunity = Opportunity(
            source=normalized["source"],
            title=normalized["title"],
            client=normalized["client"],
            budget=normalized["budget"],
        )

        opportunity = self.decision.score(opportunity)

        self.queue.add(opportunity)

        Logger.info(
            f"Opportunity queued: {opportunity.title} | Score: {opportunity.score}"
        )

        return opportunity
