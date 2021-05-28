import random

class Game:
    def __init__(self):
        self.new_deck = []

    def shuffle_deck(self, deck):
        self.new_deck = deck
        random.shuffle(self.new_deck)
        return self.new_deck

    # empty board
    def new_board(self, deck):
        self.board = [[], [], [], 
        [], [], [], 
        [], [], [], 
        [], [], []]

        index = 0
        set_on_field = False

        for i in range(8):
            while set_on_field is False:
                if not self.board[index]:
                    self.board[index].append(deck.pop(0))
                    index = 0
                    break
                elif deck[0][:3] == self.board[index][0][:3]:
                    self.board[index].append(deck.pop(0))
                    index = 0
                    break
                else:
                    index+=1

        return self.board

    # empty hand player
    def new_hand(self, deck):
        self.hand = []

        for i in range (10):
            self.hand.append(deck.pop())

        return self.hand

    # set a card from hand onto board
    # Add card collected stack as 4th parameter
    def set_card_onto_board(self, hand, board, collect_stack, player):
        value_list = ['Bright', 'Animals', 'Ribbon', 'Junk']
        index = 0

        acquired = False

        for card_stack_field in board:
            temp = '\t'.join(card_stack_field)
            if not card_stack_field:
                index += 1
                continue
            elif hand[:3] == card_stack_field[0][:3]:
                # If stack contains 3 cards of the same stack
                if len(card_stack_field) == 3:
                    for card_value in card_stack_field:
                        if 'Bright' in card_value:
                            collect_stack[0].append(card_value)
                        elif 'Animals' in card_value:
                            collect_stack[1].append(card_value)
                        elif 'Ribbon' in card_value:
                            collect_stack[2].append(card_value)
                        elif 'Junk' in card_value:
                            collect_stack[3].append(card_value)
                    # Add card from hand into collection stack
                    if 'Bright' in hand:
                        collect_stack[0].append(hand)
                    elif 'Animals' in hand:
                        collect_stack[1].append(hand)
                    elif 'Ribbon' in hand:
                        collect_stack[2].append(hand)
                    elif 'Junk' in hand:
                        collect_stack[3].append(hand)
                    board[index].clear()
                    board[index] = []
                    acquired = True
                    break
                elif ('Red' in temp or 'Blue' in temp or 'Empty' in temp) and ('Bright' in temp or 'Animals' in temp):
                    if player == 'ai':
                        reply = 'v'
                    else:
                        reply = input('Pick ribbon(r) or Other value(v): ')
                    if reply == 'r':
                        for card_value in card_stack_field:
                            if 'Ribbon' in card_value:
                                collect_stack[2].append(card_value)
                                board[index].remove(card_value)
                                acquired = True
                                break
                        # Add card from hand into collection stack
                        if 'Bright' in hand:
                            collect_stack[0].append(hand)
                        elif 'Animals' in hand:
                            collect_stack[1].append(hand)
                        elif 'Ribbon' in hand:
                            collect_stack[2].append(hand)
                        elif 'Junk' in hand:
                            collect_stack[3].append(hand)
                    else:
                        for card_value in card_stack_field:
                            if 'Bright' in card_value:
                                collect_stack[0].append(card_value)
                                board[index].remove(card_value)
                                acquired = True
                                break
                            elif 'Animals' in card_value:
                                collect_stack[1].append(card_value)
                                board[index].remove(card_value)
                                acquired = True
                                break
                        # Add card from hand into collection stack
                        if 'Bright' in hand:
                            collect_stack[0].append(hand)
                        elif 'Animals' in hand:
                            collect_stack[1].append(hand)
                        elif 'Ribbon' in hand:
                            collect_stack[2].append(hand)
                        elif 'Junk' in hand:
                            collect_stack[3].append(hand)
                else:
                    found = False
                    for i in range(len(value_list)):
                        for card_value in card_stack_field:
                            if value_list[i] in card_value:
                                if 'Bright' in card_value:
                                    collect_stack[0].append(card_value)
                                elif 'Animals' in card_value:
                                    collect_stack[1].append(card_value)
                                elif 'Ribbon' in card_value:
                                    collect_stack[2].append(card_value)
                                elif 'Junk' in card_value:
                                    collect_stack[3].append(card_value)
                                board[index].remove(card_value)
                                acquired = True
                                found = True
                                break
                        if found is True:
                            break
                    # Add card from hand into collection stack
                    if 'Bright' in hand:
                        collect_stack[0].append(hand)
                    elif 'Animals' in hand:
                        collect_stack[1].append(hand)
                    elif 'Ribbon' in hand:
                        collect_stack[2].append(hand)
                    elif 'Junk' in hand:
                        collect_stack[3].append(hand)
                break
            else:
                index += 1
                continue
            

        if acquired is False:
            index = 0
            for card_stack_field in board:
                if not card_stack_field:
                    board[index].append(hand)
                    break
                index += 1


    def draw_and_set(self, deck, board, collect_stack, player):
        self.card = deck.pop()
        print("Card from deck: ", self.card)

        value_list = ['Bright', 'Animals', 'Ribbon', 'Junk']

        index = 0

        acquired = False

        for card_stack_field in board:
            temp = '\t'.join(card_stack_field)
            if not card_stack_field:
                index += 1
                continue
            elif self.card[:3] == card_stack_field[0][:3]:
                # If stack contains 3 cards of the same stack
                if len(card_stack_field) == 3:
                    for card_value in card_stack_field:
                        if 'Bright' in card_value:
                            collect_stack[0].append(card_value)
                        elif 'Animals' in card_value:
                            collect_stack[1].append(card_value)
                        elif 'Ribbon' in card_value:
                            collect_stack[2].append(card_value)
                        elif 'Junk' in card_value:
                            collect_stack[3].append(card_value)

                    # Add card from deck into collection stack
                    if 'Bright' in self.card:
                        collect_stack[0].append(self.card)
                    elif 'Animals' in self.card:
                        collect_stack[1].append(self.card)
                    elif 'Ribbon' in self.card:
                        collect_stack[2].append(self.card)
                    elif 'Junk' in self.card:
                        collect_stack[3].append(self.card)
                    board[index].clear()
                    board[index] = []
                    acquired = True
                    break
                elif ('Red' in temp or 'Blue' in temp or 'Empty' in temp) and ('Bright' in temp or 'Animals' in temp):
                    if player == 'ai':
                        reply = 'r'
                    else:
                        reply = input('Pick ribbon(r) or Other value(v): ')
                    if reply == 'r':
                        for card_value in card_stack_field:
                            if 'Ribbon' in card_value:
                                collect_stack[2].append(card_value)
                                board[index].remove(card_value)
                                acquired = True
                                break
                        # Add card from deck into collection stack
                        if 'Bright' in self.card:
                            collect_stack[0].append(self.card)
                        elif 'Animals' in self.card:
                            collect_stack[1].append(self.card)
                        elif 'Ribbon' in self.card:
                            collect_stack[2].append(self.card)
                        elif 'Junk' in self.card:
                            collect_stack[3].append(self.card)
                    
                    else:
                        for card_value in card_stack_field:
                            if 'Bright' in card_value:
                                collect_stack[0].append(card_value)
                                board[index].remove(card_value)
                                acquired = True
                                break
                            elif 'Animals' in card_value:
                                collect_stack[1].append(card_value)
                                board[index].remove(card_value)
                                acquired = True
                                break
                        # Add card from deck into collection stack
                        if 'Bright' in self.card:
                            collect_stack[0].append(self.card)
                        elif 'Animals' in self.card:
                            collect_stack[1].append(self.card)
                        elif 'Ribbon' in self.card:
                            collect_stack[2].append(self.card)
                        elif 'Junk' in self.card:
                            collect_stack[3].append(self.card)
                else:
                    found = False
                    for i in range(len(value_list)):
                        for card_value in card_stack_field:
                            if value_list[i] in card_value:
                                if 'Bright' in card_value:
                                    collect_stack[0].append(card_value)
                                elif 'Animals' in card_value:
                                    collect_stack[1].append(card_value)
                                elif 'Ribbon' in card_value:
                                    collect_stack[2].append(card_value)
                                elif 'Junk' in card_value:
                                    collect_stack[3].append(card_value)
                                board[index].remove(card_value)
                                acquired = True
                                found = True
                                break
                        if found is True:
                            break
                    # Add card from deck into collection stack
                    if 'Bright' in self.card:
                        collect_stack[0].append(self.card)
                    elif 'Animals' in self.card:
                        collect_stack[1].append(self.card)
                    elif 'Ribbon' in self.card:
                        collect_stack[2].append(self.card)
                    elif 'Junk' in self.card:
                        collect_stack[3].append(self.card)
                break
            else:
                index += 1
                continue

        if acquired is False:
            index = 0
            for card_stack_field in board:
                # NEEDS TO STACK ON SAME SET OF CARDS IF EXISTS
                if not card_stack_field:
                    board[index].append(self.card)
                    break
                index += 1

    def calculate(self, human_stack, ai_stack):
        special_set = ['May', 'October', 'December']
        human_total_score = (20 * int(len(human_stack[0]))) + (10*int(len(human_stack[1]))) + (5*int(len(human_stack[2])))

        ai_total_score = (20 * int(len(ai_stack[0]))) + (10*int(len(ai_stack[1]))) + (5*int(len(ai_stack[2])))

        # Check for special sets

        # Human special sets
        for card_set in special_set:
            special_set_total = 0
            for stack in human_stack:
                for card in stack:
                    if card[:3] == card_set[:3]:
                        special_set_total += 1
            if special_set_total == 4:
                human_total_score += 20
        
        # AI special sets
        for card_set in special_set:
            special_set_total = 0
            for stack in ai_stack:
                for card in stack:
                    if card[:3] == card_set[:3]:
                        special_set_total += 1
            if special_set_total == 4:
                ai_total_score += 20
        

        print('Human Score: ', human_total_score)
        print('AI Score: ', ai_total_score)

        if human_total_score > ai_total_score:
            print('You WIN!')
        elif human_total_score < ai_total_score:
            print('AI WINS!')
        else:
            print('DRAW')



