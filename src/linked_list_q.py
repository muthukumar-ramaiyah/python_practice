# %%
# Stack implementation using Linked List in Python

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Q:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    self.size += 1

  def remove(self):
    if self.is_empty():
      raise Exception("Q is empty")
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value

  def first(self):
    if self.is_empty():
      return "Q is empty"
    return self.head.value

  def last(self):
    if self.is_empty():
      return "Q is empty"
    return self.tail.value

  def is_empty(self):
    return self.size == 0

  def q_size(self):
    return self.size

  def traverse_n_print(self):
    if self.is_empty():
      raise Exception("Q is empty")
    currentNode = self.head
    while currentNode:
      print(currentNode.value, end=" -> ")
      currentNode = currentNode.next
    print()

print ("__name__", __name__)

if __name__ == "__main__":
    myQ = Q()
    myQ.append('A')
    print("Peek @ start: ", myQ.first())
    print("Peek @ start: ", myQ.last())
    myQ.append('B')
    print("Peek @ start: ", myQ.first())
    print("Peek @ start: ", myQ.last())
    myQ.append('C')
    print("Peek @ start: ", myQ.first())
    print("Peek @ start: ", myQ.last())
    myQ.traverse_n_print()
    myQ.append('D')
    print("Peek @ start: ", myQ.first())
    print("Peek @ start: ", myQ.last())
    myQ.traverse_n_print()
    myQ.remove()
    myQ.traverse_n_print()
    myQ.remove()
    myQ.traverse_n_print()
    myQ.remove()
    myQ.traverse_n_print()
    myQ.remove()
    myQ.traverse_n_print()
    myQ.remove()
    myQ.traverse_n_print()
