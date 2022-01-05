def can(gas, cost):
    def location_gas(n):
        if n == 0:
            return gas[i]
        if n + i == len(gas):
            return location_gas(n - 1) + gas[n + i - len(gas)] - cost[n + i - 1]

        if n >= len(gas):
            return location_gas(n - 1) + gas[n + i - len(gas)] - cost[n + i - 1 - len(gas)]

        return location_gas(n - 1) + gas[n + i] - cost[n + i - 1]

    for i in range(len(gas)):
        for n in range(len(gas)+1):
            if location_gas(n) < 0:
                return False
        return True

print(can([1,2,5],[3,6,2]))
