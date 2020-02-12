#T2-6
#到达航班数量变化折线图和出租车供应变化折线图合成的趋势比较

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

f=open("Air_Stat.txt","r")#导入到达航班数据
x_values=[]
y_values=[]
sum=0
for line in f:#存储到达航班数据
    point=line.split()
    x_values.append(int(point[0]))
    y_values.append(2*round(int(point[1])/4,2))
    sum+=int(point[1])

print (round(sum/4,2))

print (x_values)
print (y_values)

plt.plot(x_values, y_values, label='Approach', color='red',linewidth=3)#绘制到达航班折线图
#plt.bar(x_values, y_values)

f=open("Leave_Stat.txt","r")#导入起飞航班数据
x_values=[]
y_values=[]
sum=0
for line in f:#存储起飞航班数据
    point=line.split()
    x_values.append(int(point[0]))
    y_values.append(round(int(point[1])/1,2))
    sum+=int(point[1])

print (round(sum/1,2))

print (x_values)
print (y_values)

plt.plot(x_values, y_values, label='Num of Taxi', color='green',linewidth=3)#绘制起飞航班折线图
#plt.bar(x_values, y_values, width=0.6)

plt.title('Comparation Between Taxi & Approach', fontsize=18)
plt.xlabel('Hour', fontsize=14)

plt.legend()#显示图例标签
plt.grid()#添加网格
plt.show()#显示图像