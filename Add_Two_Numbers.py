
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        counter = ans
        carry = 0
        while(l1 != None and l2 != None):
        	curr = (l1.val + l2.val + carry)%10
        	carry = int((l1.val + l2.val + carry)/10)
        	temp = ListNode(curr)
        	counter.next = temp
        	counter = counter.next
        	l1 = l1.next
        	l2 = l2.next

        if l2:
        	l1 = l2
        while(l1):
        	curr = (l1.val + carry)%10
        	carry = int((l1.val + carry)/10)
        	temp = ListNode(curr)
        	counter.next = temp
        	counter = counter.next
        	l1 = l1.next

        if(carry!= 0):
        	temp = ListNode(carry)
        	counter.next = temp
        	counter = counter.next

        return ans.next
