# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = '', ''
        temp1, temp2 = l1, l2
        while temp1 != None:
            s1 += str(temp1.val)
            temp1 = temp1.next
        while temp2 != None:
            s2 += str(temp2.val)
            temp2 = temp2.next

        num = int(s1[::-1]) + int(s2[::-1])
        num = str(num)[::-1]

        head = ListNode()
        temp = head

        for i in range(len(num)):
            temp.val = num[i]
            
            if i < len(num) - 1:
                temp.next = ListNode()
                temp = temp.next
        return head
