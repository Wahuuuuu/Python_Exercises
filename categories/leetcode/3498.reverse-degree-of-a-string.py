#
# @lc app=leetcode id=3498 lang=python3
#
# [3498] Reverse Degree of a String
#

# @lc code=start
class Solution:
    def reverseDegree(self, s: str) -> int:
        rd = 0
        for i in range(len(s)):
            rd += (ord("z") - ord(s[i]) + 1) * (i+1) 
        return rd



# @lc code=end

