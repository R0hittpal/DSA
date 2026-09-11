class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0

        for sentence in sentences:
            count = len(sentence.split())
            maxi = max(maxi, count)

        return maxi