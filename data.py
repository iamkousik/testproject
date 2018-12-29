from collections import deque
import math
list = deque([2, 1, 2, 3, 89, 95, 12])
#list.append(list.index(89))
#list.remove(3)
#list.sort()
#list.reverse()
print(list)
print(list.popleft())
print(list)
squares = []
print(squares)
for x in range(10):
    squares.append(x**2)
print(squares)
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = [value for value in raw_data if not math.isnan(value)]
print(filtered_data)
string1, string2, string3 = '', 'Trondheim', 'HammerDance'
non_null = (string1 or(string2 or string3))
print(non_null)