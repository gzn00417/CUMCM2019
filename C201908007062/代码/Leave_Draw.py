#T2-4
#起飞航班在时间上的数量分布曲线

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

f=open("Leave_Stat.txt","r")#读入起飞航班数据
x_values=[]
y_values=[]
sum=0
for line in f:#存储数据
    point=line.split()
    x_values.append(int(point[0]))
    y_values.append(round(int(point[1])/1,2))
    sum+=int(point[1])

print (round(sum/1,2))

print (x_values)
print (y_values)

plt.plot(x_values, y_values, color='black',linewidth=3)#绘制折线图
plt.bar(x_values, y_values, width=0.6)#绘制柱形图

plt.title('Connection Between Time & Leave', fontsize=20)#标签设置
plt.xlabel('Hour X 2', fontsize=14)
plt.ylabel('Leave', fontsize=14)

plt.grid()#添加网格
plt.show()#显示图像