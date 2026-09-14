#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def create_ri(self) -> dict[str, int]:
        return {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        

    def romanToInt(self, s: str) -> int:
        ri = self.create_ri()
        
        s = 0
        for roman in s:
            s += ri[roman]
        
        return s
    

    if __name__ == "__main__":
        s = Solution()
        assert(s.romanToInt("III")) == 3
        assert(s.romanToInt("LVIII")) == 58
        assert(s.romanToInt("MCMXCIV")) == 1994
        assert(s.romanToInt("")) == 
        assert(s.romanToInt("")) == 
        assert(s.romanToInt("")) == 
        
        
# @lc code=end

