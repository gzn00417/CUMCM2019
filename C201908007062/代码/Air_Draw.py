#T2-3

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

f=open("Air_Stat.txt","r")#读入降落飞机数据文件
x_values=[]
y_values=[]
sum=0
for line in f:#存储数据
    point=line.split()
    x_values.append(int(point[0]))
    y_values.append(round(int(point[1])/4,2))
    sum+=int(point[1])

print (round(sum/4,2))#平均每日降落航班数量

print (x_values)
print (y_values)

plt.plot(x_values, y_values, color='black',linewidth=3)#绘制折线图
plt.bar(x_values, y_values)#绘制柱形图

plt.title('Connection Between Time & Airline', fontsize=20)#标签设置
plt.xlabel('Hour', fontsize=14)
plt.ylabel('Flights', fontsize=14)

plt.grid()#添加网格
plt.show()#显示图像