#
# @lc app=leetcode id=3498 lang=python3
#
# [3498] Reverse Degree of a String
#

# @lc code=start
class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(self.obtainReverseDegree(s[i]) * (i+1) for i in range(len(s)))


    def obtainReverseDegree(self, ch: str) -> int:
        return ord("z") - ord(ch) + 1




s = Solution()
print(s.reverseDegree("zaza"))
# @lc code=end

