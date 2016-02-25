# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

# First way:
def deal(numhands, n=5, deck=mydeck):
    to_deal = []
    random.shuffle(deck)
    card_num = 0
    while card_num < (n * numhands):
        hand = []
        for i in range(n):
            hand.append(deck[card_num])
            card_num += 1
        to_deal.append(hand)
    return to_deal

# Better way:
def deal_better(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    return [deck[n*i:n*(i +1)] for i in range(numhands)]