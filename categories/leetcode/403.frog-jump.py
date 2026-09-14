#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # initialize
        visited_stones: set[int] = {0}

        # possible_destinations[a][b] == x  if the frog can jump to x from a
        possible_destinations: list[int] = [[] for stone in stones]
        possible_destinations[0] = [1]


        
# @lc code=end

