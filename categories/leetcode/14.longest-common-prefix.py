#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def search_shortest(self, strs: list[str]) -> int:
        shortest = len(strs[0])
        for word in strs:
            shortest = min(shortest, len(word))
        
        return shortest
    

    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_word_len = self.search_shortest(strs)

        longest_pref = []
        for i in range(shortest_word_len):
            
            curr_pref: str = strs[0][i]
            for word in strs:
                if (word[i] != curr_pref):
                    return "".join(longest_pref)
            
            longest_pref.append(curr_pref)

        return "".join(longest_pref)
    

if __name__ == "__main__":
    s = Solution()
    assert(s.longestCommonPrefix(["flower","flow","flight"])) == "fl"
    assert(s.longestCommonPrefix(["dog","racecar","car"])) == ""

    assert(s.longestCommonPrefix([""])) == ""
    assert(s.longestCommonPrefix(["iiii", "", "i"])) == ""
    assert(s.longestCommonPrefix(["Wahuuuuu", "Wahuuuuu", "Wahuuuuu"])) == "Wahuuuuu"


    
    # assert(s.longestCommonPrefix()) == 



        
# @lc code=end

