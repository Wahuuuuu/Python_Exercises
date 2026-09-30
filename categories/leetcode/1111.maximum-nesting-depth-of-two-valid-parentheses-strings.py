#
# @lc app=leetcode id=1111 lang=python3
#
# [1111] Maximum Nesting Depth of Two Valid Parentheses Strings
#

# @lc code=start
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = [0 for i in range(len(seq))]

        curr_depth = max_depth = B_depth = 0
        owes_B = 0
        for i, ch in enumerate(seq):
            if ch == "(":
                curr_depth += 1

                if curr_depth > max_depth:
                    max_depth = curr_depth
                    if B_depth+1 >= max_depth:
                        answer[i] = 1
                        B_depth += 1
                        owes_B += 1
            else:  # ch == ")"
                curr_depth -= 1

                if owes_B > 0:
                    answer[i] = 1
                    owes_B -= 1
                
                if curr_depth == 0:
                    max_depth = B_depth = 0

        return answer
                

s = Solution()
print(s.maxDepthAfterSplit("(()())"))
                
        
# @lc code=end

