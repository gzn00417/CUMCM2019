#T4-2
#优先出租车比率和期望增加系数的函数关系

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
'''
t=np.linspace(0,3)
r=0.001*t*np.sqrt(t)*np.exp(0.9*t)
'''
r=np.linspace(0,1)#设置0%-100%散点
t0=120#导入常数
w=35/3600
s=150
k=90
x=1.0*k*t0*w/s
a=-x*r+x+1#计算函数

plt.plot(np.linspace(0,1), a, linewidth=3)#绘制折线图

plt.title('Connection Between Rate & Alpha', fontsize=20)#标签设置
plt.xlabel('Rate', fontsize=14)
plt.ylabel('Alpha', fontsize=14)

plt.grid()#添加网格
plt.show()#显示图像