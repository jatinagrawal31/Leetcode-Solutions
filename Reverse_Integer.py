'''
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if(x < 0 ):
            flag = True
            x = x * -1
        newNumber = x%10
        x = x/10
        while(x != 0):
            newNumber = newNumber*10 + x%10
            x = x/10
        if flag:
            newNumber = newNumber*-1
        if (newNumber>2147483647) or (newNumber<-2147483648) :
            return 0
        return newNumber