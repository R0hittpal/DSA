class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(base, exp):
            if exp == 0:
                return 1

            half = power(base, exp // 2)

            if exp % 2 == 0:
                return (half * half) % MOD
            else:
                return (half * half * base) % MOD

        return (power(5, (n+1)//2) * power(4, n//2)) % MOD