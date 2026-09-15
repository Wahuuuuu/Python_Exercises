#
# @lc app=leetcode id=2472 lang=python3
#
# [2472] Maximum Number of Non-overlapping Palindrome Substrings
#

# @lc code=start
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        """
        Slides a window of size k or k+1 from lower index to higher index. 
        For each window:
            Check whether palindrome
                Yes: break and start from current's higher+1 index
                No: slides the window, base on: 
                    If size == k: higher index += 1
                    If size == k+1: lowerindex += 1
            Till higher index >= len(s)        
        """
        count = 0
        lower = 0; higher = lower + k - 1
        while higher < len(s):
            _lower, _higher = lower, higher

            # check whether palindrome
            while (_lower < _higher) and (s[_lower] == s[_higher]):
                _lower += 1
                _higher -= 1

            if _lower >= _higher:  # Is palindrome
                count += 1
                lower = higher + 1
                higher = lower + k - 1
            else:                  # Is NOT palindrome
                if higher - lower + 1 == k: 
                    higher += 1
                else:
                    lower += 1 


        return count

s = Solution()
assert(s.maxPalindromes("abaccdbbd", 3) == 2)
assert(s.maxPalindromes("adbcda", 2) == 0)
assert(s.maxPalindromes("a", 3) == 0)
assert(s.maxPalindromes("aaaaa", 1) == 5)
assert(s.maxPalindromes("aaaaa", 2) == 2)


    
        
# @lc code=end

