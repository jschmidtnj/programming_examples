'''
Created on May 17, 2016

@author: 174500
'''
import sys
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
        the_word = "asdfasdf"
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