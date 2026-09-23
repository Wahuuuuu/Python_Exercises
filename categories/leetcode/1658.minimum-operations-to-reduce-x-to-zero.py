#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#

# @lc code=start
from collections import deque

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        queue = deque()
        queue.append(((0, len(nums)-1), x, 0))

        while queue:
            (left, right), _x, depth = queue.popleft()
            if _x == 0: return depth
            if left > right: continue

            left_result = _x - nums[left]
            if (left_result >= 0):
                queue.append(((left+1, right), left_result, depth + 1))

            right_result = _x - nums[right]
            if (right_result >= 0):
                queue.append(((left, right-1), right_result, depth + 1))

        return -1


s = Solution()
print(s.minOperations([1,1,4,2,3], 5))
assert(s.minOperations([1,1,4,2,3], 5) == 2)
print(s.minOperations([5,6,7,8,9], 4))
assert(s.minOperations([5,6,7,8,9], 4) == -1)
print(s.minOperations([3,2,20,1,1,3], 10))
assert(s.minOperations([3,2,20,1,1,3], 10) == 5)

print(s.minOperations([1], 1))
assert(s.minOperations([1], 1) == 1)
print(s.minOperations([1,1], 3))
        
# @lc code=end

