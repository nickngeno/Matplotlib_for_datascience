#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import the necessary modules and libraries to use in plotting our graphs
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import random


# In[2]:


# use dummy data x,y dataset and use plt to plot the line graph
x=[1,2,3,4,5]
y=[4,5,6,8,10]

# adding title and lables
plt.figure(figsize=(15,10))
plt.plot(x,y,"r^")
plt.title("My first Plt graph")
plt.xlabel("Xlabel")
plt.ylabel("Ylabel")
plt.show()


# In[3]:


# multiple plots per figure
x=[1,2,3,4,5]
y=[4,5,6,8,10]

# adding title and lables
# plt.figure(figsize=(15,10))
plt.subplot(1,2,1)
plt.plot(x,y,"r^")
plt.title("Sub one")
plt.ylabel("Ylabel")
plt.xlabel("Xlabel")


plt.subplot(1,2,2)
plt.plot(x,y,"b^")
plt.title("Sub Two")

# plt.ylabel("Ylabel")

plt.suptitle("My first Plt graph")
plt.ylabel("Ylabel")
plt.xlabel("Xlabel")
plt.show()


# In[4]:


# multiple plots per figure
# implememtinmg subplots usinmg fig and ax(axis)
x=[1,2,3,4,5]
y=[4,5,6,8,10]

fig,ax=plt.subplots(ncols=2,nrows=2,figsize=(6,6))
ax[0,1].plot(x,y,"go")
ax[1,0].plot(x,y,"r^")
ax[0,1].set_title("plot 0 1")
ax[1,0].set_title("plot 1 0")
ax[1,0].set_xlabel("y 1,0")
ax[1,1].set_xlabel("x 1 1")


# In[5]:


# creating a bar graph using pyplot
divisions=["Div-A","Div-B","Div-C","Div-D","Div-E"]
divisions_score=[10,20,35,24,35]
plt.bar(divisions,divisions_score,color="green")
plt.title("Bar Graph")
plt.xlabel="Divisions"
plt.ylabel="Division_scores"
plt.show()


# In[3]:


# creating horizontal bar graphs
# xerr and yerr is used to show variance
divisions=["Div-A","Div-B","Div-C","Div-D","Div-E"]
divisions_score=[10,20,35,24,35]
variance=[1,2,3,2,1]
plt.barh(divisions,divisions_score,xerr=variance,color="green")
plt.title("Bar Graph")
plt.xlabel("Divisions")
plt.ylabel("Division_scores")
plt.show()


# In[4]:


# creating horizontally stacked bar graphs
divisions=["Div-A","Div-B","Div-C","Div-D","Div-E"]
divisions_score=[10,20,35,24,35]
boys_average=[7,18,30,15,30]

index=np.arange(5)
width=0.30

plt.bar(divisions,divisions_score,width,color="green",label="divisions_score")
plt.bar(index+width,boys_average,width,color="blue",label="Boys_average")
plt.title('Horizontally stacked bar graphs')

plt.xlabel("Divisions")
plt.ylabel("Division score")

plt.xticks(index + width/2,divisions)
plt.legend(loc='best')
plt.show()


# In[8]:


# vertically stacked bargraph
divisions=["Div-A","Div-B","Div-C","Div-D","Div-E"]
divisions_score=[10,20,35,24,35]
boys_average=[7,18,30,15,30]

index=np.arange(5)
width=0.30

plt.bar(index,divisions_score,width,color="green",label="divisions_score")
plt.bar(index,boys_average,width,color="blue",label="Boys_average" ,bottom=divisions_score)
plt.title("Vertically stacked bar graphs")

plt.xlabel("Divisions")
plt.ylabel("Division score")

plt.xticks(index,divisions)
plt.legend(loc='best')
plt.show()


# In[9]:


# pie charts
divisions=["Div-A","Div-B","Div-C","Div-D","Div-E"]
divisions_score=[10,20,35,24,35]
Explode=[0,0.1,0,0,0]

plt.pie(divisions_score,labels=divisions,explode=Explode,shadow=True,startangle=45)
plt.axis("equal")
plt.legend(title="List of Divisions",loc='upper right')
plt.show()


# In[6]:


# plotting an histogram.Histogram is a commonly used graph when plotting variables in a certain range against its frequencies

random_value=np.random.randn(1000)
plt.title("Histogram Example")
plt.xlabel("Random number")
plt.ylabel("Frequency")
# plt.xlabel('Plot Number')
# plt.ylabel('Important var')

random_value
plt.hist(random_value,10)

plt.show()


# In[10]:


# creating scatter plots and 3d plotting

# scatter is very useful especially when visualizing in terms of regressions

height=np.array([167,170,149,165,155,180,166,146,159,185,145,168,172,181,169])
weight=np.array([86,74,66,78,68,79,90,73,70,88,66,84,67,84,77])

plt.xlim(140,200)
plt.ylim(60,100)
plt.scatter(height,weight)
plt.title("Scatter plot")
plt.xlabel("Height")
plt.ylabel("weight")

plt.show()


# In[12]:


# 3d visualization
# we need to import the module mplot3d

from mpl_toolkits import mplot3d

ax=plt.axes(projection="3d")
ax.scatter3D(height,weight)
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
ax.set_title("3D plotting")
plt.show()


# In[13]:


# we can create 3D graph eg line graph as well
# instead of 3d scatter3D, we use plot

ax=plt.axes(projection="3d")
ax.plot3D(height,weight)
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
ax.set_title("3D plotting")
plt.show()

