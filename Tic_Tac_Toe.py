from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog

tk=Tk()
tk.title("********** TIC TAC TOE************")

play1=StringVar()
play2=StringVar()
p1=StringVar()
p2=StringVar()

#player1=Entry(tk, textvariable=p1,bd=4)
player1 = StringVar()
player1=simpledialog.askstring("Name of Player 1","Player 1:")
win1 = str(player1) + " Wins!!!"

#player2=Entry(tk, textvariable=p2,bd=4)
player2 = StringVar()
player2=simpledialog.askstring("Name of Player 2","Player 2:")
win2 = str(player2) + " Wins!!!"

condition=True
game=0



#play1=player1  + "\n WINS !!!!!!!!!"



    
def clicks(button):
    global play1,play2,p1,p2,condition,game
    if   button["text"]==" " and condition==True:
        button["text"]= "X"
        condition=False
       # play1=p1.get()  + "\n WINS !!!!!!!!!"

        
        winlose()
        game+=1
            
        
        
    elif button["text"]==" " and condition==False:
        button["text"]="O"
        condition=True
        #play2=player2  + "\n WINS !!!!!!!!!"
        
        winlose()
        game+=1
    else:
        tkinter.messagebox.showwarning("CLICKED","SORRY!!!!!!!!! Button has already clicked")

def winlose():
    if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
        button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
        button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
        button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
        button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
        button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
        button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
        button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        tkinter.messagebox.showinfo('WINNER',win1)
        tk.destroy()
        
    elif   (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
            button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
            button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
            button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
            button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
            button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
            button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
            button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
            tkinter.messagebox.showinfo('WINNER',win2)
            tk.destroy()
    elif (game==8):
        tkinter.messagebox.showinfo("RESULTS","Both the players have played really well so its a TIE !!!!!!!!")
        tk.destroy()
        
p22 = StringVar()
p22.set(player2)

p11 = StringVar()
p11.set(player1)

def mainbody():
    global button
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global n1
    global n2
    
    button=StringVar()
    label=Label(tk, text="Player 1:", font='Times 18 bold', bg='white', fg='black', height=2, width=8)
    label.grid(row=1, column=0)

    n1=Label(tk, textvariable=p11, font='Times 18',fg='black', height=2, width=8)
    n1.grid(row=1, column=1)

    label=Label(tk, text="Player 2:", font='Times 18 bold', bg='white', fg='black', height=2, width=8)
    label.grid(row=2, column=0)

    n2=Label(tk, textvariable=p22, font='Times 18', fg='black', height=2, width=8)
    n2.grid(row=2, column=1)

    button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda:clicks(button1))                                                                                                                          
    button1.grid(row=3, column=0)

    button2 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda:clicks(button2))
    button2.grid(row=3, column=1)

    button3 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda:clicks(button3))
    button3.grid(row=3, column=2)

    button4 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda:clicks(button4))
    button4.grid(row=4, column=0)

    button5 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda:clicks(button5))
    button5.grid(row=4, column=1)

    button6 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda:clicks(button6))
    button6.grid(row=4, column=2)

    button7 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda:clicks(button7))
    button7.grid(row=5, column=0)

    button8 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda:clicks(button8))
    button8.grid(row=5, column=1)

    button9 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda:clicks(button9))
    button9.grid(row=5, column=2)

if len(player1) > 0 and len(player2) > 0:
    mainbody()
elif len(player1) == 0:
    tkinter.messagebox.showwarning('Error',"Player 1 name is empty")
   
elif len(player2) == 0:
    tkinter.messagebox.showwarning('Error',"Player 2 name is empty")
    
elif len(player2) ==0 and len(player1)==0:
    tkinter.messagebox.showwarning('Error',"Player 2 name is empty")
   
    
else:
    tkinter.messagebox.showwarning('Error',"You need to enter correct name!")
    
tk.mainloop()
