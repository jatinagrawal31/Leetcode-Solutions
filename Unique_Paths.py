'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        rows = []
        rows.append([1]*(n))
        for i in range(m):
            temp = [1] + [0]*(n-1)
            rows.append(temp)

        for i in range(1, m):
        	for j in range(1, n):
        		rows[i][j] = rows[i-1][j] + rows[i][j-1]

            
        return rows[m-1][n-1]
        