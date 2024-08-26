class Solution {
public:
    int maxArea(vector<int>& height) {
        int max = INT_MIN;

        int left = 0; 
        int right = height.size()-1;
        int area = 0;
        while (left != right) {
            int width = right - left;
            if (height[left] < height[right]) {
                area = height[left]*width;
                left++;
            }
            else {
                area = height[right]*width;
                right--;
            }
            if (area > max) {
                max = area;
            }
            
        }
        return max;
    }
};