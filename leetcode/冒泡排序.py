def bubbling_sort(arg):
    for i in range(len(arg) - 1):
        for y in range(len(arg) - i - 1):
            if arg[y] > arg[y + 1]:
                arg[y], arg[y + 1] = arg[y + 1], arg[y]
    return arg