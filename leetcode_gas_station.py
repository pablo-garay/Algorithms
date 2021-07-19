class Solution(object):  # O(n) solution. Optimal as need to traverse each elem of array in worst case
    def canCompleteCircuit(self, gas, cost):
        gas = [gas[i] - cost[i] for i in xrange(len(gas))]

        if sum(gas) < 0:
            return -1

        start = 0
        tank = 0

        for i in xrange(len(gas)):
            tank += gas[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start


print Solution().canCompleteCircuit(gas=[1,2,3,4,5], cost=[3,4,5,1,2])
print Solution().canCompleteCircuit(gas=[2,3,4], cost=[3,4,3])
print Solution().canCompleteCircuit(gas=[0], cost=[0])
print Solution().canCompleteCircuit(gas=[0], cost=[1])
print Solution().canCompleteCircuit(gas=[1], cost=[1])
print Solution().canCompleteCircuit([5,8,2,8], [6,5,6,6])
print Solution().canCompleteCircuit([2], [2])
print Solution().canCompleteCircuit([0], [0])
