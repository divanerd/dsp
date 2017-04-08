# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def donuts(count):
  if count < 10:
    donutcount = count
  else:
    donutcount = 'many'
  print ('Number of donuts: ' + str(donutcount))

donuts(9)

"""
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """

    raise NotImplementedError


def both_ends(s):
    if len(s) < 2:
        final_string = ''
        print(final_string)
    else:
        final_string = str(s[0]) + str(s[1]) + str(s[(len(s)-2)]) + str(s[(len(s)-1)]) 
        print(final_string)

both_ends('patrick')

    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    raise NotImplementedError


def fix_start(s):
    new_word = []
    first_letter = s[0]
    i = 0
    while i < len(s):
        if i == 0:
            letter = s[0]
            new_word.append(letter)
            i+=1
        elif s[i] is first_letter:
            letter = '*'
            new_word.append(letter)
            i+=1
        else:
            letter = s[i]
            new_word.append(letter)
            i+=1
    result = ''.join(new_word)
    print(result)

fix_start('mimmick')

    # """
    # Given a string s, return a string where all occurences of its
    # first char have been changed to '*', except do not change the
    # first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    # string is length 1 or more.
    # >>> fix_start('babble')
    # 'ba**le'
    # >>> fix_start('aardvark')
    # 'a*rdv*rk'
    # >>> fix_start('google')
    # 'goo*le'
    # >>> fix_start('donut')
    # 'donut'
    # """
    # raise NotImplementedError


def mix_up(a, b):
    a_first_letters = a[:2]
    b_first_letters = b[:2] 
    a_last_letters = a[2:]
    b_last_letters = b[2:]

    final_string = str(b_first_letters) + str(a_last_letters) + ' ' + str(a_first_letters) + str(b_last_letters)

    print (final_string)

mix_up('timan','lovish')
    
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError


def verbing(s):
    last_three_letters = s[-3:]
    if len(s) >= 3:
        if str(last_three_letters) == 'ing':
            string_final = str(s) + 'ly'
        else:
            string_final = str(s) + 'ing'
    else:
        string_final = s

    print(string_final)

verbing('timan')
verbing('timaning')

    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError



def not_bad(s):
    #find first position of not
    #then find last position of bad
    #use replace function to replace substring
    starting_subs = s.find('not')
    if s.find('bad') > starting_subs:
        ending_subs = s.find('bad') + 3 #get through the end of 'bad'
        str_to_replace = s[starting_subs:ending_subs]
        final_s = s.replace(s[starting_subs:ending_subs], 'good')
    print (final_s)

not_bad('wow that was not so bad, right?')


    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    # 'This tea is not hot'
    # >>> not_bad("It's bad yet not")
    # "It's bad yet not"
    # """
    raise NotImplementedError

import math

def front_back(a, b):

    def string_parser_front(s):
        if len(s)%2 == 1:
            s_half_i = math.ceil((len(s)/2)) #round up for uneven cases
            new_s = s[:s_half_i] 
        else:
            s_half_i = math.ceil(len(s)/2)
            new_s = s[:s_half_i]
             #if list is len 4, we want up to index 2, if it's 5 we want up to index 3
        return(new_s)

    def string_parser_back(s):
        if len(s)%2 == 1:
            s_half_i = math.ceil((len(s)/2)) #round up for uneven cases
            new_s = s[s_half_i:] 
        else:
            s_half_i = math.ceil(len(s)/2)
            new_s = s[s_half_i:]
                 #if list is len 4, we want up to index 2, if it's 5 we want up to index 3
        return(new_s)

    final_s = []
    final_s.append(str(string_parser_front(a))) 
    final_s.append(str(string_parser_front(b)))
    final_s.append(str(string_parser_back(a)))
    final_s.append(str(string_parser_back(b)))

    result = ''.join(final_s)
    print(result)

front_back('timan', 'michelle')
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help

