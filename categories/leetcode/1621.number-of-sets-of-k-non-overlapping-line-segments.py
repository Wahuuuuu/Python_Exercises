#
# @lc app=leetcode id=1621 lang=python3
#
# [1621] Number of Sets of K Non-Overlapping Line Segments
#

# @lc code=start
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        dp: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]
        print(dp)


s = Solution()
s.numberOfSets(2, 2)

# @lc code=end

