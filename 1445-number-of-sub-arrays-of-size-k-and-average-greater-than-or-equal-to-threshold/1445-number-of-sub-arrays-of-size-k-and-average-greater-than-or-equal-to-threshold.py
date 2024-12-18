class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        n = len(arr)
        target = k * threshold
        cur = sum(arr[:k])
        count = 1 if cur >= target else 0

        for i in range(k, n):
            cur += arr[i] - arr[i - k]
            if cur >= target:
                count += 1
        return count
        