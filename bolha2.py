def shortBubbleSort(alist):
    troca = True
    passnum = len(alist)-1
    while passnum > 0 and troca:
       troca = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               troca = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
               print(alist)
       passnum = passnum-1


alist=[11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
shortBubbleSort(alist)
print(alist)
