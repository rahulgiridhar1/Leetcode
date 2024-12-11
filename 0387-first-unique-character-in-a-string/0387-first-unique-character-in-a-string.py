class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = {}
        for l in s:
            if l not in count:
                count[l] = 1
            else:
                count[l] += 1
        
        for n in range(len(s)):
            if s[n] in count and count[s[n]] == 1:
                return n
        return -1
        