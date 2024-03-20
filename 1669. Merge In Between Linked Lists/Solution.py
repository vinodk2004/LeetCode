# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        prev = None
        current = list1

        while count < a:
            prev = current
            current = current.next
            count += 1
        
        while count <= b:
            current = current.next
            count += 1
        
        prev.next = list2

        while list2.next != None:
            list2 = list2.next
        
        list2.next = current

        return list1