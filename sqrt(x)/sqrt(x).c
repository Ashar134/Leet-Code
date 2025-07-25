int mySqrt(int x) {

    if (x == 0 || x == 1)
        return x;

    int left = 1;
    int right = x;
    int ans = 0;

    while (left <= right) {
        long long mid = left + (right - left) / 2;

        if (mid * mid == x) {
            return mid;
        }    
        else if (mid * mid < x) {
            left = mid + 1;
            ans = mid; 

        } else {
            right = mid - 1;
        }
    }

    return ans;
}
