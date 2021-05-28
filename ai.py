import numpy as np
import random

class AI:
    def scan(self, board, hand):
        all_actions = []
        
        for hand_card in hand:
            list_cards = []
            for pile in board:
                if not pile:
                    continue
                if hand_card[:3] == pile[0][:3]:
                    list_cards.append(hand_card)
                    list_cards.append(pile)
                    all_actions.append(list_cards)
         
        # print(all_actions)

        return all_actions
        
        
    def decide(self, board, hand):
        actions = self.scan(board, hand)

        special_set = ['Dec', 'Oct', 'May']

        if not actions:
            return random.choice(hand)

        value_dict = {'Bri': 20, 'Ani': 10, 'Rib': 5, 'Jun': 0}

        max_choice = [] #the choice AI makes that can give the highest value
        max_value = 0 #evaluate which as the most value
        set_value = 0 #evaluate which has the most value within the pile of the same set
        value_hand_card_key = '' 
        value_card_in_pile = 0
        pile = []

        special_set_found = False

        # Search for any special sets from actions
        for month in special_set:
            for choice in actions:
                hand_card_key = choice[0]
                if hand_card_key[:3] == month:
                    # Evaluate value of card from hand
                    if 'Bright' in hand_card_key:
                        value_hand_card_key = value_dict['Bri']
                    elif 'Animals' in hand_card_key:
                        value_hand_card_key = value_dict['Ani']
                    elif 'Ribbon' in hand_card_key:
                        value_hand_card_key = value_dict['Rib']
                    elif 'Junk' in hand_card_key:
                        value_hand_card_key = value_dict['Jun']
                
                    # Evaluate cards value from pile and seek which card has the highest value
                    for card_in_pile in choice[1]:
                        if 'Bright' in card_in_pile:
                            value_card_in_pile = value_dict['Bri']
                        elif 'Animals' in card_in_pile:
                            value_card_in_pile = value_dict['Ani']
                        elif 'Ribbon' in card_in_pile:
                            value_card_in_pile = value_dict['Rib']
                        elif 'Junk' in card_in_pile:
                            value_card_in_pile = value_dict['Jun']

                        if set_value <= (value_hand_card_key + value_card_in_pile):
                            set_value = value_hand_card_key + value_card_in_pile
                            pile = []
                            pile.append(hand_card_key)
                            pile.append(card_in_pile)
                # Pick the one with at least the value of 10. If found then break and return
                if set_value >= 10 and set_value <= 30:
                    special_set_found = True
                    max_choice.append(pile[0])
                    max_choice.append(pile[1])
                    break
            if special_set_found:
                break
        
        if special_set_found:
            return max_choice[0]

        for choice in actions:
            hand_card_key = choice[0]

            # Evaluate value of card from hand
            if 'Bright' in hand_card_key:
                value_hand_card_key = value_dict['Bri']
            elif 'Animals' in hand_card_key:
                value_hand_card_key = value_dict['Ani']
            elif 'Ribbon' in hand_card_key:
                value_hand_card_key = value_dict['Rib']
            elif 'Junk' in hand_card_key:
                value_hand_card_key = value_dict['Jun']
                
            # Evaluate cards value from pile and seek which card has the highest value
            for card_in_pile in choice[1]:
                if 'Bright' in card_in_pile:
                    value_card_in_pile = value_dict['Bri']
                elif 'Animals' in card_in_pile:
                    value_card_in_pile = value_dict['Ani']
                elif 'Ribbon' in card_in_pile:
                    value_card_in_pile = value_dict['Rib']
                elif 'Junk' in card_in_pile:
                    value_card_in_pile = value_dict['Jun']
                    
                if set_value <= (value_hand_card_key + value_card_in_pile):
                    set_value = value_hand_card_key + value_card_in_pile
                    pile = []
                    pile.append(hand_card_key)
                    pile.append(card_in_pile)
            # print('pile: ', pile)
            if max_value <= set_value:
                max_value = set_value
                max_choice = []
                max_choice.append(pile[0])
                max_choice.append(pile[1])

        print(max_choice)
        return max_choice[0]

