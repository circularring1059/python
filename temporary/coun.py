from collections import Counter

array = [1, 1, 2, 6]

coun = Counter(array)

if 1 in coun:
    print(coun.get(1))