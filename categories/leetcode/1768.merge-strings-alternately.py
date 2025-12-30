#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        shorter = len1 if len1 <= len2 else len2

        merged = []
        for i in range(shorter):
            merged.append(word1[i])
            merged.append(word2[i])

        merged.append(word1[shorter:])
        merged.append(word2[shorter:])

        return "".join(merged)


if __name__ == "__main__":
    s = Solution()
    assert(s.mergeAlternately("abc", "pqr")) == "apbqcr"
    assert(s.mergeAlternately("ab", "pqrs")) == "apbqrs"
    assert(s.mergeAlternately("abcd", "pq")) == "apbqcd"

    assert(s.mergeAlternately("aa", "b")) == "aba"
    assert(s.mergeAlternately("a", "bb")) == "abb"




        
# @lc code=end

