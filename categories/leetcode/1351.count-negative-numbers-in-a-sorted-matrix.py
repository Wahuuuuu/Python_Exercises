#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:

    def countNegatives(self, grid: list[list[int]]) -> int:
        """
        This function returns the amount of negative numbers in grid
        For every grid[i][j], we have grid[i][j] >= grid[i+1][j] and grid[i][j] >= grid[i][j+1]
        """
        n = len(grid[0])
        count = 0

        """
        Invariant:
        For each element with index <= left in row, we have row[left] >= 0;
        For each element with index > right in row, we have row[right] < 0;
        If there's any non-negative element in row, the index of the smallest non-negetive element
        must be in the interval [left, right].

        Also, grid[i][j] >= grid[i+1][j] and grid[i][j] >= grid[i][j+1]
        """
        i_smallest_non_negative = n - 1
        for row in grid:
            while 0 <= i_smallest_non_negative and row[i_smallest_non_negative] < 0:
                i_smallest_non_negative -= 1

            # negative number in a row = distance between 
            # the last element and the smallest non-negative element
            count += n-1 - i_smallest_non_negative
        
        return count


if __name__ == "__main__":
    s = Solution()

    assert(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])) == 8
    assert(s.countNegatives([[3,2],[1,0]])) == 0

    assert(s.countNegatives([[-1]])) == 1
    assert(s.countNegatives([[0]])) == 0
    assert(s.countNegatives([[-1, -1, -1]])) == 3

    assert(s.countNegatives([[5,1,0],[-5,-5,-5]])) == 3



        
# @lc code=end

