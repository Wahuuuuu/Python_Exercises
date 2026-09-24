#
# @lc app=leetcode id=3550 lang=python3
#
# [3550] Smallest Index With Digit Sum Equal to Index
#

# @lc code=start
class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            sum_digits = 0

            num = nums[i]
            while num != 0:
                sum_digits += num % 10
                num //= 10

            if sum_digits == i:
                return i

        return -1


s = Solution()
assert(s.smallestIndex([1,3,2]) == 2)
assert(s.smallestIndex([1,10,11]) == 1)
assert(s.smallestIndex([1,2,3]) == -1)

        
# @lc code=end

