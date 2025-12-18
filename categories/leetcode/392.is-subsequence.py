#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:    
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        This function returns true if s is subsequence of t

        Parameter
        ---
        s: str, to be justified whether it's subsequence of t
        t: str

        Return
        ---
        is_sub: bool
        """
        if s == "":
            return True

        ps = 0
        for ch_t in t:
            ch_s = s[ps]
            if (ch_t == ch_s):
                ps += 1
                if ps >= len(s):
                    return True

        return False
    

if __name__ == "__main__":
    s = Solution()

    assert s.isSubsequence("abc", "abc")
    assert s.isSubsequence("abc", "ahbgdc")
    assert s.isSubsequence("axc", "ahbgdc") == False
    
    assert s.isSubsequence("", "")
    assert s.isSubsequence("a", "a")
    assert s.isSubsequence("a", "") == False

        
# @lc code=end

