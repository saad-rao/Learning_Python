# Modules and functions

# What is module in python?

# A module in Python is a file that includes Python code (functions, classes, variables, or even executable code) and is used to organize and reuse code.

# A module is essentially a.py file that can be loaded and used in other Python scripts.


# Modules help to keep the code reusable, clear, and manageable.

# 1. Built-in Modules
# Python me pehle se kaafi built-in modules hote hain, jaise:

# Math Module

import math

print(math.pi)

import random

print(random.randint(0, 9))

print(random.random())

print(random.choice([1, 2, 3, 4, 5]))


# 2. Custom Module Banana
# Agar tum khud ka module banana chahte ho, toh ek .py file create karo aur usme functions likho.


import my_module

print(my_module.greet("saad"))

print(my_module.add(5,5))


# 3. External Modules (Third-party Libraries)
# Installed via pip (pip install module_name).
# Example: numpy, pandas, requests
# Example usage:

# pip install numpy

# Import with Alias (as)

# import numpy as np


# Import Specific Functions or Variables (from ... import ...)

# from math import pi




What is functions?

# Function ek aisa block of code hota hai jo repeat use ho sakta hai. 
# Jab bhi ek task multiple dafa karna ho, toh hum function bana lete hain 
# taake code reuse ho sake.


# Function Ka Structure

def function_name(parameters):
    # Function ka code yahan likho
    return result  # Ye optional hai


#  def keyword se function banate hain
#  Parentheses () ke andar parameters (optional) hote hain
# return (optional) hota hai, jo function ka result wapas bhejta hai


# Example:

def greet():
    print("Hello, World from python!")


greet()






