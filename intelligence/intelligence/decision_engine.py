"""
VERIDEX Decision Engine
Scores opportunities before action.
"""

from intelligence.opportunity import Opportunity


class DecisionEngine:
    def score(self, opportunity: Opportunity):
        score = 50

        if opportunity.budget:
            if opportunity.budget >= 100:
                score += 20
            else:
                score += 10

        opportunity.score = score

        if score >= 70:
            opportunity.priority = "HIGH"
        elif score >= 55:
            opportunity.priority = "MEDIUM"
        else:
            opportunity.priority = "LOW"

        return opportunity
