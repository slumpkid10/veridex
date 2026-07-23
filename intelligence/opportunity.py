"""
VERIDEX Opportunity Model
Represents every opportunity found by hunters.
"""


class Opportunity:
    def __init__(self, source, title, client, budget=None):
        self.source = source
        self.title = title
        self.client = client
        self.budget = budget

        self.score = 0
        self.priority = "NORMAL"
        self.status = "NEW"

    def __str__(self):
        return f"[{self.source}] {self.title} ({self.client})"
