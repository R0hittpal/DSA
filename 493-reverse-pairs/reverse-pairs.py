class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2

        count = 0
        count += self.merge_sort(nums, left, mid)
        count += self.merge_sort(nums, mid + 1, right)

        count += self.count_pairs(nums, left, mid, right)

        self.merge(nums, left, mid, right)

        return count

    def count_pairs(self, nums, left, mid, right):
        count = 0
        j = mid + 1

        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1

            count += j - (mid + 1)

        return count

    def merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= right:
            temp.append(nums[j])
            j += 1

        nums[left:right + 1] = temp