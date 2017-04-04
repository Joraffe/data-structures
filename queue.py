from stack import Stack


# Implementation using two stacks
class Queue:
  def __init__(self):
    self.inbox = Stack()
    self.outbox = Stack()

  def enqueue(self, item):
    self.inbox.push(item)

  def dequeue(self):
    if self.outbox.size() == 0:
      while self.inbox.size() != 0:
        self.outbox.push(self.inbox.pop())

    return self.outbox.pop()

  def size(self):
    return self.inbox.size() + self.outbox.size()
