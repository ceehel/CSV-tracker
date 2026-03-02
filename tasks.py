import uuid


class Task:
    def __init__(self, line_ID, headers):
        self.line_ID = line_ID()

    def line_ID(self):
        return uuid.uuid4()

    def task_update(self, line_ID, header, value):
        pass

    def task_delete(self, line_ID):
        pass
