# -----------
# User Instructions
# 
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...

# My method:
def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    mapping = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    ranks = [mapping[r] if r in mapping else int(r) for r,s in cards]
    ranks.sort(reverse=True)
    return ranks

# Instructor's method:
def card_ranks_ins(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return ranks


print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]