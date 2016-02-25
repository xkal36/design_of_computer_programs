# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1
    
# My answer:
def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    i = 0
    while True:
        yield i
        if i != -i:
            yield -i
        i += 1
        
# Could also be:
def all_ints_2():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    i = 0
    yield i
    while True:
        yield (i + 1)
        yield -(i + 1)
        
# Could also be:
def all_ints_3():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    yield 0
    i = 1
    while True:
        yield i
        yield -i
        i += 1

# Instructor's answer:
def all_ints_ins(end=100):
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    yield 0
    for i in ints(1):
        yield +i
        yield -i
