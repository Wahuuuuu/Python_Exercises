#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = curr_depth = 0
        for ch in s:
            if ch == "(":
                curr_depth += 1
                if curr_depth > max_depth: max_depth = curr_depth 
            elif ch == ")":
                curr_depth -= 1

        return max_depth
        
# @lc code=end

