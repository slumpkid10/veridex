"""
VERIDEX Client Memory
Stores client history and interactions.
"""


class ClientMemory:
    def __init__(self):
        self.clients = {}

    def remember(self, client, data):
        self.clients[client] = data

    def recall(self, client):
        return self.clients.get(client)
