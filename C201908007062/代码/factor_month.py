#T1-3
#不同月份月份通过气温变化对于等待接客期望的间接性贡献

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

m=np.linspace(1,12)#自变量12个月
x=-1.29*m*m+17.52*m-39.15#月份与平均气温对应公式
y=-0.14*np.cos(3.1415/50.0*(x-20))+0.84#平均气温与概率系数对应公式

plt.plot(x, y, linewidth=3)#绘制散点图

plt.title('Connection Between Temp & Prob', fontsize=20)#标签设置
plt.xlabel('Temp', fontsize=14)
plt.ylabel('Prob', fontsize=14)

plt.grid()#添加网格
plt.show()#显示图像