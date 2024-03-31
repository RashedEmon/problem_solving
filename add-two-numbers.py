# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result=ListNode()
        head=result
        iterator1=l1
        iterator2=l2
        carry=0
        i=0
        while (iterator1 is not None) or (iterator2 is not None) or carry:
            value1=0
            value2=0
            #if not none then iterator1 have a value otherwise value1 equal zero
            if iterator1 is not None:
                value1=iterator1.val
                iterator1=iterator1.next
            #if not none then iterator2 have a value otherwise value1 equal zero
            if iterator2 is not None:
                value2=iterator2.val
                iterator2=iterator2.next
                
            sum=(value1+value2+carry)%10
            carry = (value1+value2+carry)//10
        
            node=ListNode(sum)
            result.next=node
            result=node
        return head.next
