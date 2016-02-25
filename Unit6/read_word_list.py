# -----------------
# User Instructions
# 
# Write a function, readwordlist, that takes a filename as input and returns
# a set of all the words and a set of all the prefixes in that file, in 
# uppercase. For testing, you can assume that you have access to a file 
# called 'words4k.txt'

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

# My answer:
def readwordlist(filename):
    """Read the words from a file and return a set of the words 
    and a set of the prefixes."""
    file = open(filename) # opens file
    text = file.read()    # gets file into string
    wordset = set(text.upper().split())
    prefixset = set([prefix_list[i] for prefix_list in map(prefixes, wordset) 
                     for i in range(len(prefix_list))])
    return wordset, prefixset

# Peter's answer:
def readwordlist_peter(filename):
    """Read the words from a file and return a set of the words 
    and a set of the prefixes."""
    file = open(filename)
    wordset = set(file.read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

def test():
    assert len(WORDS)    == 3892
    assert len(PREFIXES) == 6475
    assert 'UMIAQS' in WORDS
    assert 'MOVING' in WORDS
    assert 'UNDERSTANDIN' in PREFIXES
    assert 'ZOMB' in PREFIXES
    return 'tests pass'

print test()