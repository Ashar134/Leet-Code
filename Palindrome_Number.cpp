class Solution {
public:
    bool isPalindrome(int x) {

        long long orignal = x;
        long long remainder;
        long long result = 0;

        if (x < 0) return false;

        while (x != 0) {

            remainder = x % 10;
            result = result * 10 + remainder;
            x /= 10;
        }

        if (orignal == result) {

            return true;
        }

        return false;
    }
};


