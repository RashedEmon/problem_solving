class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

link_list = [1,2,3,4,5,6]

def build_list(link_list):
  head = Node(link_list[0])
  curr = head

  for i in range(1, len(link_list)):
    curr.next = Node(link_list[i])
    curr = curr.next

  return head

def present_list(head):
  while head:
    print(head.val)
    head = head.next
# head = build_list(link_list)
# present_list(head)
