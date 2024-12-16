class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = Counter(s)
     

        for let in t:
            if let in s and m[let] > 0:
                m[let] -= 1
            else:
                return let
        