# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while (head and head.next):
            temp = head
            temp1 = head.next
            prev.next = temp1
            temp.next = temp1.next
            temp1.next = temp
            prev = temp
            #dummy = temp1
            head = temp.next
        return dummy.next
        