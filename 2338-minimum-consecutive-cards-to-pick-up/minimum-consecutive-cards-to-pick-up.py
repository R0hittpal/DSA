class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        seen = {}
        min_len = float('inf')

        for i in range(len(cards)):
            if cards[i] in seen:
                length = i - seen[cards[i]] + 1
                min_len = min(min_len, length)

            seen[cards[i]] = i

        return min_len if min_len != float('inf') else -1
        