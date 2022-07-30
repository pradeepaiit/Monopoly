import json
import array as arr
import numpy as np

Peter = 16
Billy = 16
Charlotte = 16
Sweedal = 16

Players = [Peter, Billy, Charlotte, Sweedal]

total = 0
game = True

x = open('board.json')
y = open('rolls_1.json')
z = open('rolls_2.json')

a = json.load(x)
b = json.load(y)
c = json.load(z)

# for i in range[49]:

arr1 =np.array('i',b)
arr2 =np.array('q',c)

total =np.add(arr1, arr2)

Peter_value = (total)
Billy_value = (arr1[1])
Charlotte_value = (arr1[2])
Sweedal_value = (arr1[3])

print("Peter's turn:", Peter_value)
print("Billy's turn:", Billy)
print("Charlotte's turn:", Charlotte)
print("Sweedal's turn:", Sweedal)
