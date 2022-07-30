from typing import List

class Solution:
    def __init__(self):
        pass

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_min = prices[0]
        cur_max = cur_min
        for elm in prices[1:]:
            if elm < cur_min:
                cur_min = elm
                cur_max = cur_min
            elif elm >= cur_max:
                cur_profit = elm - cur_min
                if cur_profit > max_profit:
                    max_profit = cur_profit
                cur_max = elm
        return max_profit


print( Solution().maxProfit([7,1,5,3,6,4]) )
print( Solution().maxProfit([7,6,4,3,1]) )
print( Solution().maxProfit([2,1,2,1,0,1,2]) )
print( Solution().maxProfit([3,3,5,0,0,3,1,4]) )


