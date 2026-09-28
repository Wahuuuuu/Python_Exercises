#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#

# @lc code=start
class Solution:

    def count_overlap(self, img1: list[list[int]], img2: list[list[int]], row_zero: int, col_zero: int) -> int:
        size = len(img1)

        overlap = 0
        for i in range(size):
            row = (row_zero + i) % size
            for j in range(size):
                column = (col_zero + j) % size
                if img1[row][column] == img2[i][j] == 1: overlap += 1

        return overlap


    def test_count_overlap(self) -> None:

        t1_img1 = t1_img2 = [[0]]
        assert(self.count_overlap(t1_img1, t1_img2, 0, 0) == 0)

        t2_img1 = t2_img2 = [[1]]
        assert(self.count_overlap(t2_img1, t2_img2, 0, 0) == 1)

        t3_img1 = t3_img2 = [[0, 0, 1],
                             [0, 1, 0],
                             [1, 0, 0]]
        assert(self.count_overlap(t3_img1, t3_img2, 0, 0) == 3)
        

    """
    Move left n times. Meanwhile for each move, move down n times and count the number of overlap.
    Obtain the max overlap possible.
    """
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        size = len(img1)

        largest_overlap = 0
        for row_zero in range(size):
            for column_zero in range(size):
                current_overlap = self.count_overlap(img1, img2, row_zero, column_zero)
                largest_overlap = max(current_overlap, largest_overlap)

                print(f"({row_zero}, {column_zero}). curr_overlap = {current_overlap}, largest_overlap = {largest_overlap}")
            print()

        return largest_overlap


    def test_largestOverlap(self) -> None:
        t1_img1 = [[1,1,0],
                   [0,1,0],
                   [0,1,0]]
        t1_img2 = [[0,0,0],
                   [0,1,1],
                   [0,0,1]]
        assert(self.largestOverlap(t1_img1, t1_img2) == 3)

        t2_img1 = t2_img2 = [[1]]
        assert(self.largestOverlap(t2_img1, t2_img2) == 1)

        t3_img1 = t3_img2 = [[0]]
        assert(self.largestOverlap(t3_img1, t3_img2) == 0)

        t4_img1 = [[0, 1], 
                   [1, 1]]
        t4_img2 = [[1, 1], 
                   [1, 0]]


"""
print("start")
sol = Solution()
sol.test_count_overlap()
sol.test_largestOverlap()
print("end")
"""





        






        
# @lc code=end

