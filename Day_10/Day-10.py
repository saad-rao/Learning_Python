                     # Practice questions 

# Write a program to input user name and print it's length.

user_name:str = input("Enter your name: ") 
user_name = len(user_name)
print(user_name)


# Write a program to find the occurence of '$' in a string.

string : str = "Hello$World$"
print(string.count("$"))



# Write a program of traffic light using if-elif-else.

light = input("Enter the color of traffic light: ")
if(light =="Red"):
    print("stop")

elif(light == "yellow"):
    print("wait")

elif(light == "green"):
    print("go")

elif(light == "off"):
    print("no signal")

else:
    print("Invalid color")


# Write a program to check whether a number is even or odd.

num:int = int(input("Enter a number: "))
if(num%2 == 0):
    print("Even")
elif(num%2 == 1):
    print("Odd")

else:
    print("Invalid number")    



# Write a program to check whether a number is greater than.

a:int = int(input("Enter a first number  : "))
b:int = int(input("Enter a second number : "))
c:int = int(input("Enter a third number  : "))

if(a>=b and a>=c):
    print("First number is greater", a)

elif(b>=c):
    print("Second number is greater",b)

else:
    print("Third is the greater",c)


# Write a program to check if a number is a multiple of 7 or not

number:int = int(input("Enter a number : "))

if(number%7==0):
    print(number,"is multiple of 7")
else:
    print(number,"is not a multiple of 7")