#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_absol, max_others = (0, 1) if nums[0] > nums[1] else (1, 0)

        for i in range(2, len(nums)):
            if nums[i] > nums[max_absol]:
                max_others = max_absol
                max_absol = i
            elif nums[i] > nums[max_others]:
                max_others = i
        
        return max_absol if nums[max_absol] >= (2 * nums[max_others]) else -1
    

if __name__ == "__main__":
    s = Solution()
    assert s.dominantIndex([3,6,1,0]) == 1
    assert s.dominantIndex([1,2,3,4]) == -1

    assert s.dominantIndex([3,6,1,0,4]) == -1



        
# @lc code=end

