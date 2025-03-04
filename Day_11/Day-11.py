# SET

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# Set ke Key Concepts
# Unique Values : Duplicate nahi hote
# Unordered : Set me elements ka koi fixed order nahi hota
# Mutable : Set me naye elements add/remove ho sakte hain
# Heterogeneous : Set me different types ke values ho sakti hain
# Unindexed : Set me indexing nahi hoti

# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.
   

fruits = {"apple", "banana", "cherry"}
print(fruits)  # {'apple', 'banana', 'cherry'}

#  Order same nahi hoga har execution pe kyunki sets unordered hote hain.


# Set Operations

# Add Elements in Set

my_set = {1, 2, 3}
my_set.add(4)  # Set me ek element add karega
print(my_set)  # {1, 2, 3, 4}


# Remove Elements in Set

my_set.remove(2)  # Agar element nahi mila to error dega
print(my_set)

my_set.discard(10)  # Agar element nahi mila to kuch nahi hoga


#  Set Operations (Union, Intersection, Difference, Symmetric Difference)
# Union (|) : Dono sets ke sab unique elements

A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # {1, 2, 3, 4, 5}


#  Intersection (&) : Sirf common elements
print(A & B)  # {3}

# Difference (-)  A wale jo B me nahi hain

print(A - B)  # {1, 2}

# Symmetric Difference (^)  Jo sirf ek set me hain

print(A ^ B)  # {1, 2, 4, 5}