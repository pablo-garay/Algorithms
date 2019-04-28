class Solution(object):
    def largestNumber(self, nums):
        arr = [str(num) for num in nums]

        max_len = 0
        for word in arr:
            if len(word) > max_len:
                max_len = len(word)

        dict = {}
        list_num = []
        for word in arr:
            key = word + word[0] * (max_len - len(word)) + word[-1]
            if key not in dict:
                dict[key] = []
            dict[key].append(word)
            list_num.append(key)

        list_num.sort(reverse=True)
        res = ""
        for n in list_num:
            res += dict[n].pop()

        if res[0] == '0':  # handle 0 case
            return '0'
        return res

print Solution().largestNumber([3,30,34,5,9])
print Solution().largestNumber([10,2])
print Solution().largestNumber([3, 30, 34, 343, 332])
print Solution().largestNumber([12, 121])
print Solution().largestNumber([0, 0])
