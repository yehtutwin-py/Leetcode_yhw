# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        stack=dummy
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            while list1 and list2:
                if list1.val<list2.val:
                    stack.next=list1
                    list1=list1.next
                else:
                    stack.next=list2
                    list2=list2.next
                stack=stack.next
        if list1:
            stack.next = list1
        else:
            stack.next = list2
        return dummy.next

                    