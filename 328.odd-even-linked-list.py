# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      '''
      variable odd is a pointer of odd indexed node and variable even is a pointer of even indexed node and first_event variable always hold second indexed(event) item.
      Next node of even node always will be odd. Next node of odd node always will be even.
      First assign even.next(which is odd indexed node) to current node. Then assign next of next node of odd to even's next. Assign first_event to odd's next next.
      So main theme is hold two pointer one will always hold last grouped odd and another will point last grouped even.
      Example: in the middle of the process.[1,2,3,4,5,6,7]->[1, 3, 2, 4, 5, 6, 7]
                                                                 ^     ^
                                                                odd   even
                                                                => next of 3 will be next of 4.[line 27] (3 and 4 both pointing 5)
                                                                => next of 4 will point odd.next.next(3->5->6) which is 6. [Line 28] (currently 4 is pointing 6)
                                                                => odd.next.next(3->5->) will be first even (which is 2). [Line 29] 
      '''
        if not head or not head.next:
            return head

        odd = head
        even = odd.next
        first_even = even
        while even.next:
            odd.next = even.next
            even.next = odd.next.next
            odd.next.next = first_even

            even = even.next
            odd = odd.next

            if not even:
                break

        return head
