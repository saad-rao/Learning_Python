# Control Flow and Decision Making in Python

# Control flow is the ordered in which statements are executed in a program. 
# Python's decision-making syntax includes if, Elif, and else statements, 
# as well as comparison and logical operators.



# Control flow is the ordered in which statements are executed in a program.
# Python's decision-making syntax includes if, Elif, and else statements, 
# as well as comparison and logical operators.

#  Logical Operators:

# Logical operators combine multiple conditions:

# and (True if both conditions are True)
# or (True if at least one condition is True)
# not (reverses the result of a condition)

age = 20;
is_student = True;

if age > 18 and is_student:
    print("You are a student and you are eligible for student discount.")

    if age < 12 or age > 60:
        print("You are eligible for discount.")

        if not is_student:
            print("You are not a student.")
else:
    print("You are not eligible for student discount.")



# The if Statement:
# The if statement is used to execute a block of code only if a condition is True.


# Example Code:

num:int = 10;

if num > 0:
    print("The number is positive.")

    if num < 0:
        print("The number is negative.")

        if num == 0:
            print("The number is zero.")


# The elif Statement:

# The elif statement is used to check multiple conditions. It stands for "else if."

# Example Code:


