class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:
      self.storage[self.current] = item
      self.current += 1
    else:
      self.current = 0
      self.storage[self.current] = item
      self.current += 1

  def get(self):
    pass

rb = RingBuffer(5)

rb.append(5)
rb.append(6)
rb.append(3)
rb.append(2)
rb.append(7)
rb.append(10)

print(rb.storage)