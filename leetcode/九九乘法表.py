for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,i*j), end="  ")
    print("")

i = 1 
while i < 10:
    j = 1
    while j <= i:
        print('{}*{}={}'.format(j,i,i*j), end="  ")
        j += 1
    print("")
    i += 1

for i in range(1,10):
    j = 1
    while j <= i:
         print('{}*{}={}'.format(j,i,i*j), end="  ")
         j += 1
    print("")

i = 1
while i < 10:
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,i*j), end="  ")
    i += 1
    print("")
