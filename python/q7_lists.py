# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
import numpy

def match_ends(words):
    counter = 0
    for i in words:
         if len(i) >= 2 and i[0] == str(i[(len(i)-1)]):
            counter += 1
    return counter
    #print(counter)

# match_ends(['aa', 'zz', 'aa', 'x', 'bbb', 'oooooooooooo'])
#     """
#     Given a list of strings, return the count of the number of strings
#     where the string length is 2 or more and the first and last chars
#     of the string are the same.
#     >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
#     3
#     >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
#     2
#     >>> match_ends(['aaa', 'be', 'abc', 'hello'])
#     1
#     """
#     raise NotImplementedError


def front_x(words):
    x_words = []
    non_xs = []
    for i in words: 
        if i[0] == 'x':
            x_words.append(i)
        else: 
            non_xs.append(i)
    res = sorted(x_words) + sorted(non_xs)
    #print (res)
    return res
#front_x(['xoop', 'timmi', 'oms', 'mimz', 'xaap'])


#     """
#     Given a list of strings, return a list with the strings in sorted
#     order, except group all the strings that begin with 'x' first.
#     e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
#          ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
#     >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
#     ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
#     >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
#     ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
#     >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
#     ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
#     """
#     raise NotImplementedError


def sort_last(tuples):
    res = sorted(tuples, key=lambda x: x[-1])
    return res
    #print (res)

# sort_last([(1, 7), (1, 3), (3, 4, 9), (2, 2)])

#     """
#     Given a list of non-empty tuples, return a list sorted in
#     increasing order by the last element in each tuple.
#     e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
#          [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
#     >>> sort_last([(1, 3), (3, 2), (2, 1)])
#     [(2, 1), (3, 2), (1, 3)]
#     >>> sort_last([(2, 3), (1, 2), (3, 1)])
#     [(3, 1), (1, 2), (2, 3)]
#     >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
#     [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
#     """
#     raise NotImplementedError


def remove_adjacent(nums):
    uniques = numpy.unique(nums)
    return uniques
    #print (uniques)

# remove_adjacent([1, 3, 4, 5, 6, 7, 8, 8, 9 ,8])

#     """
#     Given a list of numbers, return a list where all adjacent equal
#     elements have been reduced to a single element, so [1, 2, 2, 3]
#     returns [1, 2, 3]. You may create a new list or modify the passed
#     in list.
#     >>> remove_adjacent([1, 2, 2, 3])
#     [1, 2, 3]
#     >>> remove_adjacent([2, 2, 3, 3, 3])
#     [2, 3]
#     >>> remove_adjacent([3, 2, 3, 3, 3])
#     [3, 2, 3]
#     >>> remove_adjacent([])
#     []
#     """
#     raise NotImplementedError


def linear_merge(list1, list2):
    new_list = sorted(list1 + list2)
    return new_list
    #print(new_list)
#linear_merge(['michelle', 'chimi'], ['timmie', 'oumie'])


#     """
#     Given two lists sorted in increasing order, create and return a
#     merged list of all the elements in sorted order. You may modify
#     the passed in lists. Ideally, the solution should work in "linear"
#     time, making a single pass of both lists.
#     >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
#     ['aa', 'bb', 'cc', 'xx', 'zz']
#     >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
#     ['aa', 'bb', 'cc', 'xx', 'zz']
#     >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
#     ['aa', 'aa', 'aa', 'bb', 'bb']
#     """
#     raise NotImplementedError