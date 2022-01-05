class Solution():
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost) or not len(gas):
            return

        l = len(gas)
        for i in range(l):
            if (i - 1 >= 0 and gas[i - 1] > cost[i - 1]):
                continue
            currentGas = gas[i]
            cnt = 1
            nextStation = i
            while (currentGas >= cost[nextStation]):
                if cnt == l:
                    return i
                cnt += 1
                costt = cost[nextStation]
                nextStation = (nextStation + 1) % l
                currentGas += gas[nextStation] - costt
        return -1



    def canCompleteCircuit(self,num1, num2):
        # i = 0
        # i = 1
        # gas1  =  num1[0]
        # gas2  = num1[0] +  num1[1] - num1[0]
        # gas3 = gas2 + num1[2] - num2[2]
        # gas4 =  gas3 + num1[3] - num2[3]
        # f(1) = num1[i]
        # f(n) =   f(n-i-1) + num1[n+i-1] - num2[n+i-1]


        # i = 1  从第二个开始
        i=1
        def test(n):
            if n==0:
                start = num1[i]
            return test(n-1) + num1[n+i-1] - num2[n+i-1]









can_compete_circuit_ins = Solution()
print(can_compete_circuit_ins.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
