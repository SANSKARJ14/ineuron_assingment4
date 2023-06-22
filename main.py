#ASSINGMENT 4
"""
 1. What exactly is []?

IT Represents an empty list. A list is a data structure that can hold multiple values in a specific order.
The "[]" notation indicates that there are no elements currently present in the list.

"""
"""
2.In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)"""

spam = [2, 4, 6, 8, 10]
spam[2] = "hello"
print (spam)


#3. What is the value of spam[int(int('3' * 2) / 11)]?
"""
#spam= [a, b, c, d]
#spam[int(int('3' * 2) / 11)] 
# output will 3 because 33/11 so answer will be d

#"4. What is the value of spam[-1]? # output will be d

#5. What is the value of spam[:2]? # output will be a and b

#Let pretend bacon has the list [3.14,'cat', 11,'cat',True] for the next three questions.

bacon = [3.14,'cat', 11,'cat',True]

#6. What is the value of bacon.index('cat')?

bacon.index('cat') # output = 1

#7 How does bacon.append(99) change the look of the list value in bacon? 
#output will be [3.14,'cat', 11,'cat',True,99]
#8 How does bacon.remove(cat) change the look of the list in bacon?
# output will [3.14,11,'cat',true]

"""
9. What are the list concatenation and list replication operators?.

the list concatenation operator (+) merges lists together, while the list replication operator (*) 
creates a new list by repeating the elements of an existing list. 
These operators provide useful ways to manipulate lists in Python, enabling us to combine or replicate their elements
as needed""".

# list concatination
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]
#list replication
list1 = [1, 2, 3]
result = list1 * 3
print(result)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

""""
10. What is difference between the list methods append() and insert()?

append() adds an element to the end of the list, while insert() inserts an element at a specific position
within the list.
append 
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

insert
my_list = [1, 2, 3]
my_list.insert(1, 5) in frist place there is position where i want to insert and 2nd what i  wanted to insert
print(my_list)  # Output: [1, 5, 2, 3]
"""

"""
11. What are the two methods for removing items from a list?

through pop and remove function we can remove item from the list. remove is used when we wanted to any particular 
thing. and pop is used when we want to remove based on index 
"""


"""
12.Describe how list values and string values are identical.

List values and string values in Python share some similarities and characteristics, but they are not identical.

Similarities:

Both lists and strings can store multiple values or characters.
Both lists and strings can be accessed using indexing and slicing.
Both lists and strings are ordered, meaning that the order of the elements or characters is preserved.
"""
"""
#13.what is difference between tuples and list 

Mutability: Tuples are immutable, which means their elements cannot be changed once they are created. and 
           mutable 
syntax - list [] and tuples ()
performance - tuples have better performance because they are immutable 
list give more flexibility 
"""
""" 
14. How do you type a tuple value that only contains the integer 42?

tuple_value = (42,)
Note the comma (,) after the integer 42. This is important because a single value enclosed in
parentheses () is not recognized as a tuple by Python. The comma after the value ensures
that it is treated as a tuple with one element.
"""
"""
15. How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?

we can use tuple(). 
list = [1, 2, 3, 4]
tuple_form = tuple(list)
print(tuple_form)

"""
"""
16. Variables that contain list values are not necessarily lists themselves. Instead, what do they
contain?

Variables that "contain" list values in Python do not actually contain the lists themselves.
Instead, they contain references or pointers to the list objects stored in memory.
"""
"""
17. How do you distinguish between copy.copy() and copy.deepcopy()?

copy.copy() creates a shallow copy, which shares references with the original object, while copy.deepcopy()
creates a deep copy, which recursively copies all nested objects,
ensuring complete independence. The choice between them depends on your specific requirements for
manipulating objects and nested data structures.
"""








































































