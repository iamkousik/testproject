
from numpy import *
#from array import *
#Sarr = array('i', [25, 23, 1, 69, 78])
#n = int(input("Enter number for search :"))
#k = 0
#for i in arr:
  #  if n == i:
 #       print(k)
  #      break
   # k += 1

#print(arr.index(n))
#ar = linspace(0, 10, 16)
#ar = arange(1, 15, 2)
#ar = logspace(1, 40, 5)
#ar = zeros(5)
#ar = ones(5, int)
#ar = array([

    #[2, 3, 5, 8, 7, 2],
   # [6, 9, 8, 4, 6, 1]
#])
#ar2 = ar.flatten()
#ar3 = ar2.reshape(2, 2, 3)
#print(ar3)
#m = matrix('1 2 3 ; 4 5 6 ; 9 7 0')
#print(diagonal(m))
#print(m.min())
#m1 = matrix('1 2 3 ; 0 5 6 ; 9 7 1')
#m2 = matrix('1 2 9 ; 4 8 6 ;3 7 0')
#m3 = m1 * m2
#print(m3)
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])