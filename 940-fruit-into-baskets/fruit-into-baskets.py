class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        left = 0
        max_len = 0
        hash = {}

        for i in range(n):
            hash[fruits[i]] = hash.get(fruits[i], 0) + 1

            while len(hash) > 2:
                hash[fruits[left]] -= 1

                if hash[fruits[left]] == 0:
                    del hash[fruits[left]]

                left += 1

            max_len = max(max_len, i - left + 1)

        return max_len