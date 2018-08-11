'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]'''



class Solution(object):
    
    def generateParanthesis(self, current, count, open_available, balance, ans):
        if(count == 0):
            ans.append(current)
            return ans
        else:
            if(open_available > 0):
                ans = self.generateParanthesis(current + "(", count - 1, open_available - 1, balance + 1, ans )
                
            if(balance > 0):
                ans = self.generateParanthesis(current + ")", count - 1, open_available, balance - 1, ans)
        return ans
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        start = "("
        open_available = n - 1
        balance = 1
        ans = []
        ans = self.generateParanthesis(start, n*2-1, open_available, balance, ans)
        return ans
    
            
        