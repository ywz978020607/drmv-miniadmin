class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        int n = arr.length;
        Map<Integer, Integer> mp = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            mp.put(arr[i], i);
        }
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                dp[j][i] = 2;
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                int delta = arr[i] - arr[j];
                if (mp.containsKey(delta)) {
                    int k = mp.get(delta);
                    if (k < j) {
                        dp[j][i] = dp[k][j] + 1;
                        ans = Math.max(ans, dp[j][i]);
                    }
                }
            }
        }
        return ans;
    }
}