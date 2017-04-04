import pytest
from heap import BinaryHeap


@pytest.fixture
def new_heap():
  return BinaryHeap()


def test_insert(new_heap):
  new_heap.insert(10)
  new_heap.insert(11)
  new_heap.insert(9)
  assert new_heap.view_heap() == [9, 11, 10]


def test_remove_root(new_heap):
  new_heap.insert(10)
  new_heap.insert(11)
  new_heap.insert(9)
  assert new_heap.remove_root() == 9
  assert new_heap.view_heap() == [10, 11]
