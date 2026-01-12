#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
class Solution:
    def calc_time(self, p1: tuple[int, int], p2: tuple[int, int]) -> int:
        vector: tuple[int, int] = (p1[0]-p2[0], p1[1]-p2[1])
        return max(abs(vector[0]), abs(vector[1]))


    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        tot_time = 0

        for i in range(len(points)-1):
            tot_time += self.calc_time(points[i], points[i+1])

        return tot_time


if __name__ == "__main__":
    s = Solution()
    assert(s.calc_time((1, 1), (3, 4))) == 3
    assert(s.calc_time((3, 4), (-1, 0))) == 4

    assert(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])) == 7
    assert(s.minTimeToVisitAllPoints([[3,2],[-2,2]])) == 5
    
    assert(s.minTimeToVisitAllPoints([[1,1]])) == 0
    assert(s.minTimeToVisitAllPoints([[1,1], [1, 1]])) == 0



        
# @lc code=end

