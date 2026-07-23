"""
VERIDEX Opportunity Queue
Stores opportunities waiting for evaluation.
"""

class OpportunityQueue:
    def __init__(self):
        self.queue = []

    def add(self, opportunity):
        self.queue.append(opportunity)

    def get_all(self):
        return self.queue

    def clear(self):
        self.queue.clear()
