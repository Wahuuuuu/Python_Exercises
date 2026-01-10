#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#

# @lc code=start
class Solution:
    def init_mat(self, mat: list[list[int]], s1: str, s2: str) -> None:
        """
        This method initialize the fist column and row of mat
        """
        for i in range(len(s1)):  # init row
            mat[0][1+i] = mat[0][i] + ord(s1[i])

        for i in range(len(s2)):
            mat[1+i][0] = mat[i][0] + ord(s2[i])

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1 = len(s1); l2 = len(s2)
        mat = [[0] * (l1+1) for i in range(l2+1)]
        # len(mat) = len(s2), len(mat[0]) = len(s1)
        self.init_mat(mat, s1, s2)
        
        for i in range(l2):
            for j in range(l1):
                if s1[j] == s2[i]:
                    mat[1+i][1+j] = mat[i][j]
                else:
                    mat[1+i][1+j] = min(mat[1+i][j] + ord(s1[j]), mat[i][j+1] + ord(s2[i]))
        
        return mat[-1][-1]


        

    

if __name__ == "__main__":
    s = Solution()
    assert(s.minimumDeleteSum("sea", "eat")) == 231
    assert(s.minimumDeleteSum("delete", "leet")) == 403



        
# @lc code=end

