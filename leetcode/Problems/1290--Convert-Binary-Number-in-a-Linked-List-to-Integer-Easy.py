# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = 0
        
        while(head):
            value = 2*value + head.val
            head = head.next
        
        return value
        