class Solution {
public:
    bool isHappy(int n) {
        std::set<int> seen;
        while (n != 1 && seen.find(n) == seen.end()) {
            seen.insert(n);
            n = sumDigits(n);
        }
        if (n == 1) {
            return true;
        } else {
            return false;
        }
    }
private:
    int sumDigits(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
};
