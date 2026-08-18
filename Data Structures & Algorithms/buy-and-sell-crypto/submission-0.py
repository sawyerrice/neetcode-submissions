class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        T = [0] * len(prices)
        for i in range(1, len(prices)):
            
                T[i] = max(T[i-1] + prices[i]-prices[i-1],0)
        print(T)

        return max(T)
        