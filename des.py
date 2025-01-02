'''
name="Pratiksha"
print(f"Name is :{name}")
print(type(name))
caste="Tamang"
print(f"Caste is :{caste}")
print(type(caste))
age=19
print(f"Age is : {age}")
print(type(age))
study="Bachelor"
print(f"Study is : {study}")
print(type(study))
faculty="bsc hons computer science"
print(f"Faculty is : {faculty}")
print(type(faculty))
fruits=[apple , banana , grapes]
print(f"Fruits is : {fruits}")
print(type(fruits))


school="nami"
print(school)


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