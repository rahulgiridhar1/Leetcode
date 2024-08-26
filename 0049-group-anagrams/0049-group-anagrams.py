class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        overall = []

        map = {}

        for word in strs:
            stry = ''.join(sorted(word))
            if stry not in map:
                map[stry] = []
                map[stry].append(word)
            else:
                map[stry].append(word)
        for key in map:
            overall.append(map[key])

        return overall
        