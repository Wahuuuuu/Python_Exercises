#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    
    def update_period(self, prices: list[int], period1: tuple[int, int], period2: tuple[int, int]) -> tuple[int, int]:
        profit1 = prices[period1[1]] - prices[period1[0]]
        profit2 = prices[period2[1]] - prices[period2[0]]

        return period1 if profit1 >= profit2 else period2
    
    
    
    def maxProfit(self, prices: list[int]) -> int:
        """
        This function returns the maximum profit can make in the given period of days

        Parameters
        ---
        self
        prices: list[int], with 1 <= len(prices) <= 10^5

        Return
        ---
        profit: int
        """
        
        # init
        final_period = (0, 0)  # period[0] and period[1] refers to the index of the buy and sell

        # dp traverse, start from index 1
        possible_period = [0, 0]
        for i in range(1, len(prices)):
            may_buy, may_sell = (i-1, i) if prices[i-1] <= prices[i] else (i, i-1)

            print(may_buy, may_sell)
            print(possible_period)

            # intend for buy
            if prices[may_buy] < prices[possible_period[0]]:
                final_period = self.update_period(prices, final_period, possible_period)

                # init possible period
                possible_period = [may_buy, may_buy]
            
            # intend for sell
            if prices[possible_period[1]] < prices[may_sell]:
                possible_period[1] = may_sell
        
        # 需要吗
        # update_period(final_period, possible_period)

        print(prices[final_period[1]] - prices[final_period[0]])
        return prices[final_period[1]] - prices[final_period[0]]



if __name__ == "__main__":
    s = Solution()
    assert s.update_period([1, 2, 3, 3], (0, 1), (2, 3)) == (0, 1)
    assert s.update_period([1, 2, 3, 5], (0, 1), (2, 3)) == (2, 3)
    assert s.maxProfit([7,1,5,3,6,4]) == 5
# @lc code=end

