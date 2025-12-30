#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        l.reverse()
        print(type(l))
        print(l)
        return " ".join(l)

    

if __name__ == "__main__":
    s = Solution()
    assert(s.reverseWords("the sky is blue")) == "blue is sky the"
    assert(s.reverseWords("  hello world  ")) == "world hello"
    assert(s.reverseWords("a good   example")) == "example good a"






# @lc code=end

