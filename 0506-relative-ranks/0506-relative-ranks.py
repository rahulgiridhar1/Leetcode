class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        n = sorted(score)

        count = len(score)
        dic = {}
        for i, el in enumerate(n):
            if i < (len(score) - 3):
                dic[el] = str(count)
                count -= 1
            elif i < len(score) -2:
                dic[el] = "Bronze Medal"
            elif i < len(score) - 1:
                dic[el] = "Silver Medal"
            elif i < len(score):
                dic[el] = "Gold Medal"
        ret = []
        print(dic)
        for s in score:
            ret.append(dic[s])
        return ret
        