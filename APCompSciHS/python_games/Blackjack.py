'''
Created on May 31, 2016

@author: 174500
'''
import random as r
import itertools as i

if __name__ == "__main__":
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