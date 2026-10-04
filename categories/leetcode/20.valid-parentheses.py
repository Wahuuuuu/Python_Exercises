#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(":")", "[":"]", "{":"}"}
        stack = []

        for ch in s:
            if ch in dic: # ch is an open parenthesis
                stack.append(ch)
            else:  # ch is a close parenthesis
                if (not stack) or (dic[stack[-1]] != ch):
                    return False
                
                stack.pop()
    
        return len(stack) == 0


s = Solution()
assert(s.isValid("()") == True)
assert(s.isValid("()[]{}") == True)
assert(s.isValid("(]") == False)
assert(s.isValid("([])") == True)
assert(s.isValid("([)]") == False)

assert(s.isValid("(([") == False)
assert(s.isValid(")]]") == False)
assert(s.isValid("(") == False)



# @lc code=end

