'''# Write a program to print area of rectangle.
side1 =int(input("Enter length : "))
side2 = int(input("Enter breadth : "))
area = side1 * side2
print(f"The area of rectangle is : {area:}.")

# Write a program to print area of circle.
import math # To use math.pi for the value of Pi
radius = float(input("Enter the radius of the circle : "))
circlearea = math.pi * radius * radius
print(f"The area of circle is : {circlearea:.2f}")


#Write a program to print area of square.
l = int(input("Enter length : "))
area = l*l
print(f"The area of square is : {area:}.")

#write a program to print perimeter of rectangle.
side1 = int(input("Enter length : "))
side2 = int(input("Enter breadth : "))
rect = 2*(side1 + side2)
print(f"The perimeter of rectangle is : {rect}")

# Write a program to print perimeter of square.
length =int(input("Enter Length :"))
sq = 4 * length
print(f"The perimeter of square is : {sq}.")

# Write a program t0 find simple interest.
P = float(input("Enter principle amount :"))
T = float(input("Enter time :"))
R = float(input("Enter rate :"))
SI = P * T * R /100
print(f"The simple interest amount is : {SI}.")

# Write a program to find average of three numbers.

f = float(input("Enter first number :"))
s = float(input("Enter second number :"))
t = float(input("Enter third number :"))
Avg = (f + s + t ) / 3
print(f"The average of three number is :{Avg}.")

# Write a program to convert kilometer into meter.
km = int(input("Enter distance in kilometer :"))
m = km * 1000
print(f"The distance in meter is :{m}.") 

 # Write a program to convert metr into kilometer.
m = float(input("Enter distane in meter :"))
km = m /1000
print(f"The distance in kilometer is :{km}.")

# write a program to convert paisa into rupees.
ps = int(input("Enter the amount in paisa :"))
rs = ps / 100
print(f"The amount is :{rs}.")

# Wrire a program to check whether a number is positive or negative.
num = int(input("Enter any number :"))
if ( num > 2):
  print(f"The number is positive :{num}.")
else:
  print(f"The number is negative :{num}.")

# Write a program to check if they are pass or fail.
Marks = int(input("Enter marks in a subject :"))
if ( Marks >= 40):
  print(f"The result is pass :{Marks}.")
else:
 print(f"The result is fail :{Marks}.")
 
# Write a program to find the greatest of two numbers.
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
if ("num1 > num2"):
    print(f"The greatest number is :{num1}.")
else:
    print(f"The greatest number is :{num2}.") 
    
# Write a program to check whether a number is exactly divisible by 5 or not.

num = int(input("Enter a number :"))
if num % 5 == 0:
    print(f"The number is exactly divisible by 5.")
else:
    print(f"The number is not divisible by 5.") 
    
# Write a program to check eligibility to vote or not.
age = int(input("Enter your age : "))
if age >= 18:
    print("You are eligible for vote.")
else:
    print("You are not eligible for vote.")
    

# write a program to find child,senior,adult, and teenager.
age = int(input("Enter your real age : "))
if age <= 13:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
elif 20 <= age <= 59:
    print("You are an adult.")
else:
    print("You are a senior.")
    
# write a program to find greatest of three numbers.
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
num3 = float(input("Enter third number :"))

if num1 > num2 and num1 > num3:
    print(f"The greatest number is: {num1}.")
elif num2 > num1 and num2 > num3:
    print(f"The greatest number is : {num2}.")
elif num3 > num1 and num3 > num2:
    print(f"The greatest number is : {num3}.")
else:
    print("Two or more numbers are equal and the greatest.") 
# Write a program to check whether a number is multiple of 10 or not.

num = int(input("Enter a number :"))
if (num % 10 ==0):
    print(f"{num} is multiple of 10.")
else:
    print(f"{num} is not a multiple of 10.")'''

    # check leap year
year = int(input("Enter a year :"))
if (year % 400 == 0) and (year % 100 ==0):
    print(f"{year} is a leap year.")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")