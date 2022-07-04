# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        result = head
        carry = 0

        while l1 or l2:
            if l1 and l2:
                carry = (result.val + l1.val + l2.val)//10
                sum = result.val+l1.val+l2.val -(carry*10)
                result.val = sum
            elif l1:
                result.val = l1.val*(10**i)
            else:
                result.val = l2.val*(10**i)