class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(item) for item in version1.strip('.').split('.')]
        v2 = [int(item) for item in version2.strip('.').split('.')]
        if len(v1) > len(v2):
            while len(v1) > len(v2):
                v2.append(0)
        if len(v1) < len(v2):
            while len(v1) < len(v2):
                v1.append(0)
        
        print(v1)
        print(v2)

        for one, two in zip(v1, v2):
            if one > two:
                return 1
            elif two > one:
                return -1

        return 0
        