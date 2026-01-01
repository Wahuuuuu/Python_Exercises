#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:        
        i = len(digits)-1
        while 0 <= i and digits[i] == 9:
            digits[i] = 0
            i -= 1
        
        if i == -1:
            # the i-th digit is assigned with zero
            digits.insert(0, 1)
            return digits
        else:
            digits[i] += 1
            return digits


if __name__ == "__main__":
    s = Solution()
    assert(s.plusOne([1,2,3])) == [1,2,4]
    assert(s.plusOne([4,3,2,1])) == [4,3,2,2]
    assert(s.plusOne([9])) == [1,0]

    assert(s.plusOne([9,9,9,9])) == [1,0,0,0,0]
    assert(s.plusOne([1,0,0,9,9])) == [1,0,1,0,0]


    
# @lc code=end

