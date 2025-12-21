#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        appeared_nums = set()
        for num in nums:
            if num in appeared_nums:
                return num
            
            appeared_nums.add(num)
        
        return "Error, no repeated num detected"
    


if __name__ == "__main__":
    s = Solution()
    assert s.findDuplicate([1,3,4,2,2]) == 2
    assert s.findDuplicate([3,1,3,4,2]) == 3
    assert s.findDuplicate([3,3,3,3,3]) == 3
        
# @lc code=end

