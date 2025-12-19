#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
class Solution:
        
    def create_word_count(self, paragraph) -> dict[str, int]:
        """
        This function returns a dict which the key : value of it 
        is every unique word in paragraph : count of its appearence.

        Furthermore, the keys of the dict are lowercased
        """
        word_count: dict[str, int] = {}
        words: list[str] = paragraph.split()
        for word in words:
            # stip puntuations and to lower case
            word = word.strip("!?',;.").lower()

            # fill dict
            word_count[word] = word_count.get(word, 0) + 1
        
        return word_count
    

    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        word_count: dict[str, int] = self.create_word_count(paragraph)

        # searching the word which appears the most
        most_frequent_word: tuple[str, int] = ("Error, no word detected", -1)
        banned_words: set[str] = set(banned)
        for word in word_count:
            count = word_count[word]
            if (word not in banned_words) and (count > most_frequent_word[1]):
                most_frequent_word = (word, count)

        return most_frequent_word[0]
    

if __name__ == "__main__":
    s = Solution()
    assert s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]) == "ball"
    assert s.mostCommonWord("a.", []) == "a"


        
# @lc code=end

