class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = Counter(magazine)
        
        for let in ransomNote:
            if let in count and count[let] > 0:
                print(12)
                count[let] -=1
            else:
                return False
        return True
        