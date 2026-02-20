import uuid


class Task:
    def __init__(self, line_ID, headers):
        self.line_ID = line_ID()

    def line_ID(self):
        return uuid.uuid4()
