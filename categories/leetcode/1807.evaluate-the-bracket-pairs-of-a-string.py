#
# @lc app=leetcode id=1807 lang=python3
#
# [1807] Evaluate the Bracket Pairs of a String
#

# @lc code=start
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dict_knowledge = {key:value for key, value in knowledge}

        result = ""
        in_brackets = False
        for letter in s:
            if not in_brackets:
                if letter == "(":
                    in_brackets = True
                    bracket_content = ""
                else:
                    result += letter
            else:
                if letter == ")":
                    in_brackets = False
                    result += dict_knowledge.get(bracket_content, "?")

                else:
                    bracket_content += letter

        return result


    def optimized_evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dict_knowledge = {key:value for key, value in knowledge}
        result = []

        left = 0
        in_brackets = False
        for i, letter in enumerate(s):
            if not in_brackets:
                if letter == "(":
                    in_brackets = True

                    result.append(s[left:i])
                    left = i+1
            else:
                if letter == ")":
                    in_brackets = False

                    key = s[left:i]
                    result.append(dict_knowledge.get(key, "?"))
                    left = i+1

        if left != len(s):
            result.append(s[left:])

        return "".join(result)

                
s = Solution()
print(s.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]))
print(s.evaluate("hi(name)", [["a","b"]]))
print(s.evaluate("(a)(a)(a)aaa", [["a","yes"]]))

print(s.evaluate("original", []))
print(s.evaluate("(a)", []))

        
# @lc code=end

