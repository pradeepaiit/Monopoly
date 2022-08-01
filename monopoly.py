import json
import array as arr
from operator import index
from unicodedata import name

from numpy import double

Peter = 16
Billy = 16
Charlotte = 16
Sweedal = 16

Players = [Peter, Billy, Charlotte, Sweedal]

total = 0
game = True
# double = True
totalDoubles = 0

x = open('board.json')
y = open('rolls_1.json')
z = open('rolls_2.json')

a = json.load(x)
b = json.load(y)
c = json.load(z)

arr1 =arr.array('i',b)
arr2 =arr.array('f',c)

# initial = a[0]

# def getNext(x):
#     next_el = None

# for name, elem in enumerate(arr1):

#     if name + 4 < len(arr1) and name - 4 >= 0:
#         curr_el = elem - 4
#         next_el = arr1[name]
        
#         print("Billy's turn:", next_el)


for i in arr1[slice(None,None,4)]:
 print("Peter's dice 1:", i)

for f in arr2[slice(None,None,4)]:
 print("Peter's dice 2:", f)


total = i + f

Peter_value = (total)
Billy_value = (arr1[1])
Charlotte_value = (arr1[2])
Sweedal_value = (arr1[3])

print("Peter's roll", total)


# print("Peter's turn:", total, initial['name'])
# print("Billy's turn:", Billy)
# print("Charlotte's turn:", Charlotte)
# print("Sweedal's turn:", Sweedal)
