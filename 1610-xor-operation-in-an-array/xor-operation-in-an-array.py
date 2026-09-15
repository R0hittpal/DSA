class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(n):
            a=start + 2 * i
            nums.append(a)
        x=0
        for i in nums:
            x=x^i
        return x

        