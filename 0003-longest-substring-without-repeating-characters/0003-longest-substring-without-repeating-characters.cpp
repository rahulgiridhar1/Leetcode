class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int count = 0;
        int max = INT_MIN;
        int left = 0;
        set<int> m;
        for (int i = 0; i < s.size(); i++) {
            left = i;
            while (true) {
            if (m.find(s[left]) == m.end()) {
                m.insert(s[left]);
                count++;
                
            }
            else {
                //left = i;
                
                m.clear();
                break;
            }
            if (left == s.size() - 1) {
                break;
            }
            left++;
            }
            if (count > max) {
                max = count;
            }
            count = 0;
           
        }
        if (s.size() == 0) {
            return 0;
        }
        if (s.size() == 1) {
            return 1;
        }
        return max;
    }
};