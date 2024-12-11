class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        print(s)
        ret = []
        for i in range(1, len(nums)+ 1):
            print(i)
            if i not in s:
                ret.append(i)

        return ret
        