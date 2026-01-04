#
# @lc app=leetcode id=1390 lang=python3
#
# [1390] Four Divisors
#

# @lc code=start
import math
class Solution:
    def calc_divisors(self, num: int) -> set[int]:
        divisors = set()

        edge = math.isqrt(num) + 1
        for i in range(1, edge):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)

        return divisors



    def sumFourDivisors(self, nums: list[int]) -> int:
        sum_of_div = 0
        for num in nums:
            divisors: set[int] = self.calc_divisors(num)
            if len(divisors) == 4:
                sum_of_div += sum(divisors)

        return sum_of_div
    

if __name__ == "__main__":
    s = Solution()
    assert(s.calc_divisors(21)) == {1, 3, 7, 21}
    assert(s.calc_divisors(4)) == {1, 2, 4}
    assert(s.calc_divisors(1)) == {1}

    assert(s.sumFourDivisors([21,4,7])) == 32
    assert(s.sumFourDivisors([21,21])) == 64
    assert(s.sumFourDivisors([1,2,3,4,5])) == 0

    assert(s.sumFourDivisors([16, 81, 825])) == 0
    assert(s.sumFourDivisors([21,4,7])) == 32
    assert(s.sumFourDivisors([21,4,7])) == 32
# @lc code=end

