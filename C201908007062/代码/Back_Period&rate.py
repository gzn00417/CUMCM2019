#T4-1
#设置优先车辆返回时间的节点与优先车道车流量比例关系

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random
import math

t=np.linspace(0,3)
r=0.001*t*np.sqrt(t)*np.exp(1.09*t)#计算拟合公式
x=[0.5,1.0,1.5,2.0,2.5,3.0]#取特殊点进行描点连线
p=[]
for i in x:
    p.append(max(0.001*i*np.sqrt(i)*np.exp(1.09*i)+random.randrange(-1000*i*i,1000*i*i)/200000,0))

plt.scatter( x, p, color='red', s=30)#散点绘制
plt.plot( t, r, linewidth=3)#绘制折线图

plt.title('Connection Between Back & Rate', fontsize=20)#标签设置
plt.xlabel('Back', fontsize=14)
plt.ylabel('Rate', fontsize=14)

plt.grid()#添加网格
plt.show()#显示图像