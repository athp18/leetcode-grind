class Solution { // mashallah better than 100 time complexity
public:
    bool isPerfectSquare(int num) {
        if (num == 0 || num == 1) {
            return true;
        }
        long l = 0;
        long r = (long) num / 2;
        while (l <= r) {
            long mid = (l + r) / 2;
            long target = mid * mid;
            if (target == num) {
                return true;
            } else if (target < num) {
                l = mid + 1;
            } else if (target > num) {
                r = mid - 1;
            }
        }
        return false;
    }
};
