class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        completeStairs = 0

        start = 1
        end = (n + 1) // 2
        
        while start <= end:
            mid = start + (end - start) // 2
			# How many coins required to completely fill 'mid' rows?
			# Use Gauss Summation to find that in O(1) time
            if (mid * ( mid + 1)) // 2 <= n:
                completeStairs = mid
                start = mid + 1
            else:
                end = mid - 1


        return completeStairs
        