from datetime import datetime


class History:

    def __init__(self):

        self.events = []

    def add(self, action):

        self.events.append({

            "time": datetime.now(),

            "action": action

        })

    def latest(self):

        return self.events[-10:]
