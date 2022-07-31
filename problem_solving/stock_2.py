from typing import List


class Solution:
    def __init__(self):
        pass

    def maxProfit(self, prices: List[int]) -> int:
        c_rest_or_buy = 0
        c_rest_or_sell = int(-prices[0])
        c_cool_down = -10 ^ 6
        for elm in prices[1:]:
            p_rest_or_buy = c_rest_or_buy
            p_rest_or_sell = c_rest_or_sell
            p_cool_down = c_cool_down
            c_rest_or_buy = max(p_rest_or_buy, p_cool_down)
            c_rest_or_sell = max(p_rest_or_sell, p_rest_or_buy - elm)
            c_cool_down = p_rest_or_sell + elm
        return max(c_rest_or_buy, c_cool_down)

print(Solution().maxProfit([1, 2, 3, 0, 2]), '\n')
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]), '\n')
print(Solution().maxProfit([7, 6, 4, 3, 1]), '\n')
print(Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]), '\n')
print(Solution().maxProfit([3, 3, 5, 0, 0, 2, 3, 1, 4, 3, 8]), '\n')
print(Solution().maxProfit([2, 1, 4]), '\n')
print(Solution().maxProfit([2, 1, 4, 5, 2, 9, 7]), '\n')
print(Solution().maxProfit([2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8]), '\n')
print(Solution().maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]), '\n')
print(Solution().maxProfit([8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]), '\n')
