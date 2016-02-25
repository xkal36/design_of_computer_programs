# CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The 
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart 
# or diamond.
#
# The itertools library may be helpful. Feel free to 
# define multiple functions if it helps you solve the
# problem. 
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    return max(itertools.combinations(hand, 5), key=hand_rank)

def wild_card_poss(ranks, suits):
    combinations = []
    for suit in suits:
        for rank in ranks:
            combinations.append(rank + suit)
    return combinations

def wild_card_rep(hand):
    vals = '23456789TJQKA'
    hand_list = list(hand)
    for card in hand_list:
        if card == '?B':
            hand_list[hand_list.index(card)] = wild_card_poss(vals, 'SC')
        elif card == '?R':
            hand_list[hand_list.index(card)] = wild_card_poss(vals, 'HD')
    return tuple(hand_list)

def form(l):
    return map(lambda x: x.split(" ") if len(x) < 3 else x, l)

def get_combs(l):
    all_combs = []
    for item in itertools.product(*l):
        all_combs.append(" ".join(item))
    return all_combs

# My solution:
def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    all_poss_hands = itertools.combinations(hand, 5)
    all_poss_hands_repl = map(list, map(wild_card_rep, all_poss_hands))
    formatted_hands = map(form, all_poss_hands_repl)
    all_combs = map(lambda x: x.split(' '), reduce(lambda x, y: x+y, map(get_combs, formatted_hands)))
    return max(all_combs, key=hand_rank)
    
    
# Instructor's solution:
def best_wild_hand_ins(hand):
    "Try all values for jokers in all 5-card selections."
    hands = set(best_hand(h) for h in itertools.product(*map(replacements, hand)))
    return max(hands, key=hand_rank)
    
def replacements(card):
    all_black_cards = [r+s for r in '23456789TJQKA' for s in 'SC'] 
    all_red_cards = [r+s for r in '23456789TJQKA' for s in 'HD']
    if card == '?B': return all_black_cards
    elif card == '?R': return all_red_cards
    else: return [card]

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'


