class Solution {
public:
    string addBinary(string a, string b) {

       
        int i = a.size() - 1;
        int j = b.size() - 1;
        string result = "";
        int extraBit = 0;

        while (i >= 0 || j >= 0 || extraBit > 0) {

            int sum = extraBit;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            
            extraBit = sum / 2;
            result = char((sum % 2) + '0') + result;

        }

        return result;
    }
};
