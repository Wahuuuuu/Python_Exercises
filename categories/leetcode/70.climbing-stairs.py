#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This function returns the amount of distinct ways to climb to the top of a stair with n steps.

        Parameter
        ---
        self
        n: int

        Return
        ---
        d: int
        """
        if n == 1: return 1

        # init a list stair * n, with stair[0] = stair[1] = 1
        ways: list[int] = [-1] * (n)
        ways[0] = 1
        ways[1] = 2

        def dp(ways: list[int]) -> int:
            """
            Status: ways[i] represents the ways to climb to the top of a stair with i-1 steps
            Update: ways[i] = ways[i-2] + ways[i-1]
            """

            i = 2
            ways.append("sentinel")
            while (ways[i] != "sentinel"):
                ways[i] = ways[i-1] + ways[i-2]
                i += 1
            ways.pop()
            
            return ways[-1]

        return dp(ways)
        
# @lc code=end

