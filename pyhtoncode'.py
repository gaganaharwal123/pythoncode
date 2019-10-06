# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:44:45 2019

@author: gagan agarwal
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# dice in eange of 1 to 6
import random as rd
dice=rd.randint(1,6)
print(dice)


#rock paper and cizer
rd.choices(["rock","paper","cizer"])


#WAP to count no. of words in a sentance
myStr=input("enter the sentance>")
count=myStr.split()
print(len(count))

#print(len(input(">").split()))


#wap  to clean the messy salary
salary='$876,001'
slic=salary[1:4]+salary[5:8]
salary=int(slic)
print(salary)

salary='$876,001'
stri=salary[1:]
s1=stri.split(',')
s2=''.join(s1)
print(int(s2))

#wap to take input from user
imp=input("enter blank for exit>")
lis=[imp]
while (True):
    imp=input("enter blank for exit>")
    if (imp == ' ' or imp == '' ):
        print(lis)
        break
    lis.append(imp)


#wap remove all three from list
import pdb
some_list=[1,2,3,5,6,2,4,3,5,6,7,8,1,2,3]
for x in some_list:
    if(x==3):
        some_list.remove(x)
    pdb.set_trace()
print(some_list)


#clear the messy salary
salary=['$876,001','$543,903','$2453,896']
s3=[]
for x in salary:
    sub_salary = x
    s3.append(''.join(sub_salary[1:].split(',')))
print(s3)


#remove the breakword
str1="this is good"
stp=["this","is"]
str2=str1.split(" ")
list2=[]
for x in str2:
    if x not in stp:
        list2.append(x)
str1="".join(list2)
str1

#
stste_name=['alabama','california','oklahoma','florida']
vol=['a','e','i','o','u']
st=[]
for x in stste_name:
    sub_salary = x
    sub_salary








