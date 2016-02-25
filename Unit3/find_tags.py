# ---------------
# User Instructions
#
# Write a function, findtags(text), that takes a string of text
# as input and returns a list of all the html start tags in the 
# text. It may be helpful to use regular expressions to solve
# this problem.

import re

# My naive Naive solution:
def findtags_naive(text):
    return re.findall(r'\<(?:[^(?:\<\/)|\'])*\>', text)

# My better solution:
def findtags(text):
    possible_tags = re.findall(r'\<(?:[^(?:\<\/)])*\>', text)
    correct_tags = []
    for tag in possible_tags:
        if len(tag) - tag.count(' ') > 3:
            if '=' in tag:
                correct_tags.append(tag)
        else:
            correct_tags.append(tag)
    return correct_tags

# Best solution (instructor's):
def findtags_ins(text):
    params = '(\w+\s*=\s*"[^"]*"\s*)*'
    tags = '(<\s*\w+\s*'+ params +'\s*/?>)'
    return re.findall(tags, text)

# Instructor's solution modified (only returns full tags):
def findtags_ins_mod(text):
    params = '(\w+\s*=\s*"[^"]*"\s*)*'
    tags = '(<\s*\w+\s*'+ params +'\s*/?>)'
    return map(lambda x: x[0], re.findall(tags, text))


testtext1 = """
My favorite website in the world is probably 
<a href="www.udacity.com">Udacity</a>. If you want 
that link to open in a <b>new tab</b> by default, you should
write <a href="www.udacity.com"target="_blank">Udacity</a>
instead!
"""

testtext2 = """
Okay, so you passed the first test case. <let's see> how you 
handle this one. Did you know that 2 < 3 should return True? 
So should 3 > 2. But 2 > 3 is always False.
"""

testtext3 = """
It's not common, but we can put a LOT of whitespace into 
our HTML tags. For example, we can make something bold by
doing <         b           > this <   /b    >, Though I 
don't know why you would ever want to.
"""

def test():
    assert findtags(testtext1) == ['<a href="www.udacity.com">', 
                                   '<b>', 
                                   '<a href="www.udacity.com"target="_blank">']
    assert findtags(testtext2) == []
    assert findtags(testtext3) == ['<         b           >']
    return 'tests pass'

print test()