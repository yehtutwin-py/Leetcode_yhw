# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        if head==None:
            return head
        else:
            while current.next is not None:
                if current.next.val==current.val:
                    current.next=current.next.next
                else:
                        current=current.next
            return head



        