#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
import re

class Solution:
    def extract_words(self, paragraph: str) -> list[str]:
        """
        This function returns a list containing every word in paragraph
        Furthermore, the words in list are lowercased
        """
        paragraph = paragraph.lower()
        word_pattern = re.compile(r"[a-z]+")
        return word_pattern.findall(paragraph)
    

    def create_word_count(self, paragraph: str) -> dict[str, int]:
        """
        This function returns a dict displaying each word appearing in the paragraph 
        and its occurrence count, with the format "word:count"
        Furthermore, the words are lowercased
        """
        words: list[str] = self.extract_words(paragraph)
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        return word_count


    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """
        This function returns the word that occures the most in the paragraph
        that is not banned.

        Parameter
        ---
        paragraph: str
        banned: list[str]

        Return
        ---
        max_word: str
        """
        word_count: dict[str, int] = self.create_word_count(paragraph)

        max_word, max_count = "Error, word not found", -1
        banned_words: set[str] = set(banned)
        for word in word_count:
            count = word_count[word]
            if (word not in banned_words) and count > max_count:
                max_word, max_count = word, count
        
        return max_word



if __name__ == "__main__":
    s = Solution()
    assert(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])) == "ball"
    assert(s.mostCommonWord("a.", [])) == "a"


        
# @lc code=end

