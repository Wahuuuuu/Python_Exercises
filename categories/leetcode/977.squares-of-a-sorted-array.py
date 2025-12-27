#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:

    def search_edge(self, nums: list[int]) -> int:
        """
        This function returns the index of the first positive element (included 0)
        If there's no positive element in nums, return len(nums)
        """

        """
        Invariant:
        If there's any element >= 0, the first positive element must be in the interval [left, right] 
        For every elements with index < left, we have nums[left] < 0
        For every elements with index >= right, we have nums[left] >= 0
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid

        return right


    def sortedSquares(self, nums: list[int]) -> list[int]:
        edge = self.search_edge(nums)

        pos = edge
        neg = edge - 1

        sorted = []
        while 0 <= neg and pos < len(nums):

            val_neg, val_pos = abs(nums[neg]), nums[pos]
            if val_neg < val_pos:
                smaller = val_neg
                neg -= 1
            else:
                smaller = val_pos
                pos += 1
            
            sorted.append(smaller * smaller)
        

        # append the rest of elements
        for p in range(pos, len(nums)):
            sorted.append(nums[p]*nums[p])

        for n in range(neg, -1, -1):
            sorted.append(nums[n]*nums[n])
        
        print(sorted)
        return sorted
    

if __name__ == "__main__":
    s = Solution()
    assert (s.search_edge([-1, 0, 1, 2])) == 1
    assert (s.search_edge([0, 1, 2])) == 0
    assert (s.search_edge([-0, -1, -2])) == 3

    assert (s.sortedSquares([-4,-1,0,3,10])) == [0,1,9,16,100]
    assert (s.sortedSquares([-7,-3,2,3,11])) == [4,9,9,49,121]

    assert (s.sortedSquares([-4])) == [16]
    assert (s.sortedSquares([0])) == [0]







        
# @lc code=end

