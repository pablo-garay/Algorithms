class Solution(object):  # The Sieve of Eratosthenes uses an extra O(n) memory and its runtime complexity is O(n log log n)
    def countPrimes(self, n):
        if n <= 2:
            return 0

        is_prime = [1 for _ in xrange(n)]
        is_prime[0] = is_prime[1] = 0

        i = 2
        while i * i < n:  # i < sqrt(n)
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = 0
                    j += i

            i += 1

        return sum(is_prime)


print Solution().countPrimes(10)
print Solution().countPrimes(0)
print Solution().countPrimes(1)
print Solution().countPrimes(2)
print Solution().countPrimes(3)
print Solution().countPrimes(11)
print Solution().countPrimes(12)
print Solution().countPrimes(13)
print Solution().countPrimes(14)
print Solution().countPrimes(15)
print Solution().countPrimes(16)
print Solution().countPrimes(17)
print Solution().countPrimes(18)
print Solution().countPrimes(1500000)
