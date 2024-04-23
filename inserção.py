def insertionSort(alist):
   for index in range(1,len(alist)):

     valor = alist[index]
     posição = index
     print(alist)

     while posição>0 and alist[posição-1]>valor:
         alist[posição]=alist[posição-1]
         posição = posição-1

     alist[posição]=valor

alist = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
insertionSort(alist)
print(alist)
