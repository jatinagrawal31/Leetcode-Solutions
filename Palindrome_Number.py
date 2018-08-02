'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return False
        newNumber = x%10
        num = x/10
        while(num!= 0):
            newNumber = newNumber*10 + num%10
            num/= 10
        if(newNumber == x):
            return True
        else:
            return False