class Solution {
    public int getSum(int a, int b) {
        // XOR and AND + Shift carry 1 operation until there is no more carry
        while (b!=0){
            // AND + Shift carry 1 operation
            int temp = (a & b) << 1;
            // XOR Operation, if same digit return 0 else 1
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}