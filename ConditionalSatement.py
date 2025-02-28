# To create a class, use the keyword class:
import math


class MyClass:
 x = 5
# print(x)
#=====================================================================================================
# Now we can use the class named MyClass to create objects:
#Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

#Check if a number is even or odd 
num = 8
if num % 2 == 0:   
    print("Even")   
else:   
    print("Odd")  
#======================================================================================================
  # 2. Check if a person is eligible to vote (age 18 or above) 

# age = int(input("Enter age:+" ))   
age=23
if age >= 18:  
    print("Eligible to vote")   
else:   
    print("Not eligible to vote")    
#========================================================================================================
  #  3. Determine if a given year is a leap year or not 
year = int(input("Enter the Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
    print("Leap Year")
else:
   print("Not a Leap Year")

#=======================================================================================================
 
 # 4. Check if a number is positive, negative, or zero
num=int(input("Enter number: "))
if num > 0:
   print("Possitive number")
else:
    print("Negative Number")
num=int(input("enter num: "))
if num > 0:
    print("Possitive number")
elif num > 0:
    print("Negative Number")
else:
    print("Zero")
#===========================================================================================================
#  5. Write a program to find the greatest of two numbers 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a>b:
    print("Greatest: a,")
else:
    print("Greatest: b,")
    
#================================================================================================================

#    6. Determine if a number is a multiple of 5 
num = int(input("Enter anumber :" ))
if num%5==0:
    print("multipule of 5")
else:
    print("not multipule 5 ")

#=======================================================================================================
#. Check if a character is a vowel or consonant 
char = input("enter a charecter: ").lower()
if char in 'aeiou':
    print("vowel")
else:
    print("consonant")

#==================================================================================================

#8. Determine if a person is eligible for a senior citizen discount (age 60+) 
age = int(input("ENTER age:"))

if age>=60:
    print("Eligibule for senier citizen discount ")
else:
    print("Not eligible ")

#================================================================================================

# 9. Check if a number is a single-digit number #

num=int(input("Enter the num digit :"))

if 0<=abs(num)<10:
    print("single digit number")
else:
    print("duble digite")

#====================================================================================================

# 10. Print "Good Morning" if the time is before 12 PM, otherwise print "Good Afternoon"

hour = int(input("enter hour(24 hour format): "))

if hour<=12:
    print("Good Morning")
else:
    print("Good Afternoon")

#=========================================================================================================
#11. Check if a string is empty or not      

s = input("Enter a string: ")   
if not s:   
    print("String is empty")   
else:   
    print("String is not empty")  

#========================================================================================================
num =int(input("Enter the number: "))

if math.isqrt(num) ** 2 == num:
      
      print("Perfect Square")   
else:   
    print("Not a perfect square")  


 #===========================================================================================================
 #13. Determine if a number is between 1 and 100 
num = int(input("Enter a number: "))   
if 1 <= num <= 100:   
    print("Within range")   
else:   
    print("Out of range")  

#=======================================================================================================
# 14. Print "Weekend" if the day is Saturday or Sunday; otherwise, print "Weekday" 
day = input("Enter a day: ").lower()   
if day in ["saturday", "sunday"]:   
    print("Weekend")   
else:   
    print("Weekday")   

#==============================================================================================================

#15. Find if a given number is exactly divisible by  both 3 and 7   

num = int(input("Enter a number: "))   
if num % 3 == 0 and num % 7 == 0:   
    print("Divisible by 3 and 7")   
else:   
    print("Not divisible by both")   

#==========================================================================================================
# 
#   16. Check if the sum of two numbers is greater than 100 
a = int(input("Enter first number: "))   
b = int(input("Enter second number: "))   
if (a + b) > 100:   
    print("Sum is greater than 100")   
else:   
    print("Sum is 100 or less") 

#============================================================================================================
# 
# 17. Write a program to find the minimum of two numbers 
a = int(input("Enter first number: "))   
b = int(input("Enter second number: "))   
if a < b:   
    print("Minimum:a",+ a)   
else:   
    print("Minimum:", b)   
      
 
   