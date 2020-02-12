#T2-5
#运用已经整理、补全的起飞航班数据构造关于预测实时出租车数量模型

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

f=open("Leave_Stat.txt","r")#读入起飞飞机数据
x_values=[]
y_values=[]
sum=0
for line in f:#存储数据
    point=line.split()
    x_values.append(int(point[0]))
    y_values.append(round(int(point[1])/1,2))
    sum+=int(point[1])

print (round(sum/1,2))#计算平均值

print (x_values)
print (y_values)

plt.plot(x_values, y_values, color='black',linewidth=3)#绘制折线图
plt.bar(x_values, y_values, width=0.6)#绘制柱形图

plt.title('Forecast of Taxi', fontsize=20)#标签设置
plt.xlabel('Hour X 2', fontsize=14)
plt.ylabel('Num', fontsize=14)

plt.grid()#添加网格
plt.show()#显示图像