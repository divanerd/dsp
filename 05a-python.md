# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing. Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.  Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> **Sets** are *Unordered collections of unique elements* --> ie: all words used in a speech.  **Lists** are *ordered collections of elements* --> ie: telephone number respository

1) **List**

   fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
   fruits.count('apple')

2) **Set**

   engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
   programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
   managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
   employees = engineers | programmers | managers  


Sets allows you to do operations such as intersection, union, difference, and symmetric difference.  Sets doesn't allow indexing and are implemented on hash tables.  Lists are variable-length arrays. In lists the elements are accessed by indices.  When you want to store some values which you'll be iterating over, Python's list constructs are slightly faster. However, if you'll be storing (unique) values in order to check for their existence, then sets are significantly faster (constant time not based on size of set).

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda function is a function that takes any number of arguments and returns the value of a single expression. lambda functions can't contain commands, and they can not contain more than one expression. lambda is a quick way of making functions.

ie: getFirst = lambda x: x[0]

ie: sorted(student_tuples, key=lambda student: student[2])   # sort by age

[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> We can write map and filter patterns more concisely using a list comprehension.
The bracket operators indicate that we are constructing a new list. The expression inside the brackets specifies the elements of the list, for clause indicates what sequence we are traversing. 

**map**
def capitalizeall(t):
   return [s.capitalize() for s in t]

**filter**
def findOnlyCapitals(t)
   return [s for s in t if s.isupper()]

**set comprehension**
s = { x for x in range(10) }

**dictionary comprehension**
d = {k:v for k, v in iterable}

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





