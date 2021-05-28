import random
import game
import ai

def create_deck():
    deck_dict = {"JanBright": 20, "JanRibbonRed": 5, "JanJunk1": 0, "JanJunk2": 0, 
    "FebAnimals": 10, "FebRibbonRed": 5, "FebJunk1": 0, "FebJunk2": 0, 
    "MarchBright": 20, "MarchRibbonRed": 5, "MarchJunk1": 0, "MarchJunk2": 0, 
    "AprilAnimals": 10, "AprilRibbonEmpty": 5, "AprilJunk1": 0, "AprilJunk2": 0, 
    "MayAnimals": 10, "MayRibbonEmpty": 5, "MayJunk1": 0, "MayJunk2": 0, 
    "JuneAnimals": 10, "JuneRibbonBlue": 5, "JuneJunk1": 0, "JuneJunk2": 0, 
    "JulyAnimals": 10, "JulyRibbonEmpty": 5, "JulyJunk1": 0, "JulyJunk2": 0, 
    "AugustBright": 20, "AugustAnimals": 10, "AugustJunk1": 0, "AugustJunk2": 0, 
    "SeptAnimals": 10, "SeptRibbonBlue": 5, "SeptJunk1": 0, "SeptJunk2": 0, 
    "OctAnimals": 10, "OctRibbonBlue": 5, "OctJunk1": 0, "OctJunk2": 0, 
    "NovBright": 20, "NovJunk1": 0, "NovJunk2": 0, "NovJunk3": 0, 
    "DecBright": 20, "DecAnimals": 10, "DecRibbon": 5, "DecJunk": 0}

    deck_list = []
    for month in deck_dict.keys():
        deck_list.append(month)
        # print(month, value)

    return deck_list


def main():
    play = True

    while play:
        my_game = game.Game()
        current_deck = create_deck()
        current_deck = my_game.shuffle_deck(current_deck)

        human_hand = my_game.new_hand(current_deck)
        board = my_game.new_board(current_deck)
        ai_hand = my_game.new_hand(current_deck)

        ai_agent = ai.AI()

        player_stack = [[], [], [], []]
        ai_stack = [[], [], [], []]

        while len(current_deck) > 0:
            
            print('Player Hand: ')
            print(human_hand)
            print('Player Stack: ')
            print(player_stack)
            print(' ')
            print('Board: ')
            print(board[0], board[1], board[2])
            print(board[3], board[4], board[5])
            print(board[6], board[7], board[8])
            print(board[9], board[10], board[11])
            print(' ')
            # print('AI Hand: ')
            # print(ai_hand)
            print('AI Stack: ')
            print(ai_stack)
            print('\n')


            # Human Player
            player = 'human'
            hand_index = int(input('Select by number: '))
            
            while (hand_index < 0) or (hand_index > len(human_hand)):
                hand_index = int(input('Invalid input. Please re-enter: '))

            print('Human Hand Choice: ', human_hand[hand_index])
            card_hand = human_hand[hand_index]
            del human_hand[hand_index]
            my_game.set_card_onto_board(card_hand, board, player_stack, player)
            my_game.draw_and_set(current_deck, board, player_stack, player)

            # AI Player
            player = 'ai'
            # ai_hand_choice = random.choice(ai_hand)
            ai_hand_choice = ai_agent.decide(board, ai_hand)
            print('AI Hand choice: ', ai_hand_choice)
            ai_hand.remove(ai_hand_choice)
            my_game.set_card_onto_board(ai_hand_choice, board, ai_stack, player)
            my_game.draw_and_set(current_deck, board, ai_stack, player)
            print('\n')



        my_game.calculate(player_stack, ai_stack)
        reply = input('Do you wish to continue(y/n)?')
        if reply == 'y':
            play = True
        else:
            play = False


main()
