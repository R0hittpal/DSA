class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        
    

        element1 = 0
        count1 = 0
        element2 = 0
        count2 = 0

        for num in nums:

            if count1 == 0 and num != element2:
                element1 = num
                count1 = 1

            elif count2 == 0 and num != element1:
                element2 = num
                count2 = 1

            elif num == element1:
                count1 += 1

            elif num == element2:
                count2 += 1

            else:
                count1 -= 1
                count2 -= 1

        # Verification
        count1 = 0
        count2 = 0

        for num in nums:
            if num == element1:
                count1 += 1
            elif num == element2:
                count2 += 1

        ans = []

        if count1 > len(nums) // 3:
            ans.append(element1)

        if count2 > len(nums) // 3:
            ans.append(element2)

        return ans