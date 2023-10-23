class Solution {
    public int divide(int a, int b) {
        int sign = 1;
        if ((a < 0) != (b < 0)) {
            sign = -1;
        }
        long x = abs(a);
        long y = abs(b);
        long tot = 0;
        while (x >= y) {
            int cnt = 0;
            while (x >= (y << (cnt + 1))) {
                cnt++;
            }
            tot += 1L << cnt;
            x -= y << cnt;
        }
        long ans = sign * tot;
        if (ans >= Integer.MIN_VALUE && ans <= Integer.MAX_VALUE) {
            return (int) ans;
        }
        return Integer.MAX_VALUE;
    }

    private long abs(long a) {
        if (a < 0) {
            return -a;
        }
        return a;
    }
}
