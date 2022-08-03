import json
import array as arr
# from multiprocessing.sharedctypes import Value
# from operator import index
# from unicodedata import name

# from numpy import double, tile

#DEFINING VARIABLES

round_number = 0
players_list = ["Peter", "Billy", "Charlotte", "Sweedal"]
score_list=[16,16,16,16]

# total = 0
# game = True
# totalDoubles = 0



#TAKING VALUES FROM JSON

x = open('board.json')
y = open('rolls_1.json')
z = open('rolls_2.json')

a = json.load(x)
b = json.load(y)
c = json.load(z)

arr1 =arr.array('i',b)
arr2 =arr.array('f',c)



# for i in arr1[slice(None,None,4)]:
#  print("Peter's dice 1:", i)



# for f in arr2[slice(None,None,4)]:
#  print("Peter's dice 2:", f)

#  total = i + f

#MAKING LOOP BETWEEN 4 PLAYERS
while True:
    round_number += 1
print("Round:", round_number)
if round_number%4:
    total = i + f
    print(players_list[0], "Turn" , total)
   
else:
    print(players_list[1], "Turn")



# Peter_value = (total)
# Billy_value = (arr1[1])
# Charlotte_value = (arr1[2])
# Sweedal_value = (arr1[3])

# print("Peter's roll", total)

