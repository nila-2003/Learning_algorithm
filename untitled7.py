# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VcTTvklU72bo7DcDy_hLx0EIGLxXTbFy
"""

import numpy as np
import matplotlib.pyplot as plt
#getting random data sets
#features
x=3*np.random.rand(100,1)# 3 denotes the last limit on x axis
#equation
y=9 + 2*x+np.random.rand(100,1)#starts from 9 and difference is 2
#scatter pplot
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x vs y')
plt.figure(figsize=(15,25))