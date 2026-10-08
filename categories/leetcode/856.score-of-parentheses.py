#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        sum_score = 0
        unit_score = 0

        for i in range(1, len(s)):
            window = [s[i-1], s[i]]
            if window == ["(", "("]:
                score += 0
            elif window == ["(", ")"]:
                score += 1
            elif window == [")", ")"]:
                score *= 2
            else:  # window == [")", "("]
                sum_score += unit_score
                unit_score = 0


        
# @lc code=end

