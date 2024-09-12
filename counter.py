class Counter:
    def __init__(self):
        self.counter = 0

    def get(self):
        self.counter += 1
        return self.counter - 1