# write a program to add two numbers'.
'''
num1=5
num2=4
add=num1+num2
print(f"The sum of two number is : {add}")

a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=a+b
print(f"Added number is :{c}") '''
'''
# write a area of rectangle.
l=5
b=4
Area=l*b
print(f"Area of rectangle is :{Area}")'''
'''
# write a program of area of circle.
import math # To use math.pi for the value of Pi
#Input values
radius = float(input("Enter the radius of the circle: "))
circlearea = math.pi * radius * radius
print(f"The area of circle is : {circlearea : .2f}")
'''
'''
# Input number from the user.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} ia an odd number.")
    '''
'''
#Input score from the user.
score = float(input("Enter your score: "))
 # Check the grade
if score >= 90:
     print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
   print("Grade: F")
   '''
#Input temperature from the user
temp_celsius = float(input("Enter temperature in Celsius: "))
 
#Convert to fahrenheit
temp_fahrenheit = (temp_celsius * 9/5) + 32

#Print the result
print(f"{temp_celsius} degree celsius is eqal to {temp_fahrenheit} degree fahrenheit .")
