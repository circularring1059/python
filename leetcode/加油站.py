class Solution():
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost) or not len(gas):
            return

        l = len(gas)
        for i in range(l):
            if (i-1 >= 0 and gas[i-1] > gas[i-1]):
                continue
            currentGas = gas[i]
            cnt = 1
            nextStation = i
            while (currentGas >= cost[nextStation]):
                if cnt == l:
                    return i
                cnt += 1
                costt = cost[nextStation]
                nextStation = (nextStation +1) % l
                currentGas += gas[nextStation] - costt
        return -1

can_compete_circuit_ins = Solution()
print(can_compete_circuit_ins.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))