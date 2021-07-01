#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib as mp


# In[6]:


import numpy as np


# In[10]:


import sklearn


# In[20]:


#USING VARIABLES
x = 3
print(x)
print(type(x)) #Displayiny the tupe of x i.e. integer


# In[23]:


#USING FOR LOOP
for i in range(0,8):
    print(i) #printing numbers from 0-7
print("New is i", i) #out of for loop


# In[27]:


#USING IF LOOP
n = int(input())
#Determining  whether the number is odd or even
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")


# In[48]:


#USING OPERATORS
x = int(input())
y = int(input())

print("1. Addition:", end = " ")
print(x+y)
print("2. Subtraction", end = " ")
print(x-y)
print("3. Multiplication:", end = " ")
print(x*y)
print("4. Division:", end = " ")
print(x/y)


# In[ ]:





# In[49]:


#list creation and printing of list

thislist = ["apple", "banana", "cherry"]

print(thislist)


# In[52]:


#prints the length of list
print(len(thislist))
#prints the type of list
print(type(thislist))


# In[55]:


#tuple creation and printing tuple, its size and type

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))


# In[56]:


#defining a string

str = " Ruchir "
print(str)


# In[58]:


#string concatenation

str2 = "is a boy"
print(str+str2)


# In[59]:


print(str[3])

