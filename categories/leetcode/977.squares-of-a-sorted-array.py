#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:

    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        sorted = [-1] * n

        left, right = 0, n-1
        p_sorted = n-1
        while p_sorted >= 0:
            left_val = abs(nums[left])
            right_val = abs(nums[right])

            if left_val >= right_val:
                bigger = left_val
                left += 1
            else: 
                bigger = right_val
                right -= 1

            sorted[p_sorted] = bigger * bigger
            p_sorted -= 1
        
        return sorted




if __name__ == "__main__":
    s = Solution()
    assert (s.sortedSquares([-4,-1,0,3,10])) == [0,1,9,16,100]
    assert (s.sortedSquares([-7,-3,2,3,11])) == [4,9,9,49,121]

    assert (s.sortedSquares([-4])) == [16]
    assert (s.sortedSquares([0])) == [0]







        
# @lc code=end

