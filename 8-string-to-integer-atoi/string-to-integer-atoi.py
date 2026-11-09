class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        sign=1
        n=len(s)
        nums=0

        Int_max=(2**31)-1
        Int_min=(-2**31)
        while i <n and s[i]==" ":
            i+=1
        if i <n and s[i]=="-":
            sign=-1
            i+=1
        elif i <n and s[i]=="+":
            i+=1
        while i<n and s[i].isdigit():
            digit=int(s[i])
            nums=nums*10+digit

            if sign*nums < Int_min:
                return Int_min
            elif sign*nums > Int_max:
                return Int_max
            i+=1
        return sign*nums
        


      