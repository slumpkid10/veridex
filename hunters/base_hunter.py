"""
Base Hunter Class
Every hunter inherits from this.
"""

class BaseHunter:
    def __init__(self, name):
        self.name = name

    def scan(self):
        raise NotImplementedError("Each hunter must implement scan().")
