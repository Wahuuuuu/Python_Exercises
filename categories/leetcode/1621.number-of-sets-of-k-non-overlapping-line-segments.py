#
# @lc app=leetcode id=1621 lang=python3
#
# [1621] Number of Sets of K Non-Overlapping Line Segments
#

# @lc code=start
class Solution:
    def printDp(self, dp) -> None:
        for row in dp:
            print(row)
        print()


    def numberOfSets(self, n: int, k: int) -> int:
        """
        dp[n][k] = the number of ways to draw k non-overlapping line segments in all n points
        
        Init: 
        - for all dp[n][k] which n-1 == k, dp[n][k] = 1
        - for all dp[n][k] which k == 1, dp[n][k] = sum(range(n))

        Transition: dp[n][k] = 
                        dp[n-1][k] 
                        + (dp{n-1}{k-1} + dp{n-2}{k-1} + ... + dp{2}{k-1})
            - In code, the sequence of (dp{n-1}{k-1} + dp{n-2}{k-1} + ... + dp{2)}{k-1}) will be maintained
              in previous_sum.
        
        previous_sum[n] = (dp{n}{k-1} + dp{n-1}{k-1} + ... + dp{2}{k-1})
        """
        # init dp
        dp: list[list[int]] = [[0 for _ in range(k+1)] for _ in range(n+1)]
        for ni in range(2, n+1):
            dp[ni][1] = ni * (ni - 1) // 2

        # init aux
        previous_sum: list[int] = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            previous_sum[i] = previous_sum[i - 1] + dp[i][1]

        # start dp
        for ki in range(2, k+1):
            dp[ki+1][ki] = 1

            for ni in range(ki+2, n+1):
                dp[ni][ki] = dp[ni-1][ki] + previous_sum[ni-1]

            # maintain aux
            for ni in range(n+1):
                if ni < ki:
                    previous_sum[ni] = 0
                else:
                    previous_sum[ni] = dp[ni][ki] + previous_sum[ni-1]
                
        return dp[-1][-1] % (10**9 + 7)



s = Solution()
print(s.numberOfSets(30,7))

# @lc code=end

