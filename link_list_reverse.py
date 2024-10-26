from link_list_builder import build_list, present_list

head = build_list([2,5,7])


def reverse_list(head):
  if not head.next:
    return head

  prev = head
  curr = head.next
  next_node = head.next.next
  prev.next = None

  while curr.next:
    curr.next = prev
    prev = curr
    curr = next_node
    next_node = curr.next

  curr.next = prev

  return curr


head = reverse_list(head)
present_list(head)
