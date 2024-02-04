class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        low=prices[0]
        for i in prices:
            if i < low:
                low = i
            maxprofit=max(maxprofit,i-low)
        return maxprofit
        