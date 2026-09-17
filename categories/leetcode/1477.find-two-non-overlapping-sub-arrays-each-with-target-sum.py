#
# @lc app=leetcode id=1477 lang=python3
#
# [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum
#

# @lc code=start
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        """
        Maintain an window[left, right], and traverse the arr.
            If sum(window) > target: left += 1
                           < target: right += 1
                           = target: compare to the subarrays
        """
        len_subarray1 = len_subarray2 = target+1

        # traverse the arr and obtain the two len_subarrays
        left = right = 0
        for _ in arr:
            right += 1
            sum_window = sum(arr[left:right])

            while sum_window > target:
                left += 1
                sum_window = sum(arr[left:right])

            # now sum_window <= target
            if sum_window == target:
                # print(f"The sum of these:{arr[left:right]} = target")

                if len_subarray1 >= len_subarray2:
                    len_subarray1 = right-left
                else:
                    len_subarray2 = right-left

                left = right


        if len_subarray1 == target+1 or len_subarray2 == target+1:
            # print("-1", len_subarray1, len_subarray2)
            return -1

        # print(len_subarray1 + len_subarray2)
        return len_subarray1 + len_subarray2



s = Solution()

assert(s.minSumOfLengths([3,2,2,4,3], 3) == 2)
assert(s.minSumOfLengths([7,3,4,7], 7) == 2)
assert(s.minSumOfLengths([4,3,2,6,2,3,4], 6) == -1)
assert(s.minSumOfLengths([4], 4) == -1)
assert(s.minSumOfLengths([4, 4], 4) == 2)



        
# @lc code=end

