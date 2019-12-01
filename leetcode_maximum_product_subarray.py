class Solution(object):  # complexity O(n). Optimal as we need to traverse all the n elems of list in the worst case
    global_max = None

    def find_max_prod(self, start, end):
        if self.memo[start][end] is None:
            a, b = self.find_max_prod(start + 1, end)
            elem = self.memo[start][start][0]
            max_elem = min_elem = elem

            for prod in (a * elem, b * elem):
                if prod > max_elem:
                    max_elem = prod
                    if max_elem > self.global_max:
                        self.global_max = max_elem

                if prod < min_elem:
                    min_elem = prod

            self.memo[start][end] = [max_elem, min_elem]

        return self.memo[start][end]

    def parseFirst(self, nums):
        array = []
        # get rid of trailing 1's
        first_one, prev = (True, None)

        for num in nums:
            if num == 1:
                if not first_one:
                    continue
                first_one = False
            prev = num

            array.append(num)
            if len(array) >= 3 and -1 == array[-1] == array[-2] == array[-3]:
                array[-3:] = [-1]

        return array

    def maxProduct(self, nums):
        array = self.parseFirst(nums)

        self.global_max = array[0]
        self.memo = [[None for _ in xrange(len(array))] for _ in xrange(len(array))]

        for i in xrange(len(array)):
            self.memo[i][i] = [array[i], array[i]]

            if array[i] > self.global_max:
                self.global_max = array[i]

        self.find_max_prod(0, len(array) - 1)

        return self.global_max


print Solution().maxProduct([2,3,-2,4])
print Solution().maxProduct([-2,0,-1])
print Solution().maxProduct([4, -2, 3, 2])
print Solution().maxProduct([-1])
print Solution().maxProduct([9])
print Solution().maxProduct([-2,0,5,6])
print Solution().maxProduct([2,0,5,6])
print Solution().maxProduct([0, -2, 10, 10, 10, 10, 10, -1])
print Solution().maxProduct([0, 1, 2, 1, 1, 1, 1])
print Solution().maxProduct([0, 1, 2, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1])