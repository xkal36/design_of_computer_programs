# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.


# My answers:

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    states = {}
    
    # We can only cross the bridge with the torch
    # So we move from whatever side contains the string 'light'
    if 'light' in here:
        for person in filter(lambda x: x != 'light', here):
            here_after_move = frozenset(filter(lambda x: x != person and x != 'light', here))
            there_after_move = frozenset(list(there) + [person, 'light'])
            states[(here_after_move, there_after_move, t + person)] = (person, person, '->')
    else:
        for person in filter(lambda x: x != 'light', there):
            there_after_move = frozenset(filter(lambda x: x != person and x != 'light', there))
            here_after_move = frozenset(list(here) + [person, 'light'])
            states[(here_after_move, there_after_move, t + person)] = (person, person, '<-')
    return states
      
# Helper function for bsuccessors2
def cross_bridge(move_from, move_to , person, t):
     from_after_move = frozenset(filter(lambda x: x != person and x != 'light', move_from))
     to_after_move = frozenset(list(move_to) + [person, 'light'])
     return (from_after_move, to_after_move, person + t)

# Recfactored according to DRY principle:    
def bsuccessors2(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    states = {}
    # We can only cross the bridge with the torch
    # So we move from whatever side contains the string 'light'
    move_from = here if 'light' in here else there
    move_to = there if 'light' in here else here
    for person in filter(lambda x: x != 'light', move_from):
        new_state = cross_bridge(move_from, move_to, person, t)
        new_here = new_state[0] if move_from == here else new_state[1]
        new_there = new_state[1] if move_to == there else new_state[0]
        new_state_ordered = (new_here, new_there, new_state[2])
        if move_from == here:
            states[new_state_ordered] = (person, person, '->')
        else:
            states[new_state_ordered] = (person, person, '<-')
    return states

# Peter's answer:
def bsuccessors_peter(state):
    """Return a dict of {state:action} pairs.  A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the light, and t is a number indicating the elapsed time."""
    here, there, t = state
    if 'light' in here:
        return dict(((here  - frozenset([a,b, 'light']),
                      there | frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here  | frozenset([a,b, 'light']),
                      there - frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light') 
        
    
    

def test():
    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'


print test()