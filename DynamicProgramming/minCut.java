class Solution{
    public boolean isPalindrome(String s, int l, int r){
        while (l < r){
            if(s.charAt(l) !=  s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
    public int mincut(String s){
        int n = s.length();
        int[] dp = new int[n+1];
        for(int i = n-1; i >= 0; i--){
            int minCost = Integer.MAX_VALUE;
            for(int j = i; j < n; j++){
                if isPalindrome(s, i, j){
                    int cost = 1 + dp[j+1];
                    minCost = Math.min(minCost, cost);
                }
            }
            dp[i] = minCost;
        }
        return dp[0] - 1;
    }

}