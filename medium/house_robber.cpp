class Solution {
public:
    int rob(vector<int>& nums) {
        int house1 = 0;
        int house2 = 0;

        for (int num : nums) {
            int temp = max(num + house1, house2);
            house1 = house2;
            house2 = temp;
        }
        return house2;
    }
};
