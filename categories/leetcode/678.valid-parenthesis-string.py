#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        parenthesis = asterisk = 0
        for i, ch in enumerate(s):
            if ch == "(":
                parenthesis += 1
                if parenthesis > (len(s) - (i+1)): 
                    # if the demanded quantity of ")" or "*" > the ideal remaining quantity
                    # it will be impossible
                                    
                    print(f"At index {i}, asterisk = {asterisk}, parenthesis = {parenthesis}")
                    print(s[i:])
                    print(len(s))

                    return False
            elif ch == "*":
                asterisk += 1
            else:  # ch == ")"
                if parenthesis > 0:
                    parenthesis -= 1
                elif asterisk > 0:
                    asterisk -= 1
                else:
                    print("here2")
                    return False

        return True


s = Solution()
assert(s.checkValidString("(*()") == True)
assert(s.checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()") == True)

"""
assert(s.checkValidString("()") == True)
assert(s.checkValidString("(*)") == True)
assert(s.checkValidString("(*))") == True)
assert(s.checkValidString("(") == False)

assert(s.checkValidString("**") == True)
assert(s.checkValidString("()*") == True)
assert(s.checkValidString("((**") == True)

assert(s.checkValidString(")*(") == False)
assert(s.checkValidString(")*()") == False)
assert(s.checkValidString("()())*") == False)
assert(s.checkValidString(")*") == False)
assert(s.checkValidString("()(*)(") == False)
"""


# @lc code=end

