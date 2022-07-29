import json
import array as arr

Peter = 16
Billy = 16
Charlotte = 16
Sweedal = 16

x = open('board.json')
y = open('rolls_1.json')
z = open('rolls_2.json')

a = json.load(x)
b = json.load(y)
c = json.load(z)


num = 0
count = 0
num_of_plyrs = 4
stop = False

arr1 =arr.array('l',b)
arr2 =arr.array('q',c)

Peter = (arr1[0],arr2[0])

print("Peter's turn:", Peter)

while not stop:
    if count == 4:
        stop == True