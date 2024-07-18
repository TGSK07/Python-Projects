from tkinter import *

ttt = Tk()
ttt.title('Tic Tac Toe')
ttt.geometry('400x600')
ttt.resizable(0,0)
photo = PhotoImage(file = r"D:\Learning\Python\tic-tac-toe_39.png")
ttt.iconphoto(True, photo)
player1,player2,computer = 'X','O','O'
turn = player1
board = {2:' ',5:' ',8:' ',
         3:' ',6:' ',9:' ',
         4:' ',7:' ',0:' '}

def home():
    f0 = Frame(ttt,bg='#192A32')
    f0.place(x=0,y=0,width=400,height=600)
    play_button = Button(f0,text='Play',fg='#1F3540',bg='#31C4BE',font=('IMPACT',25),command=Play)
    play_button.place(x=150,y=180,width=120,height=60)
    exit_button = Button(f0,text='Exit',fg='#1F3540',bg='#31C4BE',font=('IMPACT',25),command=ttt.quit)
    exit_button.place(x=150,y=260,width=120,height=60)


def insert(pos,player):
    global board
    board[pos] = player

def is_com():
    global board
    for i in board.keys():
        if board[i] not in ['X','O']:
            return 1
        
def is_winner():
    global board
    con = is_com()
    # -------- Return 1st element -----------
    if (board[2]==board[5]==board[8]) or (board[2]==board[3]==board[4]) or (board[2]==board[6]==board[0]):
            return board[2]
    
    #-------- Return 5th element -----------
    elif (board[3]==board[6]==board[9]) or (board[5]==board[6]==board[7]):
            return board[6]
    
    #-------- Return 3rd element -----------
    elif (board[8]==board[9]==board[0]) or (board[8]==board[6]==board[4]):
            return board[8]
    
    # -------- Return 7th element -----------
    elif (board[4]==board[7]==board[0]) :
            return board[4]
    else:
        if con != 1:
             
             return 'draw'
        else:
             return 0
    
def smart_com():
    max_player = computer
    min_player = player1
    
def Game(event):
    global turn,board
    button = event.widget
    butto=str(button)
    pos = int(butto[-1])
    insert(pos,turn)
    
    if turn==player1 and button["text"]==" ":
        button["fg"] = "#31C4BE"
        button['text'] = 'X'
        turn=player2

    else:
        if button["text"]==" ":
            button["fg"] = "#F0B237"
            button['text']='O'
            turn = player1
    con = is_com()
    if con == 1:
        winner=is_winner()
        if winner in ['X','O']:
            accouncement()
            
   
    
def Play():
    global board
    for i in board.keys():
         board[i]=' '
    f1 = Frame(ttt,bg='#192A32')
    f1.place(x=0,y=0,width=400,height=600)

    name = Label(f1,text='MULTIPLAYER MODE',fg='#F0B237',bg='#192A32',font=('Impact',32))
    name.place(x=38,y=40)

    back = Button(f1,text='<',fg='#1F3540',bg='#A8BEC9',font=('impact',15),command=home)
    back.place(x=2,y=2,width=20,height=20)
    
    b1 = Button(f1,text=' ',font=('Berlin Sans FB Demi',40),fg="#F0B237",bg='#1F3540',activebackground="#1F3540",activeforeground="#1F3540",borderwidth=0)
    b1.place(x=20,y=150,width=120,height=120)
    b1.bind('<Button-1>',Game)

    b2 = Button(f1,text=' ',font=('Berlin Sans FB Demi',40),fg="#F0B237",bg='#1F3540',activebackground="#1F3540",activeforeground="#1F3540",borderwidth=0)
    b2.place(x=20,y=272,width=120,height=120)
    b2.bind('<Button-1>',Game)

    b3 = Button(f1,text=' ',font=('Berlin Sans FB Demi',40),fg="#F0B237",bg='#1F3540',activebackground="#1F3540",activeforeground="#1F3540",borderwidth=0)
    b3.place(x=20,y=394,width=120,height=120)
    b3.bind('<Button-1>',Game)

    b4 = Button(f1,text=' ',font=('Berlin Sans FB Demi',40),fg="#F0B237",bg='#1F3540',activebackground="#1F3540",activeforeground="#1F3540",borderwidth=0)
    b4.place(x=142,y=150,width=120,height=120)
    b4.bind('<Button-1>',Game)

    b5 = Button(f1,text=' ',font=('Berlin Sans FB Demi',40),fg="#F0B237",bg='#1F3540',activebackground="#1F3540",activeforeground="#1F3540",borderwidth=0)
    b5.place(x=142,y=272,width=120,height=120)
    b5.bind('<Button-1>',Game)

    b6 = Button(f1,text=' ',font=('Berlin Sans FB Demi',40),fg="#F0B237",bg='#1F3540',activebackground="#1F3540",activeforeground="#1F3540",borderwidth=0)
    b6.place(x=142,y=394,width=120,height=120)
    b6.bind('<Button-1>',Game)

    b7 = Button(f1,text=' ',font=('Berlin Sans FB Demi',40),fg="#F0B237",bg='#1F3540',activebackground="#1F3540",activeforeground="#1F3540",borderwidth=0)
    b7.place(x=264,y=150,width=120,height=120)
    b7.bind('<Button-1>',Game)

    b8 = Button(f1,text=' ',font=('Berlin Sans FB Demi',40),fg="#F0B237",bg='#1F3540',activebackground="#1F3540",activeforeground="#1F3540",borderwidth=0)
    b8.place(x=264,y=272,width=120,height=120)
    b8.bind('<Button-1>',Game)    

    b9 = Button(f1,text=' ',font=('Berlin Sans FB Demi',40),fg="#F0B237",bg='#1F3540',activebackground="#1F3540",activeforeground="#1F3540",borderwidth=0,cursor="hand2")
    b9.bind('<Button-1>',Game)
    b9.place(x=264,y=394,width=120,height=120)
    
    restart = Button(f1,text='Restart',font=('Impact',30),fg='#192A32',bg='#A8BEC9',command=Play)
    restart.place(x=130,y=530,width=160,height=56)

def accouncement():
     global turn
     turn = player1
     f3 = Frame(ttt,bg='#192A32')
     f3.place(x=0,y=0,width=400,height=600)

     back = Button(f3,text='<',fg='#1F3540',bg='#A8BEC9',font=('impact',15),command=home)
     back.place(x=2,y=2,width=20,height=20)
     con = is_com()
     winner = ''
     if con == 1:
        winner = is_winner()
        notice = Label(f3,text=f"{winner} WIN",font=('IMPACT',50),fg='#F0B237',bg='#192A32',padx=10)
        notice.place(x=120,y=110)
     restart = Button(f3,text='Restart',font=('Impact',40),fg='#192A32',bg='#A8BEC9',command=Play)
     restart.place(x=115,y=300,width=190,height=55)

home()

ttt.mainloop()