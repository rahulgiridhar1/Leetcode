class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """

        m= events[0][1]
        ind = events[0][0]
        # if len(events) == 1:
        #     return events[0][0]
        for i in range(1, len(events)):
            cur = events[i][1] - events[i-1][1]
            print('hi')
            if cur > m:
                m = cur
                ind = events[i][0]
            if cur == m:
                ind = min(ind, events[i][0])

        return ind

        
        