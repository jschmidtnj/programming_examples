'''
Created on Jun 15, 2016

@author: 174500
'''
from tkinter import *
from tkinter import messagebox
import random
import time
from tkinter import ttk
import random as r
import itertools as i
import turtle

if __name__ == "__main__":
    class App:
        def __init__(self,master):
            frame = Frame(master)
            frame.pack()
            def color2():
                r = "red"
                g = "green"
                b = "blue"
                y = "yellow"
                o = "orange"
                p = "purple"
                v = "violet"
                i = "indigo"
                colorRand = random.randrange(1,8)
                if colorRand == 1:
                    color = r
                elif colorRand == 2:
                    color = g
                elif colorRand == 3:
                    color = b
                elif colorRand == 4:
                    color = y
                elif colorRand == 5:
                    color = o
                elif colorRand == 6:
                    color = p
                elif colorRand == 7:
                    color = v
                elif colorRand == 8:
                    color = i
                return color
            def b1(self):
                tk = Tk()
                tk.title("Game")
                tk.resizable(0, 0)
                tk.wm_attributes("-topmost", 1)
                canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
                canvas.pack()
                tk.update()
                
                class Ball:
                    def __init__(self, canvas, paddle, color):
                        self.canvas = canvas
                        self.paddle = paddle
                        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
                        self.canvas.move(self.id, 245, 100)
                        starts = [-3, -2, -1, 1, 2, 3]
                        random.shuffle(starts)
                        self.x = starts[0]
                        self.y = -3
                        self.canvas_height = self.canvas.winfo_height()
                        self.canvas_width = self.canvas.winfo_width()
                        self.hit_bottom = False
                
                    def draw(self):
                        self.canvas.move(self.id, self.x, self.y)
                        pos = self.canvas.coords(self.id)
                        if pos[1] <= 0:
                            self.y = 3
                        if self.hit_paddle(pos) == True:
                            self.y = -3
                        if pos[3] >= self.canvas_height:
                            self.hit_bottom = True
                            result=messagebox.askquestion("Continue", "Would you like to play again?")
                            if result == 'yes':
                                self.id = canvas.create_oval(10, 10, 25, 25, fill=color2())
                                self.canvas.move(self.id, 245, 100)
                                starts = [-3, -2, -1, 1, 2, 3]
                                random.shuffle(starts)
                                self.x = starts[0]
                                self.y = -3
                                self.canvas_height = self.canvas.winfo_height()
                                self.canvas_width = self.canvas.winfo_width()
                                self.hit_bottom = False
                            else:
                                exit
                                tk.destroy()
                        if pos[0] <= 0:
                            self.x = 3
                        if pos[2] >= self.canvas_width:
                            self.x = -3
                
                    def hit_paddle(self, pos):
                        paddle_pos = self.canvas.coords(self.paddle.id)
                        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                                return True
                        return False
                
                class Paddle:
                    def __init__(self, canvas, color):
                        self.canvas = canvas
                        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
                        self.canvas.move(self.id, 200, 300)
                        self.x = 0
                        self.canvas_width = self.canvas.winfo_width()
                        self.canvas.bind_all('<Left>', self.turn_left)
                        self.canvas.bind_all('<Right>', self.turn_right)
                
                    def turn_left(self, evt):
                        self.x = -2
                
                    def turn_right(self, evt):
                        self.x = 2
                
                    def draw(self):
                        self.canvas.move(self.id, self.x, 0)
                        pos = self.canvas.coords(self.id)
                        if pos[0] <= 0:
                            self.x = 0
                        elif pos[2] >= self.canvas_width:
                            self.x = 0
                
                paddle = Paddle(canvas, color2())
                ball = Ball(canvas, paddle, color2())
                
                def update_game():
                    if ball.hit_bottom == False:
                        ball.draw()
                        paddle.draw()
                    tk.update_idletasks()
                    tk.after(10, update_game)
                
                tk.after(10, update_game)
                tk.mainloop() 
            
            """    
            def b2(self):
                def calculate():
                    try:
                        value = float(feet.get())
                        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
                    except ValueError:
                        pass
                    
                root = Tk()
                root.title("Feet to Meters")
                
                mainframe = ttk.Frame(root, padding="3 3 12 12")
                mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
                mainframe.columnconfigure(0, weight=1)
                mainframe.rowconfigure(0, weight=1)
                
                feet = StringVar()
                meters = StringVar()
                
                feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
                feet_entry.grid(column=2, row=1, sticky=(W, E))
                
                ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
                ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
                
                ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
                ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
                ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
                
                for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
                
                feet_entry.focus()
                root.bind('<Return>', calculate)
                
                root.mainloop()
            """    
            """
            def b3(self):
                tk = Tk()
                canvas = Canvas(tk, width = 1000, height = 1000)
                canvas.pack()
                def move(event):
                    if event.keysym == 'Up':
                        global y
                        global y1
                        y-=10
                        y1-=10
                    elif event.keysym == 'Down':      
                        y+=10
                        y1+=10
                    elif event.keysym == 'Right':
                        global x
                        global x1
                        x+=10
                        x1+=10
                    elif event.keysym == 'Left':
                        x-=10
                        x1-=10
                
                
                background = canvas.create_rectangle(0, 0, 1000, 1000, fill = color2()) #draws background
                ranNum=random.random()*960  #Creates a random number
                ranNum1=random.random()*960 #Creates a random number
                r1 = None
                o = 0
                length = 4
                x = 500
                y = 500
                x1 = 515
                y1 = 515
                while o < length:          
                    r=canvas.create_rectangle(x, y, x1, y1, fill = color2())
                    tk.bind('<KeyPress-Up>', move )
                    tk.bind('<KeyPress-Down>', move)
                    tk.bind('<KeyPress-Left>', move)
                    tk.bind('<KeyPress-Right>', move)
                    time.sleep(.01)
                    canvas.delete(r1)
                    r1 = r
                    tk.update()
                    tk.update_idletasks()
                
                tk.mainloop()
                
            """    
            def b4(self):
                class Hangman():
                    def initial(self):
                        print ("Welcome to Hangman. Are you ready to begin?")
                        print ("(1)Yes!\n(2)No")
                        user = input("")
                        
                        if user == '1': self.start()
                        elif user == '2':
                            print ("Okay. See you some other time.")
                            exit()
                        else:
                            print ("Please input 1 or 2. You only have two choices. It is not hard.")
                            self.initial()
                            
                    def hangman(self, guesses, the_word):
                        if guesses == 0:
                            print ("________      ")
                            print ("|      |      ")
                            print ("|             ")
                            print ("|             ")
                            print ("|             ")
                            print ("|             ")
                        elif guesses == 1:
                            print ("________      ")
                            print ("|      |      ")
                            print ("|      0      ")
                            print ("|             ")
                            print ("|             ")
                            print ("|             ")
                        elif guesses == 2:
                            print ("________      ")
                            print ("|      |      ")
                            print ("|      0      ")
                            print ("|     /       ")
                            print ("|             ")
                            print ("|             ")
                        elif guesses == 3:
                            print ("________      ")
                            print ("|      |      ")
                            print ("|      0      ")
                            print ("|     /|      ")
                            print ("|             ")
                            print ("|             ")
                        elif guesses == 4:
                            print ("________      ")
                            print ("|      |      ")
                            print ("|      0      ")
                            print ("|     /|\     ")
                            print ("|             ")
                            print ("|             ")
                        elif guesses == 5:
                            print ("________      ")
                            print ("|      |      ")
                            print ("|      0      ")
                            print ("|     /|\     ")
                            print ("|     /       ")
                            print ("|             ")
                        else:
                            print ("________      ")
                            print ("|      |      ")
                            print ("|      0      ")
                            print ("|     /|\     ")
                            print ("|     / \     ")
                            print ("|             ")
                            print ("The noose tightens around your neck, and you begin to black out.")
                            print ("GAME OVER!")
                            print("The correct answer was " + the_word)
                            self.__init__()
                
                    def start(self):
                        print ("Get Ready to Die")
                        self.game()
                
                    def game(self):
                        guesses = 0
                        letters_used = ""
                        the_word = "hello world"
                        #also add the number of characters below:
                        progress = ["*"]*len(the_word)
                        z=0
                        while guesses < 6:
                            guess = input("Guess a letter ->")
                            if guess in the_word and guess not in letters_used and len(guess)==1:
                                print ("Your guess was right!")
                                letters_used += "," + guess
                                self.hangman(guesses, the_word)
                                print ("Progress: " + self.update(guess, the_word, progress))
                                print ("Letter used: " + letters_used)
                                for x in range(0,len(the_word)):
                                    if the_word[x] == progress[x]:
                                        z+=1
                                if z>len(the_word)+10:
                                    print ("Your guess was right!")
                                    print("You survived for now...")
                                    sys.exit()
                            elif guess not in the_word and guess not in letters_used and len(guess)==1:
                                guesses += 1
                                print ("Incorrect Guess!") 
                                letters_used += "," + guess
                                self.hangman(guesses, the_word)
                                print ("Progress: " + "".join(progress))
                                print ("Letter used: " + letters_used)
                            else:
                                print ("That's the wrong letter! Try again")
                                
                
                    def update(self, guess, the_word, progress):
                        i = 0
                        while i < len(the_word):
                            if guess == the_word[i]:
                                progress[i] = guess
                                i += 1
                            else:
                                i += 1
                
                        return "".join(progress)
                
                Hangman().initial()
                
                
            def b5(self):
                def randDice():
                    print ("*****************************\n\nThis is a dice simulation. It will output a random " + 
                    "integer between 1 and 6.\n\n")
                    num = random.randrange(1,6)
                    print("The die rolled a ", num) 
                    cont = input("\n\nWould you like to continue? ") #in python3, raw_input( is now input()
                    if "yes" in cont:
                        randDice()
                    else:
                        exit()
                randDice()
                
                
            def b6(self):
                suit = 'SCDH'
                rank = '23456789TJQKA'
                deck = tuple(''.join(card) for card in i.product(rank, suit))
                val = ()
                for _ in range(9):
                    val = val + (_+2, _+2, _+2, _+2)
                    if _ == 8:
                        for __ in range(3):
                            val = val + (10, 10, 10, 10)
                val = val + (1, 1, 1, 1)
                deckval = dict(zip(deck, val))
                
                
                def deal():
                    global hand, dealer_hand, player_hand, counter
                    hand = r.sample(deck, 52)
                    counter = 0
                    dealer_hand = list(hand[counter:counter + 1])
                    counter += 2
                    player_hand = list(hand[counter:counter + 2])
                    counter += 2
                
                def run():
                    play = input('********************\nWould you like to play again?').lower()
                    
                    print (play)
                    if "no" in play:
                        exit()
                    elif "yes" in play:
                        deal()
                        main()
                        print("\n\n********************\nWELCOME TO BLACKJACK!!!")
                    else:
                        print('Please enter yes or no')
                        run()
                
                def sum_player_hand():
                    global hand, player_hand, counter, player_sum, opt_player_sum
                    player_sum = 0
                    opt_player_sum = 0
                    for a in range(len(player_hand)):
                        if int(deckval[player_hand[a]]) == 1 and opt_player_sum + int(deckval[player_hand[a]]) <= 21:
                            opt_player_sum = player_sum + int(deckval[player_hand[a]]) + 10
                            player_sum += int(deckval[player_hand[a]])
                        elif opt_player_sum > 21:
                            player_sum += int(deckval[player_hand[a]])
                            opt_player_sum = player_sum
                        else:
                            player_sum += int(deckval[player_hand[a]])
                            opt_player_sum += int(deckval[player_hand[a]])
                
                
                def dealer_init():
                    global hand, dealer_hand, counter, dealer_sum, opt_dealer_sum
                    dealer_sum = 0
                    opt_dealer_sum = 0
                    if int(deckval[dealer_hand[0]]) == 1:
                        dealer_sum += int(deckval[dealer_hand[0]])
                        opt_dealer_sum += dealer_sum + 10
                    else:
                        dealer_sum = int(deckval[dealer_hand[0]])
                        opt_dealer_sum = int(deckval[dealer_hand[0]])
                    dealer_logic()
                
                
                def dealer_logic():
                    global hand, dealer_hand, counter, dealer_sum, opt_dealer_sum
                    if dealer_sum >= 17 or opt_dealer_sum >= 17:
                        pass
                    else:
                        while opt_dealer_sum <= 16:
                            dealer_sum = 0
                            opt_dealer_sum = 0
                            dealer_hand = dealer_hand + list(hand[counter:counter + 1])
                            counter += 1
                            for _ in range(len(dealer_hand)):
                                if int(deckval[dealer_hand[_]]) == 1 and (opt_dealer_sum + int(deckval[dealer_hand[_]])) <= 21:
                                    opt_dealer_sum += int(deckval[dealer_hand[_]])
                                    dealer_sum += int(deckval[dealer_hand[_]])
                                else:
                                    dealer_sum += int(deckval[dealer_hand[_]])
                                    opt_dealer_sum += int(deckval[dealer_hand[_]])
                
                def initial():
                    print("\n\n********************\nWELCOME TO BLACKJACK!!!")
                    
                def main():
                    global hand, dealer_hand, player_hand, counter, player_sum,     dealer_sum, opt_player_sum, opt_dealer_sum
                    sum_player_hand()
                    print('\nDealer has:', dealer_hand[0:2], '--')
                    if player_sum <= 21:
                        if opt_player_sum == player_sum or opt_player_sum > 21:
                            print('Your hand is:', player_hand, '\nYour sum is:', player_sum)
                        else:
                            print('Your hand is:', player_hand, '\n', 'Your sum is:', player_sum, 'or', opt_player_sum)
                        choice = input('Hit or stay? ').lower()
                        if choice == 'hit':
                            player_hand = player_hand + list(hand[counter:counter + 1])
                            counter += 1
                            main()
                        elif choice == 'stay':
                            print('')
                            if opt_player_sum <= 21:
                                print('Final Hand: ', player_hand, 'Final Sum:', opt_player_sum)
                                dealer_init()
                                if opt_dealer_sum <= 21:
                                    print('Dealer has:', dealer_hand, 'Sum:', opt_dealer_sum)
                                    if 21 >= opt_dealer_sum > opt_player_sum:
                                        print('DEALER WINS')
                                    else:
                                        print('YOU WIN')
                                    run()
                                else:
                                    print('Dealer has:', dealer_hand, 'Sum:', dealer_sum)
                                    if 21 >= dealer_sum > opt_player_sum:
                                        print('DEALER WINS')
                                    else:
                                        print('YOU WIN')
                                    run()
                            else:
                                print('Final Hand: ', player_hand, '\n', 'Final Sum:', player_sum)
                                dealer_init()
                                if opt_dealer_sum <= 21:
                                    print('Dealer has:', dealer_hand, 'Sum:', opt_dealer_sum)
                                    if 21 >= opt_dealer_sum > player_sum:
                                        print('DEALER WINS')
                                    else:
                                        print('YOU WIN')
                                    run()
                                else:
                                    print('Dealer has:', dealer_hand, 'Sum:', dealer_sum)
                                    if 21 >= dealer_sum > player_sum:
                                        print('DEALER WINS')
                                    else:
                                        print('YOU WIN')
                                    run()
                        else:
                            print('BUST\nYOUR HAND WAS:', player_hand, '\nYOUR SUM WAS:', player_sum, '\n')
                        dealer_init()
                        if opt_dealer_sum < 21:
                            print('Dealer has:', dealer_hand, 'Sum:', opt_dealer_sum)
                            if dealer_sum > 21:
                                print('DEALER BUSTS')
                            run()
                        else:
                            print('Dealer has:', dealer_hand, 'Sum:', dealer_sum)
                            if dealer_sum > 21:
                                print('DEALER BUSTS')
                            run()
                
                initial()
                deal()
                main()
                run()
                
                
            def b7(self):
                def graphics():
                    print(1)
                    global canvas
                    window = Tk()
                    canvas = Canvas(window, width=800, height=600)
                    canvas.pack()
                    
                def hello():
                    bob = turtle.Turtle()
                    bob.forward(50)
                    turtle.done() 
                def color():
                    painter = turtle.Turtle()
                    """    These are all different methods that I can run:
                    painter.pencolor("blue")
                    for i in range(70):
                        painter.forward(60)
                        painter.left(143)
                    painter.pencolor("red")
                    for i in range(44):
                        painter.forward(130)
                        painter.left(88)
                    painter.pencolor("blue")
                    for i in range(33):
                        painter.forward(28)
                        painter.left(66)
                    painter.pencolor("orange")
                    for i in range(28):
                        painter.forward(72)
                        painter.left(39)
                    painter.pencolor("green")
                    for i in range(19):
                        painter.forward(64)
                        painter.left(71)
                    painter.pencolor("purple")
                    for i in range(34):
                        painter.forward(54)
                        painter.left(92)
                    painter.pencolor("yellow")
                    for i in range(66):
                        painter.forward(103)
                        painter.left(97)
                    painter.pencolor("red")
                    for i in range(101):
                        painter.forward(21)
                        painter.left(10) 
                    """
                    
                    for i in range(60):
                        num = random.randrange(1,50)
                        num1 = random.randrange(1,30)
                        num2 = random.randrange(1,100)
                        
                        painter.pencolor(color2())
                        for i in range(num):
                            painter.forward(num1)
                            painter.left(num2)
                    turtle.done()
                color()
                hello()
                graphics()
            
            #lamda: is used so that the function does not execute to find the value for command. Instead, it runs so that b1 is the function that it runs.!!!
            self.button1=Button(frame,text="Pong", fg=color2(), command=lambda:b1(self))
            #self.button2=Button(frame,text="Feet to Meters", fg=color2(), command=lambda:b2(self))
            #self.button3=Button(frame,text="Moving Box", fg=color2(), command=lambda:b3(self))
            self.button4=Button(frame,text="Hangman", fg=color2(), command=lambda:b4(self))
            self.button5=Button(frame,text="Dice", fg=color2(), command=lambda:b5(self))
            self.button6=Button(frame,text="Blackjack", fg=color2(), command=lambda:b6(self))
            self.button7=Button(frame,text="Turtle Graphics", fg=color2(), command=lambda:b7(self))
            self.button1.pack(side=LEFT)
            #self.button2.pack(side=LEFT)
            #self.button3.pack(side=LEFT)
            self.button4.pack(side=LEFT)
            self.button5.pack(side=LEFT)
            self.button6.pack(side=LEFT)
            self.button7.pack(side=LEFT)
            
            
    root=Tk()
    app=App(root)
    root.mainloop()
