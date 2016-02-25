# -----------------
# User Instructions
# 
# Write a function, csuccessors, that takes a state (as defined below) 
# as input and returns a dictionary of {state:action} pairs. 
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where 
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings: 
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C', '<-CC'
# where 'MM->' means two missionaries travel to the right side.
# 
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.

# My answer:
def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    successors = {}
    
    ## Check for state with no successors
    if (C1 > M1) or (C2 > M2):
        return successors
    # Check for any negative number of people:
    elif any(map(lambda x: x < 0, state[:4])):
        return "Cannot have a negative number of people!!!"
    else:
        if B1 == 1 and B2 == 0: # moving from left to right
            actions = ['MM->', 'MC->', 'M->', 'C->', 'CC->']
            for action in actions:
                num_miss_move = action.count('M')
                num_cann_move = action.count('C')
                successors[(M1 - num_miss_move, C1 - num_cann_move, 
                            0, M2 + num_miss_move, 
                            C2 + num_cann_move, 1)] = action
        
        elif B2 == 1 and B1 == 0: # moving from right to left
            actions = ['<-MM', '<-MC', '<-M', '<-C', '<-CC']
            for action in actions:
                num_miss_move = action.count('M')
                num_cann_move = action.count('C')
                successors[(M1 + num_miss_move, C1 + num_cann_move, 
                            1, M2 - num_miss_move, 
                            C2 - num_cann_move, 0)] = action
        else:
            return "Can't be on both sides at once!!!"
    return successors
            

# Peter's answer:

def add(X, Y):
    "add two vectors, X and Y."
    return tuple(x+y for x, y in zip(X, Y))

def sub(X, Y):
    "subtract two vectors, X and Y."
    return tuple(x-y for x, y in zip(X, Y))

deltas = {
    (2, 0, 1,   -2,  0, -1): 'MM',
    (0, 2, 1,    0, -2, -1): 'CC',
    (1, 1, 1,   -1, -1, -1): 'MC',
    (1, 0, 1,   -1,  0, -1): 'M',
    (0, 1, 1,    0, -1, -1): 'C'}      
    

def csuccessors_peter(state):
    # Norvig's solution, with a check to make sure no state has negative numbers.
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    ## Check for state with no successors
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}
    items = []
    if B1 > 0:
        for delta, a in deltas.items():
            x = sub(state, delta)
            if all(val >= 0 for val in x):
                items.append((sub(state, delta), a + '->'))
    if B2 > 0:
        for delta, a in deltas.items():
            x = add(state, delta)
            if all(val >= 0 for val in x):
                items.append((add(state, delta), '<-' + a))
    return dict(items)

       
        
def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->', 
                                               (1, 2, 0, 1, 0, 1): 'M->', 
                                               (0, 2, 0, 2, 0, 1): 'MM->', 
                                               (1, 1, 0, 1, 1, 1): 'MC->', 
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C', 
                                               (2, 1, 1, 3, 3, 0): '<-M', 
                                               (3, 1, 1, 2, 3, 0): '<-MM', 
                                               (1, 3, 1, 4, 1, 0): '<-CC', 
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print test()