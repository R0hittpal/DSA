class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        start = sorted(x[0] for x in intervals)
        end = sorted(x[1] for x in intervals)

        count = 0
        maxi = 0
        j = 0

        for i in range(len(start)):
            if start[i] <= end[j]:
                count += 1
            else:
                count -= 1
                j += 1
                count += 1

            maxi = max(maxi, count)

        return maxi