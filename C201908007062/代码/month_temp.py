#T1-2
#平均气温关于月份的函数拟合

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq#最小二乘法拟合函数库

# 待拟合的数据
f=open("temp_avg.txt","r")#导入每月平均气温数据
x=[]
y=[]
for line in f:
    a=line.split()
    x.append(float(a[0]))
    y.append(float(a[1]))
    
X = np.array(x)#标准化存储数据
Y = np.array(y)


# 二次函数的标准形式
def func(params, x):
    a, b, c = params
    return a * x * x + b * x + c


# 误差函数，即拟合曲线所求的值与实际值的差
def error(params, x, y):
    return func(params, x) - y


# 对参数求解
def slovePara():
    p0 = [10, 10, 10]

    Para = leastsq(error, p0, args=(X, Y))
    return Para


# 输出最后的结果
def solution():
    Para = slovePara()
    a, b, c = Para[0]
    print ("a=",a," b=",b," c=",c)
    print ("cost:" + str(Para[1]))
    print ("求解的曲线是:")
    print ("y="+str(round(a,2))+"x*x+"+str(round(b,2))+"x+"+str(c))

    plt.figure(figsize=(8,6))
    plt.scatter(X, Y, color="green", label="sample data", linewidth=2)

    #   画拟合直线
    x=np.linspace(1,12,100) ##在0-15直接画100个连续点
    y=a*x*x+b*x+c ##函数式
    plt.plot(x,y,color="red",label="solution line",linewidth=2)
    plt.legend() #绘制图例
    plt.title('Connection Between Month & Temp', fontsize=20)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Temp', fontsize=14)
    plt.grid()
    plt.show()


solution()