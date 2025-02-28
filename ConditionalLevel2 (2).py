 
a = int(input("Enter first number: "))   
b = int(input("Enter second number: "))   
c = int(input("Enter third number: "))   
if a >= b and a >= c:   
    print("Largest:", a)   
elif b >= a and b >= c:   
    print("Largest:", b)   
else:   
    print("Largest:", c)  

##=============================================================================================================
# 
#22. Determine if a number is a prime number 
num = int(input("Enter a number: "))   
if num > 1:   
    for i in range(2, int(num**0.5) + 1):   
        if num % i == 0:   
            print("Not a prime number")   
            break   
    else:   
        print("Prime number")   
else:   
    print("Not a prime number")   

#==================================================================================================================
# 
#   23. Check if a person is eligible for a driving license 
age = int(input("Enter age: "))   
passed_test = input("Did you pass the driving test? (yes/no): ").lower()   
if age >= 18 and passed_test == "yes":   
    print("Eligible for a driving license")   
else:   
    print("Not eligible")   
 
 
 #==================================================================================================
 
 
#  24. Determine if a triangle is equilateral, isosceles, or scalene 
a = int(input("Enter first side: "))   
b = int(input("Enter second side: "))   
c = int(input("Enter third side: "))   
if a == b == c:   
    print("Equilateral Triangle")   
elif a == b or b == c or a == c:   
    print("Isosceles Triangle")   
else:   
    print("Scalene Triangle")  
    
#=====================================================================================================================
# 
#   25. Determine if a student passes or fails 
marks = int(input("Enter marks: "))   
if marks >= 40:   
    print("Pass")   
else:   
    print("Fail")   
 
#====================================================================================================================
# 
# 26. Check if a number is a palindrome 
num = input("Enter a number: ")   # same input and out put 121,mum
if num == num[::-1]:   
    print("Palindrome")   
else:   
    print("Not a Palindrome")  

#===========================================================================================================     
 
#27. Calculate electricity bill 
units = int(input("Enter electricity units consumed: "))   
if units <= 100:   
    bill = units * 5   
elif units <= 300:   
    bill = (100 * 5) + (units - 100) * 10   
else:   
    bill = (100 * 5) + (200 * 10) + (units - 300) * 15   
print("Total Bill: ₹", bill)   

#==========================================================================================================
 
#28. Find the grade of a student 
marks = int(input("Enter marks: "))   
if marks >= 90:   
    print("Grade: A")   
elif marks >= 80:   
    print("Grade: B")   
elif marks >= 70:   
    print("Grade: C")   
elif marks >= 60:   
    print("Grade: D")   
elif marks >= 40:   
    print("Grade: E")   
else:   
    print("Grade: F (Fail)")   
 
#================================================================================================================ 
#29. Determine if a given date is valid 
import calendar   
day = int(input("Enter day: "))   
month = int(input("Enter month: "))   
year = int(input("Enter year: "))   
if 1 <= month <= 12 and 1 <= day <= calendar.monthrange(year, month)[1]:   
    print("Valid date")   
else:   
    print("Invalid date")  

#=========================================================================================================== 
# 
# 30. Check if a given time is AM or PM 
hour = int(input("Enter hour (24-hour format): "))   
if hour < 12:   
    print("AM")   
else:   
    print("PM")   
#==============================================================================================================
#31. Check if a number is an Armstrong number 
num = input("Enter a number: ")   
power = len(num)   
if sum(int(digit) ** power for digit in num) == int(num):   
    print("Armstrong Number")   
else:   
    print("Not an Armstrong Number")   
#=======================================================================================================
#32. Determine the type of quadrilateral 
a = int(input("Enter first side: "))   
b = int(input("Enter second side: "))   
c = int(input("Enter third side: "))   
d = int(input("Enter fourth side: "))   
if a == b == c == d:   
    print("Square")   
elif a == c and b == d:   
    print("Rectangle")   
else:   
    print("Other Quadrilateral")   
 
33. Implement a basic calculator 
a = float(input("Enter first number: "))   
b = float(input("Enter second number: "))   
op = input("Enter operation (+, -, *, /): ")   
if op == "+":   
    print("Result:", a + b)   
elif op == "-":   
    print("Result:", a - b)   
elif op == "*":   
    print("Result:", a * b)   
elif op == "/":   
    print("Result:", a / b)   
else:   
    print("Invalid operation")   
 
34. Check if a bank account balance is sufficient for withdrawal 
balance = float(input("Enter account balance: "))   
withdraw = float(input("Enter withdrawal amount: "))   
if balance >= withdraw:   
    print("Withdrawal successful")   
else:   
    print("Insufficient funds")   
   