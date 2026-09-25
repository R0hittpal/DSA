class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        
        element1=None
        count1=0
        element2=None
        count2=0
        n=len(nums)

        # if all(x == 0 for x in nums):
        #     return [0]


        for i in range(n):
            if count1==0 and nums[i]!=element2:
                element1 =nums[i]
                count1=1
            elif count2==0 and nums[i]!=element1:
                element2 =nums[i]
                count2=1

            elif nums[i]==element1:
                count1+=1
            elif nums[i]==element2:
                count2+=1
            else:
                count1-=1
                count2-=1
        ans=[]           
        count3=0
        for i in range(n):
            if nums[i]==element1:
                count3+=1
        if count3>(n//3):
            ans.append(element1)

        count4=0
        for i in range(n):
            if nums[i]==element2:
                count4+=1
        if count4>(n//3):
            ans.append(element2)
        return ans

    
        
            

        