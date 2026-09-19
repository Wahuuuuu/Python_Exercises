#
# @lc app=leetcode id=1621 lang=python3
#
# [1621] Number of Sets of K Non-Overlapping Line Segments
#

# @lc code=start
class Solution:
    def initDp(self, n: int, k: int, dp: list[list[int]]) -> list[list[int]]:
        for ni in range(2, n+1):
            dp[ni][1] = sum([x for x in range(ni)])

        for i in range(1, k+1):
            dp[i+1][i] = 1

        return dp


    def printDp(self, dp) -> None:
        for _ in dp:
            print(_)
        print()


    def numberOfSets(self, n: int, k: int) -> int:
        """
        dp[n][k] = number of ways we can draw k non-overlapping line segments in all n points
        
        Init: 
        - for all dp[n][k] which n < k, dp[n][k] = 0
        - for all dp[n][k] which n == k, dp[n][k] = 1

        Function: dp[n][k] = dp[n-1][k] + (dp{n-1}{k-1} + dp{n-2}{k-1} + ... + dp{n-(n-2)}{k-1})
        """
        dp: list[list[int]] = [[0 for _ in range(k+1)] for _ in range(n+1)]
        dp = self.initDp(n, k, dp)

        # row 0-2 and column 0-1 are already initialized
        for ni in range(3, n+1):
            for ki in range(2, min(ni-1,k+1)):
                dp[ni][ki] = dp[ni-1][ki] + sum([dp[i][ki-1] for i in range(ni-1, 1, -1)])

        print(dp[-1][-1] % (10**9 + 7))
        return dp[-1][-1] % (10**9 + 7)



s = Solution()
s.numberOfSets(30, 7)

# @lc code=end

