def selectionSort(alist):
   for slot in range(len(alist)-1,0,-1):
       posiçãoMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[posiçãoMax]:
               posiçãoMax = location
               print(alist)

       temp = alist[slot]
       alist[slot] = alist[posiçãoMax]
       alist[posiçãoMax] = temp


alist = [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
selectionSort(alist)
print(alist)
