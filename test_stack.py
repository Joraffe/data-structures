import pytest
import sys
from stack import Stack

sys.dont_write_bytecode = True


@pytest.fixture
def new_stack():
  return Stack()


def test_push_and_pop(new_stack):
  new_stack.push(1)
  assert new_stack.pop() == 1


def test_multiple_push_and_pop(new_stack):
  new_stack.push(1)
  new_stack.push(2)
  new_stack.push(3)
  assert new_stack.pop() == 3
  new_stack.push(4)
  assert new_stack.pop() == 4
  assert new_stack.pop() == 2
  assert new_stack.pop() == 1
