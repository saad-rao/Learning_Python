
# Working with Lists and Tuples:
# Python provides powerful sequence types: lists and tuples. 
# These data structures help store and manage collections of data efficiently.

car:list = ['Toyota', 'Honda', 'BMW', 'Audi', 'Ford']
print(car.extend(['Jeep', 'Kia', 'Hyundai']))
# print(car.append('jeep'))
print(car)


# Modifying Lists:
# Lists are mutable, meaning their elements can be changed.


car:list = ['Toyota', 'Honda', 'BMW', 'Audi', 'Ford'];
car[2] = 'Jeep';
print(car);



# List Slicing:
# Extract multiple elements using slicing.

car:list = ['Toyota', 'Honda', 'BMW', 'Audi', 'Ford'];
print(car[1:4]);
print(car[:4]);
print(car[1:]);
print(car[:]);


# Removing Elements
# In Python, remove() and pop() are two distinct methods used to manipulate lists. While they may seem similar, they have different purposes and behaviors.

# Remove() Method

# The remove() method is used to delete the first occurrence of a specified 
# value from a list. If the value is not found in the list, a ValueError exception
# is raised.

car:list = ['Toyota', 'Honda', 'BMW', 'Audi', 'Ford'];
car.remove('BMW');
print(car);


# The remove() method is used to delete the first occurrence of a specified value from a list. If the value is not found in the list, a ValueError exception is raised.

# Key aspects of remove():

# Value-based: remove() searches for a specific value in the list.

# Returns None: The remove() method does not return any value.

# Raises ValueError: If the value is not found in the list, a ValueError exception is
# raised.

car:list = ['Toyota', 'Honda', 'BMW', 'Audi', 'Ford'];
car.remove('BMW');
print(car);


# Pop() Method:
# The pop() method is used to delete an item at a specified index from a list. If no index is provided, it removes and returns the last item in the list.

# Key aspects of pop():
# Index-based: pop() searches for an item at a specific index in the list.

# Returns the removed item: The pop() method returns the item that was removed from the list.

# Raises IndexError: If the index is out of range, an IndexError exception is raised.

car:list = ['Toyota', 'Honda', 'BMW', 'Audi', 'Ford'];
car.pop(2);
print(car);



# Sorting a List
# The sorted() function returns a new list containing the sorted elements of the original list.
# The original list remains unchanged.    
number:int = [0,3,5,2,6,7,1,10,4,8,9];
print(sorted(number));

number.reverse();
print(number);





#  Tuples in Python
# A tuple is an ordered, immutable (unchangeable) sequence of elements. 
# Tuples are useful for fixed data collections.

# In Python, a tuple is an immutable data type.
# This means that once a tuple is created, its elements cannot be changed, added, or removed.

# 1. Cannot Modify Elements:
# Once a tuple is created, you cannot change its elements.
# 2. Cannot Add or Remove Elements:
# You cannot add new elements to a tuple or remove existing ones.
