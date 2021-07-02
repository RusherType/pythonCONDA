#!/usr/bin/env python
# coding: utf-8

# # CUREYA TASK1
#       Implementing for,if,operators and variables

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


# In[1]:


a = 33
b = 33
if b < a:
    print("B is less than A")
elif a == b:
    print("A and B are equal")


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


# # *LISTS

# In[49]:


#list creation and printing of list

thislist = ["apple", "banana", "cherry"]

print(thislist)


# In[52]:


#prints the length of list
print(len(thislist))
#prints the type of list
print(type(thislist))


# # *TUPLES

# In[55]:


#tuple creation and printing tuple, its size and type

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))


# # *STRINGS

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


# 
# # INSTALLING PANDAS,NUMPY,MATPLOTLIB

# In[4]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install numpy')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install sklearn')


# # *NUMPY

# In[5]:


# importing numpy package
import numpy as np
  
# creating two matrices
p = [[13, 11], [9, 7]]
q = [[9, 1], [6, 5]]
print("Matrix p :")
print(p)
print("Matrix q :")
print(q)
  
# product of 2 matrices
op = np.multiply(p, q)
  
# printing the output
print("The matrix multiplication is :")
print(op)


# In[1]:


# Python program to inverse
# a matrix using numpy
  
# Import required package
import numpy as np
  
# Taking a 3 * 3 matrix
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
  
# Calculating the inverse of the matrix
print(np.linalg.inv(A))


# In[3]:


# Subtracting elements of the matrix
# importing numpy package
import numpy as np
  
# creating two matrices
p = [[21, 17], [19, 37]]
q = [[22, 13], [26, 25]]
print("Matrix p :")
print(p)
print("Matrix q :")
print(q)
  
# product of 2 matrices
op = np.subtract(p, q)
  
# printing the output
print("The matrix subtracted is :")
print(op)


# # *PANDAS

# In[1]:


# Importing the library
import pandas as pd
 
print("All the marks are out of 30")
# inserting data into the list.
data = {'Subject':['Maths', 'SST', 'Science'],
        'Marks':[20, 21, 19]}
 
dataFrame = pd.DataFrame(data)
 
print(dataFrame)


# In[2]:



# import pandas library
import pandas as pd  
      
# List initialization  
list = [['bat', 650], ['racket', 1000], 
       ['football', 800], ['basketball', 700]] 
  
# creating df object with columns specified    
df = pd.DataFrame(list, columns =['item', 'price']) 
print(df )


# # *MATPLOTLIB

# In[17]:


import matplotlib.pyplot as plt
 
plt.bar([0.15,1.5,2.05,3.65,4.75],[75,50,70,48,80],
label="Fruit",color='r', width = 0.2)
plt.bar([.75,1.75,2.75,3.5,4.5],[73,19,31,53,56],
label="Arora lemon", color='g',width=.2)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Consumption(L)')
plt.title('Survey')
plt.show()


# In[22]:


import matplotlib.pyplot as plt

slices = [12,25,50,36]
activities = ['Prescription drugs','clinical services','hospital services','other services']
cols = ['c','m','r','g']
plt.pie(slices,
labels=activities,
colors=cols,
startangle=90,
shadow= True,
explode=(0,0.1,0,0),
autopct='%1.1f%%')
plt.title('Pie Plot')
plt.show()

