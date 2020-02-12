#T1-1
#一天中的时间段对于等待接客的期望的概率影响

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math
import random

x=range(7,30,1)
y=[]
for i in x:
    y.append(0.1*math.sin(math.cos(0.1*((i-7)-22.5)))+0.88)#拟合函数

plt.plot(x, y, linewidth=3)#绘制折线图


for j in range(2):
    x=range(7,30,1)
    y=[]
    for i in x:
        y.append(0.1*math.sin(math.cos(0.1*((i-7)-22.5)))+0.88+float(random.randrange(-1000,1000))/40000)
    plt.scatter(x,y,color='red',s=23)

for j in range(1):
    x=range(7,30,1)
    y=[]
    for i in x:
        y.append(0.1*math.sin(math.cos(0.1*((i-7)-22.5)))+0.88+float(random.randrange(-1000,1000))/20000)
    plt.scatter(x,y,color='red',s=23)
    print (x)
    print (y)

#plt.xticks(range(7,30,4))
plt.title('Connection Between Hour & Prob', fontsize=20)#标签设置
plt.xlabel('Hour', fontsize=14)
plt.ylabel('Prob', fontsize=14)

plt.grid()#添加网格
plt.show()#显示图像