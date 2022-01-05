def can(num1, num2):
    def location_gas(n):
        if n == 0:
            return num1[i]
        if n + i == len(num1):
            return location_gas(n - 1) + num1[n + i - len(num1)] - num2[n + i - 1]

        if n >= len(num1):
            return location_gas(n - 1) + num1[n + i - len(num1)] - num2[n + i - 1 - len(num1)]

        return location_gas(n - 1) + num1[n + i] - num2[n + i - 1]

    for i in range(len(num1)):
        for n in range(len(num1)+1):
            if location_gas(n) < 0:
                return False
        return True

print(can([1,2,5],[3,6,2]))
