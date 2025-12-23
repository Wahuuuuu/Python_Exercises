#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def generate_binary(self, n: int) -> list[int]:
        """
        This function returns a list that represents n in binary
        """
        if n == 0: return [0]
        
        binary = []
        while n > 0:
            binary.append(n % 2)

            n //= 2
        
        binary.reverse()
        return binary

    
    def binaryGap(self, n: int) -> int:
        """
        This function returns the longest distance between any two 
        adjavent 1's in the binary representation of n.
        If there are no two adjacent 1's, return 0.
        """
        binary_n: list[int] = self.generate_binary(n)

        longest_distance = curr_distance = 0
        for i in range(len(binary_n)):
            if binary_n[i] == 1:
                longest_distance = max(longest_distance, curr_distance)
                curr_distance = 1
            else:  # if binary_n[i] == 0
                curr_distance += 1
    
        return longest_distance



if __name__ == "__main__":
    s = Solution()
    assert s.generate_binary(0) == [0]
    assert s.generate_binary(2) == [1, 0]
    assert s.generate_binary(8) == [1, 0, 0, 0]

    assert s.binaryGap(22) == 2
    assert s.binaryGap(8) == 0
    assert s.binaryGap(5) == 2

    assert s.binaryGap(0) == 0


# @lc code=end

