class Solution():

    def trap(self, array):

        if not array:
            return "invald input"
        s = 0
        x = 0
        for i in range(len(array)-1):
          if array[i] != 0:
              t = i
              for j in range(t, len(array)-1):
                  if array[j+1] >= array[j]:
                      s = s + array[j]
                  else:
                      for x in range(j+2, len(array)-1):
                          if array[x] > array[j]:
                              s = s+ array[j] * (x-j)
                          elif array[x] == array[j]:
                              s = s+ array[j] * (x-j)
                          else:
                              pass
                              # s = s+  max(array[x+1], len(array)-1]) * rfind(max(array[x+1], len(array)-1) )
              break
#
#

for i in range(10):
    if i == 3:
        i == 7

    print(i)



