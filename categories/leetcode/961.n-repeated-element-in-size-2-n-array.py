#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return nums[0]
        
        for i in range(2, len(nums)):
            if nums[i] == nums[i-1] or nums[i] == nums[i-2] or nums[i] == nums[i-3]:
                return nums[i]
        
        return None



if __name__ == "__main__":
    s = Solution()
    assert (s.repeatedNTimes([1,2,3,3])) == 3
    assert (s.repeatedNTimes([2,1,2,5,3,2])) == 2
    assert (s.repeatedNTimes([5,1,5,2,5,3,5,4])) == 5

    assert (s.repeatedNTimes([100, 100])) == 100
    assert (s.repeatedNTimes([1,5,1,2,1,3,1,4])) == 1



# @lc code=end

