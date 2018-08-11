'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newCounter = newHead
        while(l1 and l2):
            if(l1.val < l2.val):
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            temp.next = None
            newCounter.next = temp
            newCounter = newCounter.next
        
        if(l1):
            newCounter.next = l1
        if(l2):
            newCounter.next = l2  
            
        return newHead.next