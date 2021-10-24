#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2.Write a Python program to get the Python version you are using
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[2]:


#3.Write a Python program to display the current date and time.
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[3]:


#9.Write a program which print the length of the list?
l=[11,22,33,44,55,66]

#printing the length using len()
print("The length of the list",l, "is :",len(l))


# In[ ]:


#4.Write a Python program which accepts the radius of a circle from the user and compute
the area.
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[ ]:


#8.Write a program which take input from user and identify that the given number is even or odd

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))


# In[ ]:


#10.Write a Python program to sum all the numeric items in a list?
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


# In[ ]:


#11.Write a Python program to get the largest number from a numeric list.
list1 = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)
    print("Largest element is:", max(list1))


# In[ ]:


#1.Write a Python program to print the following string in a specific format (see theoutput).

#Twinkle, twinkle, little star,
#How I wonder what you are!
#Up above the world so high,
#Like a diamond in the sky.

#Twinkle, twinkle, little star,
#How I wonder what you are
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# In[ ]:


#5.Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[ ]:


#6.Write a python program which takes two inputs from user and print them addition
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[ ]:


#7.Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades ?
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")


# In[ ]:


#12Take a list, say for example this one:a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] Write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:

    if i < 5:

        print(i)

