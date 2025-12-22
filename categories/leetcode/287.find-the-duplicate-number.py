#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def no_rep_before_mid(self, nums: list[int], p: int) -> bool:
        """
        This function returns true if no repetition in the sublist [ :p+1], return False otherwise
        """
        count = 0
        for num in nums:
            if num <= p:
                count += 1
        
        return count <= p


    def findDuplicate(self, nums: list[int]) -> int:
        """
        Invariant
        The repeated integer must in the interval [left, right]
        No repetition occurres in the interval [0, left) and (right, len(nums)-1]
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if self.no_rep_before_mid(nums, mid):
                left = mid + 1
            else:
                right = mid

        
        return right
        
        """
        set method

        def findDuplicate(self, nums: list[int]) -> int:
            appeared_nums = set()
            for num in nums:
                if num in appeared_nums:
                    return num
                
                appeared_nums.add(num)
            
            return "Error, no repeated num detected"
        """


if __name__ == "__main__":
    s = Solution()
    assert s.findDuplicate([1,3,4,2,2]) == 2
    assert s.findDuplicate([3,1,3,4,2]) == 3
    assert s.findDuplicate([3,3,3,3,3]) == 3

    assert s.findDuplicate([1, 1, 2]) == 1

        
# @lc code=end

