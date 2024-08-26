class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        counter = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[counter] = num
                counter = counter + 1

        
        return len(seen)
        