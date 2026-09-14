#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

# @lc code=start
class Solution:
    """
    If (no overlap on axis x) and (no overlap on axis y), no overlap on rectangle
    """
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        
        overlap_x = self.isAxisOverlap(rec1[0], rec1[2], rec2[0], rec2[2])
        overlap_y = self.isAxisOverlap(rec1[1], rec1[3], rec2[1], rec2[3])

        return overlap_x and overlap_y
        

    
    """
    lower1 <= higher1
    lower2 <= higher2
    """
    def isAxisOverlap(self, lower1: int, higher1: int, lower2: int, higher2: int) -> bool:
        if (higher1 <= lower2) or (higher2 <= lower1) : 
            return False
        
        return True
    

if __name__ == "__main__":
    s = Solution()
    assert(s.isRectangleOverlap([0,0,2,2], [1,1,3,3])) == True
    assert(s.isRectangleOverlap([0,0,1,1], [1,0,2,1])) == False
    assert(s.isRectangleOverlap([0,0,1,1], [2,2,3,3])) == False

    assert(s.isRectangleOverlap([0,0,1,1], [0,0,1,1])) == True
    assert(s.isRectangleOverlap([0,0,5,5], [1,1,3,3])) == True

        
# @lc code=end

