#T1-4
#时间段和月份共同影响等待接客期望的三维图像

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D#三维绘图工具
import math

h=range(7,30)#7时到次日6时
m=range(1,12)#1月到12月
X=[]
Y=[]
Z=[]

for i in h:
    for j in m:
        X.append(i)
        Y.append(j)
        Z.append((0.1*math.sin(math.cos(0.1*((i-7)-22.5)))+0.88)*(-0.14*math.cos(3.1415/50.0*((-1.29*j*j+17.52*j-39.15)-20))+0.84))#带入公式计算两个因子影响后的概率系数

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')#建立3D模型
ax.plot_trisurf(X,Y,Z,linewidth=0.1, antialiased=True,cmap='rainbow')#勾勒函数值

ax.set_title('Hour & Month & Prob', fontsize=20)#标签设置
ax.set_xlabel('Hour', fontdict={'size': 10, 'color': 'red'})
ax.set_ylabel('Month', fontdict={'size': 10, 'color': 'red'})
ax.set_zlabel('Prob', fontdict={'size': 10, 'color': 'red'})

plt.show()#显示图像