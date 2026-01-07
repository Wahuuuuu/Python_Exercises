#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        total_zero_subarrays = 0

        length = 0  # length of the current subarray of 0
        for n in nums:
            if n:  # a subarray of zero had just begun
                length = 0
            else:  # a subarray of zero had just end
                length += 1
                total_zero_subarrays += length

        return total_zero_subarrays
            


if __name__ == "__main__":
    s = Solution()
    assert(s.zeroFilledSubarray([1,3,0,0,2,0,0,4])) == 6
    assert(s.zeroFilledSubarray([0,0,0,2,0,0])) == 9
    assert(s.zeroFilledSubarray([2,10,2019])) == 0

    assert(s.zeroFilledSubarray([0,0,0,-2,0,0])) == 9
    assert(s.zeroFilledSubarray([0,0,0,0,0,0,0,0,0])) == sum(i for i in range(1, 9+1))



            
        
# @lc code=end

