# Created by Eddie Garcia at 11/28/19

# Queue
# First in first out.

class Queue:
    def __init__(self, head=None):
        self.queue = []
        if head is not None:
            self.queue.append(head)

    def put(self, i=None):
        if i is None and not self.is_empty():
            return self.queue.pop(0)
        self.queue.append(i)

    def is_empty(self):
        return len(self.queue) == 0
