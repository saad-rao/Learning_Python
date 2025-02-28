# Dictionaries in Python

# Introduction to Dictionaries
# A dictionary is a collection of key-value pairs. It is:

# Ordered (since Python 3.7): Items are stored in the order they were inserted.

# Mutable: Items can be added, removed, or modified after the dictionary is created.

# Un-indexed: Items are accessed using keys, not indices.

# Without duplicates: Keys must be unique, but values can be duplicated.

# Before Python 3.7, dictionaries were unordered, meaning that items were not stored in a specific order. However, with the introduction of Python 3.7, dictionaries now maintain their insertion order.

# OrderedDict vs dict in Python: The Right Tool for the Job

# 2. Creating a Dictionary
# Dictionaries are created using curly braces {} with key-value pairs separated by commas.

# The syntax is:

# dictionary = {key1: value1, key2: value2, ...}
# Example Code:

person: dict = {
    "name":"saad",
    "age":22
}


# 3. Accessing Values
# You can access the value associated with a key using square brackets [] or the get() method.

# Example Code:

print(person["name"])
print(person.get("age"))    


# 3. Accessing Values
# You can access the value associated with a key using square brackets [] or the get() method.

# Example Code:

person["name"] = "asad"
person["age"] = 20