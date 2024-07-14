class Solution {
public:
    int getSum(int a, int b) {
        unsigned int carry;
        while (b != 0) {
            carry = (a & b) & 0xFFFFFFFF;  
            a = (a ^ b) & 0xFFFFFFFF; // xor to get sum -- mask to avoid integer overflow
            b = (carry << 1) & 0xFFFFFFFF; 
        }
        
        if (a > 0x7FFFFFFF) {
            a = ~(a ^ 0xFFFFFFFF);
        }
        
        return a;
    }
};
