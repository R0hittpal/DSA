class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lst1=[]
        lst2=[]
        lst=[]
        n=len(nums)//2
        for i in nums:
            if i >=0:
                lst1.append(i)
            elif i<0:
                lst2.append(i)
        for i in range(n):
            lst.append(lst1[i])
            lst.append(lst2[i])
        return lst

        