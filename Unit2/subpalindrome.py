# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def all_substrings(input_string):
    length = len(input_string)
    return filter(lambda x: len(x) > 1, 
        [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)])


def is_palindrome(s):
    if len(s) < 2:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome2(s[1:-1])
        else:
            return False 


def is_palindrome2(s):
    s_list = [char for char in s]
    still_equal = True
    while still_equal and len(s_list) > 1:
        first = s_list.pop(0)
        last = s_list.pop()
        if first != last:
            still_equal = False
    return still_equal
     
    
    
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text_lower = text.lower()
    all_subs = all_substrings(text_lower)
    palindromes = filter(lambda sub_st: is_palindrome2(sub_st), all_subs)
    if palindromes:
        largest = max(palindromes, key=len)
        return text_lower.find(largest), text_lower.find(largest) + len(largest)
    else:
        return (0, 0)
        
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()