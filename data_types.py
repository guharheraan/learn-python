# we have numeric,sequence,boolean,set,dictionary
# --------------------------------- Numeric  -------------------------------- 
# first let start with the numeric
# numeric datatype has three types of data such as

x = 12 #this is the  integer type
y = 11.5 # this is float or decimal type
z = 12 + 3j #this is a complex datatype 

# we can check the data type of any variable or constant in the program by the following function

# print(type(x)) # will return <class 'int'>
type(y) # will return <class 'float'>
type(z) # will return <class 'complex'>

# -------------------------------------- boolean ------------------------------ 
# the boolean data type only has two values 
# True and False

# print(1 > 5) # it will return False because 1 is not greater than 5.

# print(type(True))
# print(type(False))

# ------------------------------------- sequence ---------------------------------- 

# now let's move on to sequence which includes list,tuple and strings.

# strings can be written in three ways 

# print('single quotes')
# print("double quotes")

# """
# this is a tripple qoutes string in python.
# untill it is stored in any variable it works as comments 
# so we can use it as a multiLine comment 
# but once its assigned to a variable it works as the <pre> tag in the html.

# """ here it works as comment 

multiline = """
this is a tripple qoutes string in python.
untill it is stored in any variable it works as comments 
so we can use it as a multiLine comment 
but once its assigned to a variable it works as the <pre> tag in the html.

"""
# print(multiline)
# print(type(multiline))

# ------------------------- lists ------------------------------------- 

# lists can store  multiple items of different types in them.
# lists are like array in other languages and they can be accessed using the index number.

# my_list = [1,3,5,6,7,89,7]

# print(my_list)

# another_list = [1,"hello",[2,4],true]

# print(another_list)

# ----------------------------------- tuple -------------------------- 
# the tuples are used when data is never going to be changed.
# tuples are like the constant variavles  in javaScript which means they cant  be changed after assignment.
# tuples can only store a single type of data  unlike list that can store multiple types.

# my_tuple = (1,2,4,5,6,7,8,9)

# print(my_tuple)

# strings_tuple = ("guhar","raban","waseem","ayaz")

# print(strings_tuple)

# -------------------------------------- sets -------------------------------- 
# set is an unordered collection of unique elements.
#  sets do not have indexes rather they have elements .
#  they can not be access by the index number bcz thay dont have it.
# the values of a set can be access by loops but cant by the index number.

# my_set = {1,2,3,4,5}
# print(my_set)

# another_set = {"guhar","raban","waseem","ayaz","guhar"}
# print(another_set)

# numbers = {1,2,4,2,5,6,3,4,2,1,0}
# print(numbers)

# ------------------------------------ dictionaries ---------------------------------- 
# dictionaries are like the object in other languages 
# they dont have the index number instead they have  key value pairs.
# the values of a dictionary can be accessed by their key  name.
# ditionaries can store all datatypes  including lists and tuples inside them.

class_mates = {"regno":1910001,"name":"guhar","semester": 6,"pass":True}

print(class_mates["name"])

print(class_mates)



# ---------------------------------- links for further study -------------------------- 
# https://realpython.com/python-numbers/
# https://www.geeksforgeeks.org/python-string-methods/
# https://realpython.com/python-boolean/ 
# https://www.geeksforgeeks.org/list-methods-python/ 
# https://www.geeksforgeeks.org/python-tuple-methods/
# https://www.geeksforgeeks.org/python-set-methods/
# https://www.geeksforgeeks.org/python-dictionary-methods/