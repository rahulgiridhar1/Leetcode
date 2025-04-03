class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
    
    # Step 2: Initialize the result list with the first interval
        merged = []
        
        for interval in intervals:
            # If merged is empty or no overlap with the last interval, append the current one
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge the intervals by updating the end time of the last merged interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
        