print(17 % 3 + 1)

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed

    def clear(self):
        self.queue.clear()

    def write(self):
        for i in range(len(self.queue)):
            print(self.queue)
        
A = Queue()

