class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=[]
        left=0
        right=0
        while left<len(nums1) and right<len(nums2):
            if nums1[left]<nums2[right]:
                lst.append(nums1[left])
                left+=1
            else:
                lst.append(nums2[right])
                right+=1
        while left<len(nums1):
            lst.append(nums1[left])
            left+=1
        while right<len(nums2):
            lst.append(nums2[right])
            right+=1


        if len(lst)%2==0:
            return  (lst[len(lst)//2]+lst[(len(lst)//2)-1])/2
        else:
            return lst[len(lst)//2]

        