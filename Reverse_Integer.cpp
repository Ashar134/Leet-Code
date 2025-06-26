class Solution {
public:
    int reverse(int x) {

        long long reverse = 0;

        while (x != 0) {

            int rem = x % 10;
            reverse = reverse * 10 + rem;
            x /= 10;

        }

        if (reverse < INT_MIN || reverse > INT_MAX)
            return 0;

        return reverse;
    }
};
