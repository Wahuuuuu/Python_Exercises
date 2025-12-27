#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        """
        This function returns the longest distance between any two 
        adjacent 1's in the binary representation of n.
        If there are no two adjacent 1's, return 0.
        """

        longest_distance = curr_distance = 0
        while n > 0:
            if n & 1:
                longest_distance = max(curr_distance, longest_distance)
                curr_distance = 1
            elif curr_distance != 0:  # if some 1 is found
                curr_distance += 1
            
            n >>= 1
    
        return longest_distance



if __name__ == "__main__":
    
    s = Solution()

    assert s.binaryGap(22) == 2
    assert s.binaryGap(8) == 0
    assert s.binaryGap(5) == 2

    assert s.binaryGap(0) == 0

    s.binaryGap(2)



# @lc code=end

