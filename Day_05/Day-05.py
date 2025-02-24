# Practice Questions

# QS:1 Write a program to input two numbers and print their sum.

input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))

sum = input1 + input2
print("Sum of the two numbers is : ", sum)


# QS:2 Write a program to input side of square and print it's area.

square_input = float(input("Enter the side of the square: "))
area = int( square_input * square_input)
print("Area of the square is: ", area)


# QS:3 Write a program to input 2 floating point numbers and print their average.

input1 = float(input("Enter the first number: "))
input2 = float(input("Enter a second number : "))

average = (input1 + input2) / 2
print("Average of the two numbers is: ", average)



# QS:4 Write a program to input a two integers a and b and 
# print true if value of a is greater than or equal to value of b, otherwise print false.

input1 = input("Enter the first number: ")
input2 = input("Enter the second number: ")

print(input1 >= input2)