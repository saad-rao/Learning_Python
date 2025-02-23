#DATA tYPES IN PYTHON  

# 1.Numeric tYPES

# Python has three main numeric types:
# a.Integer(int)
# b.Floating-point(float)
# c.Complex (complex)

# a.Integer(int)

num_init:int = 20
print(type(num_init), "num_init =",num_init)


# b.Floating-point(float)

num_float: float = 3.14
print(type(num_float), " num_float = ", num_float)  # <class 'float'>


# c.Complex (complex)

num_complex: complex = 2 + 3j
print(type(num_complex), " num_complex = ", num_complex)  # <class 'complex'>


# 2.Boolean type

is_python_fun: bool = True
print(type(is_python_fun), " is_python_fun = ", is_python_fun)  # <class 'bool'>



# 3. Sequence Types
# These store multiple items in an ordered way.

# a. String (str)

python:str="Python"

double_string:str="Hello, World!"
single_string:str='Hello, World!'
single_multi_string:str= f'''Hello,
 World! from {python}'''
double_multi_string:str="""Hello, World!"""

print(type(double_string), " double_string = ", double_string)  # <class 'str'>
print(type(single_string), " single_string = ", single_string)  # <class 'str'>
print(type(single_multi_string), " single_multi_string = ", single_multi_string)  # <class 'str'>
print(type(double_multi_string), " double_multi_string = ", double_multi_string)  # <class 'str'>




# b. List (list)
# An ordered, mutable collection.

my_list:list = [1, 2, 3, "python", 3.14, True]
my_list1:list=[1, 2, 3, "python", .14, 3+4j]

print(type(my_list),"my_list = ",my_list)  # <class 'list'>
print(type(my_list1),"my_list1 = "+str(my_list1))  # <class 'list'>
print(len(my_list))  # 6
print(my_list[3])  # python
print(my_list[-1])  # True
print(my_list[1:3]) # [2, 3]



# c. Tuple (tuple)
# An ordered, immutable collection.

my_Tuple:tuple=(1, 2, 3, "python", 3.14, True)
print(type(my_Tuple),"my_Tuple = ",my_Tuple)  # <class 'tuple'>
print(len(my_Tuple))  # 6