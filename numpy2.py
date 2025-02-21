#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pykernel


# In[3]:


import numpy as np


# In[9]:


list = [1,2,3,4,5,6]
np.array(list)


# In[10]:


list = [5,6,7,8,9]
arr = np.array(list)


# In[11]:


type(arr)


# In[15]:


arr.shape


# In[16]:


np.array([[1,2,3],[4,5,6]])


# In[18]:


array1 = np.array([[1,2,3],[4,5,6]])


# In[19]:


array1.shape


# In[20]:


np.arange(1,30,2)


# In[21]:


np.arange(1,30,3)


# In[26]:


np.arange(1,20,2)


# In[37]:


np.arange(1,20,2).reshape(2,5).shape


# In[40]:


np.arange(20,1,-1)


# In[41]:


np.arange(20,1,-2)


# In[47]:


np.arange(20,1,-3)


# In[52]:


np.linspace(1,20,40).reshape(2,20)


# In[53]:


print(np.random.randn(5,2))


# In[56]:


print(np.random.randint(23,44))


# In[57]:


np.random.randn(123,321)


# In[59]:


np.random.randint(1,20,40)


# In[79]:


np.random.randint(1,100,(4,4))


# In[80]:


array1 = np.random.randint(1,100,20).reshape(5,4)


# In[85]:


array1


# In[87]:


array1 


# In[95]:


array1[0:3]


# In[99]:


array1[0:3,0:3]


# In[120]:


array1[3:5,1:5]


# In[162]:


array1[2:5]

