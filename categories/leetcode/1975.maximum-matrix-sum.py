#
# @lc app=leetcode id=1975 lang=python3
#
# [1975] Maximum Matrix Sum
#

# @lc code=start
class Solution:
    def count_negative(self, matrix: list[list[int]]) -> int:
        count = 0
        for row in matrix:
            count += sum(1 for n in row if n < 0)
        
        return count


    def make_matrix_all_positive(self, matrix: list[list[int]]) -> None:
        """
        given a matrix n * n
        """
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                matrix[i][j] = abs(matrix[i][j])


    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        """
        Idea:
        If the amount of the negative values is EVEN, there must be a way to make each of them positive.
        So, the maxim matrix sum in this situation is the sum of the whole matrix in positive.

        If the amount of the negative calues is ODD, there will be inevitably one negative value in the 
        matrix. The way to maximise the matrix is to transform the value with the smallest absolute value
        into a negative value.
        """

        amount_negative = self.count_negative(matrix)
        self.make_matrix_all_positive(matrix)


        sum_all_positive: int = sum(sum(row) for row in matrix)
        if amount_negative % 2 == 0:
            return sum_all_positive
        else:
            return sum_all_positive - 2*(min(min(row) for row in matrix))



if __name__ == "__main__":
    s = Solution()
    assert s.maxMatrixSum([[1,-1],[-1,1]]) == 4
    assert s.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]) == 16

    assert s.maxMatrixSum([[-10, -10], [-10, -10]]) == 40
    assert s.maxMatrixSum([[0, -0], [0, 0]]) == 0
    assert s.maxMatrixSum([[0, -0], [0, 10086]]) == 10086





# @lc code=end

