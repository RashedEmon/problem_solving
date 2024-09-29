import math
from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = -1
        temp = head
        while temp:
            index += 1
            temp = temp.next

        if index == 0:
            return None
            
        middle_node = math.ceil(index/2)
        index = -1
        current = head
        prev = head
        while current:
            index += 1
            if index == middle_node and current.next:
                prev.next = current.next
            elif index == middle_node:
                prev.next = None

            prev = current
            current = current.next
        return head
