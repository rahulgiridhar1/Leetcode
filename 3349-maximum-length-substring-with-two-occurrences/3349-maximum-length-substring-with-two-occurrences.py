class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        dic = {}
        maxi = 0
        for r in range(len(s)):
            if s[r] not in dic:
                dic[s[r]] = 1
            else:
                dic[s[r]] += 1

            while dic[s[r]] > 2:
                
                dic[s[l]] -= 1
                
                l += 1
            maxi = max(maxi, r - l + 1)

        return maxi
        