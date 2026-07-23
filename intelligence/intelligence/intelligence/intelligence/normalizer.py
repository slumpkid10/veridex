"""
VERIDEX Opportunity Normalizer
Converts data from different sources into one format.
"""


class Normalizer:
    def normalize(self, source, data):
        return {
            "source": source,
            "title": data.get("title", ""),
            "client": data.get("client", ""),
            "budget": data.get("budget"),
            "description": data.get("description", "")
        }
