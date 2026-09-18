#
# @lc app=leetcode id=1520 lang=python3
#
# [1520] Maximum Number of Non-Overlapping Substrings
#

# @lc code=start
class Solution:
    def createDictOfIntervals(self, s: str) -> dict[str, list[int]]:
        intervals: dict[str, list[int]] = dict()
        for i in range(len(s)):
            letter = s[i]
            if letter in intervals:
                intervals[letter][-1] = i
            else:
                intervals[letter] = [i, i]
        return intervals

    def expandIntervals(self, s: str, intervals: dict[str, list[int]]) -> dict[str, list[int]]:
        for letter in intervals:
            checked = False
            while (not checked):
                letter_start, letter_end = intervals[letter][0], intervals[letter][1]

                interval = s[letter_start+1 : letter_end]
                for element in interval:
                    element_start, element_end = intervals[element][0], intervals[element][1]

                    if element_start < letter_start:
                        intervals[letter][0] = intervals[element][0]
                        checked = False
                        break

                    if element_end < letter_end:
                        intervals[element][1] = intervals[letter][1]
                        checked = False
                        break

                    checked = True
        
        return intervals
        

    def printDict(self, d: dict) -> None:
        for key, value in d.items():
            print(f"{key} : {value}, ")


    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # make dict
        intervals: dict[str, list[int]] = self.createDictOfIntervals(s)

        # minimum legal interval for each letter
        self.expandIntervals(s, intervals)

        self.printDict(intervals)


                



        



s = Solution()
s.maxNumOfSubstrings("adefaddaccc")
print()
s.maxNumOfSubstrings("abab")
print()
s.maxNumOfSubstrings("abbaccd")


        

        
# @lc code=end

