class Solution:
    def maxProfit(self, prices) -> int:
        # 772 ms solution
        # left, right = 0, 1
        # profit = 0
        # while right < len(prices):
        #     profit = max(profit, prices[right] - prices[left])
        #     if prices[left] > prices[right]:
        #         left += 1
        #     else:
        #         right += 1            
        # return profit
        # 736 ms solution
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP