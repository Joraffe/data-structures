import pytest
from queue import Queue


@pytest.fixture
def new_queue():
  return Queue()


def test_enqueue_and_dequeue(new_queue):
  new_queue.enqueue(1)
  assert new_queue.dequeue() == 1


def test_multiple_enqueue_and_dequeue(new_queue):
  new_queue.enqueue(1)
  new_queue.enqueue(2)
  new_queue.enqueue(3)
  assert new_queue.dequeue() == 1
  new_queue.enqueue(4)
  assert new_queue.dequeue() == 2
  assert new_queue.dequeue() == 3
  assert new_queue.dequeue() == 4
