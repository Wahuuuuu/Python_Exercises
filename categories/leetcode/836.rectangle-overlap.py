#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        in_rec1 = lambda x, y: (rec1[0] < x < rec1[2]) and (rec1[1] < y < rec1[3])

        return in_rec1(rec2[0], rec2[1]) or in_rec1(rec2[2], rec2[3]) or rec1 == rec2
    

if __name__ == "__main__":
    s = Solution()
    assert(s.isRectangleOverlap([0,0,2,2], [1,1,3,3])) == True
    assert(s.isRectangleOverlap([0,0,1,1], [1,0,2,1])) == False
    assert(s.isRectangleOverlap([0,0,1,1], [2,2,3,3])) == False

    assert(s.isRectangleOverlap([0,0,1,1], [0,0,1,1])) == True
    assert(s.isRectangleOverlap([0,0,5,5], [1,1,3,3])) == True

        
# @lc code=end

