#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        dict_parenthesis = self.construct_dict_parenthesis(s)
        result = []

        i = -1
        lr_direction = True
        while i < len(s):
            i += (1 if lr_direction else -1)
            if i >= len(s): break
            ch = s[i]
            if (ch == "(") or (ch == ")"):
                i = dict_parenthesis[i]
                lr_direction = not lr_direction
            else:
                result.append(ch)

        return "".join(result)


    def construct_dict_parenthesis(self, s: str) -> dict[int, int]:
        dict_parenthesis = {}
        nonclosed = []
        for i, ch in enumerate(s):
            if ch == "(":
                nonclosed.append(i)
            elif ch == ")":
                dict_parenthesis[nonclosed[-1]] = i
                dict_parenthesis[i] = nonclosed[-1]
                nonclosed.pop()

        assert (not nonclosed)
        return dict_parenthesis

                
s = Solution()
print(s.reverseParentheses("(abcd)"))
print(s.reverseParentheses("(u(love)i)"))
print(s.reverseParentheses("(ed(et(oc))el)"))
print(s.reverseParentheses("(())"))
print(s.reverseParentheses("((hello))"))
print(s.reverseParentheses("12((90)87(56)43)12"))





            


                

        
# @lc code=end

