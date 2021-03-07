def choose_sort(arg):
    for i in range(len(arg)-1):
        middle = i
        for y in range(i+1,len(arg)):
            if arg[middle]  >  arg[y]:
                middle = y
        arg[i],arg[middle] = arg[middle],arg[i]
    return arg
