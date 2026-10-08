#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#

# @lc code=start

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        minOp = len(nums)+1
        target = sum(nums) - x

        left, right = 0, 0
        current = nums[0]
        while left < len(nums):
            if current < target:
                # 应该先试探边界再加上 right
                right += 1
            elif current > target:
                left += 1
            else:
                minOp == min(minOp, len(nums) - (right - left))


        if minOp > len(nums):
            return -1

        return minOp



        


s = Solution()
print(s.minOperations([1,1,4,2,3], 5))
# assert(s.minOperations([1,1,4,2,3], 5) == 2)
print(s.minOperations([5,6,7,8,9], 4))
# assert(s.minOperations([5,6,7,8,9], 4) == -1)
print(s.minOperations([3,2,20,1,1,3], 10))
# assert(s.minOperations([3,2,20,1,1,3], 10) == 5)

print(s.minOperations([1], 1))
# assert(s.minOperations([1], 1) == 1)
print(s.minOperations([1,1], 3))
        
# @lc code=end

