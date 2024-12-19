class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        cur = 0
        if sum(nums) < target:
            return 0
        mini = 100000
        for r in range(len(nums)):
            cur += nums[r]

            while cur >= target:
                # if (cur - nums[l]) < target:
                #     break
                mini = min(mini, r - l + 1)
                cur -= nums[l]
                l += 1
                
            
            

        return mini
        