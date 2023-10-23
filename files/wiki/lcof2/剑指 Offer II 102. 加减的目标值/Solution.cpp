class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int s = 0;
        for (int x : nums) s += x;
        if (s - target < 0 || (s - target) % 2 != 0) return 0;
        target = (s - target) / 2 + 1;
        vector<int> dp(target);
        dp[0] = 1;
        for (int i = 1; i < nums.size() + 1; ++i)
        {
            for (int j = target - 1; j >= nums[i - 1]; --j)
            {
                dp[j] += dp[j - nums[i - 1]];
            }
        }
        return dp[target - 1];
    }
};