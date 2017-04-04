# children positions of node at position n is 2n + 1 and 2n + 2
# parent position of node at position n is (n - 1) / 2


class BinaryHeap:
  def __init__(self):
    self._heap = []

  def __sift_up(self, ni):
    node = self._heap[ni]
    pi = ((ni - 1) / 2)
    parent = self._heap[pi]

    if pi >= 0:
      if node < parent:
        self._heap[ni], self._heap[pi] = self._heap[pi], self._heap[ni]
      self.__sift_up(pi)

  def __sift_down(self, ni):
    node = self._heap[ni]
    ci_1 = (2 * ni) + 1
    ci_2 = (2 * ni) + 2

    if ci_1 < len(self._heap):
      c1 = self._heap[ci_1]
      if node > c1:
        self._heap[ni], self._heap[ci_1] = self._heap[ci_1], self._heap[ni]
      self.__sift_down(ci_1)

    if ci_2 < len(self._heap):
      c2 = self._heap[ci_2]
      if node > c2:
        self._heap[ni], self._heap[ci_2] = self._heap[ci_2], self._heap[ni]
      self.__sift_down(ci_2)

  def insert(self, item):
    self._heap.append(item)
    self.__sift_up(len(self._heap) - 1)

  def remove_root(self):
    li = len(self._heap) - 1
    self._heap[0], self._heap[li] = self._heap[li], self._heap[0]

    root = self._heap.pop()
    self.__sift_down(0)

    return root

  def view_heap(self):
    return self._heap
