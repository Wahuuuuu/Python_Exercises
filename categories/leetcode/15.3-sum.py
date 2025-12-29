#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:

    def bin_search_first_non_negative(self, nums: list[int]) -> int:
        """
        This function is called by self.init

        This function returns the index of the first non-negative element in nums.
        If there's multiple non-negative elements, returns the one which has the minimum index
        If there's no non-negative elements, retuns -1

        The list is in non-decreasing order
        """
        if nums[-1] < 0:
            return -1

        """
        Invariant
        For every elements with index < left, we have element < 0
        For every elements with index >= right, we have element >= 0
        If there's any non-negative element, it's index must be in the interval [left, right]
        """
        left, right = 0, len(nums)
        while (left < right):
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid

        return right
    

    def init(self, nums: list[int]) -> tuple[int]:
        mid = self.bin_search_first_non_negative(nums)
        # can be zhenghe in while logic
        if mid == -1:
            return []
        left, right = mid-1, mid+1

        print("Init: ", left, mid, right)

        return left, mid, right


    def bin_search_target(self, nums: list[int], left: int, right: int,  target: int) -> int:
        """
        Given the interval of index(left, right), this function returns the index of target in nums
        If nums not in the interval, return -1

        Index left and right are excluded.
        """
        left += 1; right -= 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1


    def expand_edge(self, nums: list[int], left: int, mid: int, right: int) -> tuple[int, int]:
        """
        This function will expand or update the interval (left, right), returning
        a tuple with two int elements. Respectively, they are left and right updated.

        Only one side (left or right) will be expanded.
        Which is the side with minimal difference after the expantion.

        If the difference are the same, expand left
        """
        if left  == 0: return ((left, right+1))
        elif right == len(nums)-1: return (left-1, right)


        diff_left = abs(nums[left - 1] - nums[mid])
        diff_right = abs(nums[right + 1] - nums[mid])

        """ show status
        print(left, mid, right)
        print(nums[left], nums[mid], nums[right])
        print(diff_left, diff_right)
        print("expand left" if diff_left <= diff_right else "expand right")
        """
        return (left - 1, right) if diff_left <= diff_right else (left, right + 1)


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        left, mid, right = self.init(nums)

        sums_up_to_zero = []
        while 0 <= left and right <= len(nums)-1:
            """
            If value of (left + mid + right = 0), then we have value of ( -1 * (left + right) = mid )
            The objective is to search a value equals to -(left + right) in the interval of index (left, right)
            """
            target = -1 * (nums[left] + nums[right])
            index_target = self.bin_search_target(nums, left, right, target)
            if index_target != -1:
                sums_up_to_zero.append([nums[left], nums[index_target], nums[right]])
        
            left, right = self.expand_edge(nums, left, mid, right)


        return sums_up_to_zero



def bsfnn() -> None:
    s = Solution()
    assert s.bin_search_first_non_negative([-1, 0, 1]) == 1
    assert s.bin_search_first_non_negative([0, 1]) == 0
    assert s.bin_search_first_non_negative([-1, -1]) == -1
    assert s.bin_search_first_non_negative([-1, -1, 0, 0, 0, 100]) == 2
    # assert s.bin_search_first_non_negative([0, 0, 0]) == 1


def bst() -> None:
    s = Solution()
    assert s.bin_search_target([-2, 0, 2, 4, 6, 8], 0, 5, 0) == 1
    assert s.bin_search_target([-2, 0, 2, 4, 6, 8], 0, 5, 1) == -1

    # left and right are excluded
    assert s.bin_search_target([-2, 0, 2, 4, 6, 8], 1, 5, 0) == -1
    assert s.bin_search_target([-2, 0, 2, 4, 6, 8], 0, 5, -8) == -1

def ee() -> None:
    s = Solution()
    left, mid, right = 2, 3, 4
    nums = [-6, -3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while 0 <= left and right <= len(nums) - 1:
        left, right = s.expand_edge(nums, left, mid, right)


if __name__ == "__main__":
    bsfnn()
    bst()
    ee()

    s = Solution()
    exp = [[-1,-1,2],[-1,0,1]]
    out = s.threeSum([-1,0,1,2,-1,-4])
    print(exp, out)

    exp = []
    out = s.threeSum([0,1,1])
    print(exp, out)

    exp = [0,0,0]
    out = s.threeSum([0,0,0])
    print(exp, out)





        
# @lc code=end

