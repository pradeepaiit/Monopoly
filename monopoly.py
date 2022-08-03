# import json
# import array as arr


# #DEFINING VARIABLES

# round_number = 0
# players_list = ["Peter", "Billy", "Charlotte", "Sweedal"]
# score_list=[16,16,16,16]


# #TAKING VALUES FROM JSON

# x = open('board.json')
# y = open('rolls_1.json')
# z = open('rolls_2.json')

# a = json.load(x)
# b = json.load(y)
# c = json.load(z)

# arr1 =arr.array('i',b)
# arr2 =arr.array('f',c)




# #MAKING LOOP BETWEEN 4 PLAYERS
# while True:
#     round_number += 1
# print("Round:", round_number)
# if round_number%4:
#     total = i + f
#     print(players_list[0], "Turn" , total)
   
# else:
#     print(players_list[1], "Turn")

from tkinter import *

root = Tk()

root.geometry('400x400')

root.resizable(False,False)

#DEFINING VARIABLES
namelist=[]
number = 0 

def submit(numberofplayers):
    global namelist
    global number
    if name.get()!='':
       namelist.append(name.get())
       number = number+1
    
    if(number==int(numberofplayers)):
        root.destroy()
        gamescreen(namelist)
        
    def gamescreen(namelist):
        screen=Tk()
        screen.geometry('400x400')
        screen.resizable(False,False)
        
        titlelabel=Label(screen, text = "MONOPOLY BANK", font="bold, 20")
        titlelabel.place(x=110,y=14)
        
        placey=80
        initial_money=16
        money=[]
        for i in namelist:
             money.append(initial_money)
             
        for j in namelist:
            namedroplabels=Label(screen,text=j, font="bold, 20")
            namedroplabels.place(x=20, y=placey)
            
            moneydroplabel=Label(screen,text="initial_money", font="bold, 16")
            moneydroplabel.place(x=20,y=placey)
             
            placey=placey+80
    
            namedropdownlabel=Label(screen,text="Select Player", font="bold, 11")
            namedropdownlabel.place(x=20, y=425)
            
            selectedname=StringVar()
            selectedname.set("Player name")
            drop=OptionMenu(screen,selectedname, *namelist)
            drop.place(x=160,y=420)
            
            buyorselllabel=Label(screen,text="Select Option", font="bold, 11")
            buyorselllabel.place(x=20,y=450)
            
            buyorsell=StringVar()
            buyorsell.set("Select Option")
            drop=OptionMenu(screen,buyorsell,*buyorsell)
            
            amountlabel=Label(screen,text="Select Amount", font="bold, 11")
            amountlabel.place(x=20, y=480)
            
            amount=Entry(screen,borderwidth=5, highlightthickness=0)       
            amount.place(x=160, y=490, width=110, height=25)     
            
            button=Button(screen,text="submit", command=lambda:score(screen,namelist,money,initial_money,selectedname.get(), buyorsell.get(), amount.get()),border=1)
            button.place(x=150, y=520)
            
            screen.mainloop()
            
            
    titlelabel=Label(root, text = "MONOPOLY BANK", font="bold, 20")
    titlelabel.place(x=110,y=14)

    numberofplayerslabel = Label(root, text ="No. of Players", font="bold, 16")
    numberofplayerslabel.place(x=20,y=80)

    numberofplayers=Entry(root, borderwidth=5)
    numberofplayers.place(x=200,y=80,width=185,height=33)

    namelabel=Label(root, text="Enter the Player name", font="bold, 16")
    namelabel.place(x=80,y=120)

    name=Entry(root,borderwidth=5)
    name.place(x=200,y=120, width=185,height=33)

    button=Button(root,text="Submit", command=lambda:submit(numberofplayers.get()),border=1,height=2,width=20)
    button.place(x=150,y=160)

    root.mainloop()