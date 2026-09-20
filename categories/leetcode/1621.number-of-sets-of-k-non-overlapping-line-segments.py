#
# @lc app=leetcode id=1621 lang=python3
#
# [1621] Number of Sets of K Non-Overlapping Line Segments
#

# @lc code=start
class Solution:
    def initDp(self, n: int, k: int, dp: list[list[int]]) -> list[list[int]]:
        for ni in range(2, n+1):
            dp[ni][1] = sum(range(ni))

        return dp


    def printDp(self, dp) -> None:
        for _ in dp:
            print(_)
        print()


    def numberOfSets(self, n: int, k: int) -> int:
        """
        dp[n][k] = number of ways we can draw k non-overlapping line segments in all n points
        
        Init: 
        - for all dp[n][k] which n-1 == k, dp[n][k] = 1
        - for all dp[n][k] which k == 1, dp[n][k] = sum(range(n))

        Function: dp[n][k] = dp[n-1][k] + (dp{n-1}{k-1} + dp{n-2}{k-1} + ... + dp{n-(n-2)}{k-1})
            - In code, the sequence of (dp{n-1}{k-1} + dp{n-2}{k-1} + ... + dp{n-(n-2)}{k-1}) will be maintained
              in aux.
              aux[n] represents (dp{n}{k-1} + dp{n-1}{k-1} + ... + dp{n-(n-2)}{k-1})
        """
        dp: list[list[int]] = [[0 for _ in range(k+1)] for _ in range(n+1)]
        dp = self.initDp(n, k, dp)

        # init aux, the aux[n] will not be need
        aux: list[int] = [0 for _ in range(n+1)]
        for i in range(2, n+1):
            aux[i] = aux[i-1] + i-1
            aux[i-1] = aux[i-1] + aux[i-2]

        # start dp
        for ki in range(2, k+1):
            dp[ki+1][ki] = 1

            for ni in range(ki+2, n+1):
                dp[ni][ki] = dp[ni-1][ki] + aux[ni-1]

            # maintain aux
            for ni in range(n+1):
                if ni < ki:
                    aux[ni] = 0
                else:
                    aux[ni] = dp[ni][ki] + aux[ni-1]
                
        return dp[-1][-1] % (10**9 + 7)



s = Solution()
print(s.numberOfSets(30,7))

# @lc code=end

