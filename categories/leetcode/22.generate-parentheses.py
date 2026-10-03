#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # the elements means (<pair>, <open parenthesis>, <close parenthesis>), respectfully
        prev = [("(", n-1, n)]
        curr = None

        for _ in range(2*n - 1):
            curr = [None for _ in range(len(prev))]  # append a new level, which's length = curr
            for j, stat in enumerate(prev):
                if stat[1] == 0:  # append ")"
                    curr[j] = self.append_parenthesis(stat, ")")
                elif stat[1] == stat[2]:
                    curr[j] = self.append_parenthesis(stat, "(")
                elif stat[1] < stat[2]:  # append ")" and append "("
                    curr[j] = self.append_parenthesis(stat, ")")
                    curr.append(self.append_parenthesis(stat, "("))
                else:
                    print(f"happening open < close: pair = {stat[0]}, op = {stat[1]}, cl = {stat[2]}")
                    return

            prev = curr
            curr = []

        return [stat[0] for stat in prev]


    def append_parenthesis(self, stat: tuple[str, int, int], parenthesis: str) -> tuple[str, int, int]:
        if parenthesis == "(":
            return (stat[0] + "(", stat[1] - 1, stat[2])
        else:
            return (stat[0] + ")", stat[1], stat[2] - 1)



s = Solution()
result_8 = s.generateParenthesis(8)
print(len(result_8), len(set(result_8)))

print(s.generateParenthesis(3))
print(s.generateParenthesis(1))








    


        

s = Solution()
s.generateParenthesis(3)

        
# @lc code=end

