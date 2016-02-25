#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

from itertools import permutations

def nextto(f1, f2):
    "Two floors are next to each other if they differ by 1."
    return abs(f1-f2) == 1




# Without  using a generator expression:
def floor_puzzle():
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(permutations(floors))
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
          if (Hopper is not top
          and Kay is not bottom
          and Liskov is not top
          and Liskov is not bottom
          and Perlis > Kay
          and not nextto(Ritchie, Liskov)
          and not nextto(Liskov, Kay)):
                return [Hopper, Kay, Liskov, Perlis, Ritchie]
   