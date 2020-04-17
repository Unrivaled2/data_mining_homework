#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.pylab import *

"""
2020春学期中国地质大学（武汉）数据挖掘课程
作业2的代码

作者：李静涛
qq：2079624548
"""

mpl.rcParams["font.sans-serif"] = ['SimHei']

def normfun(x,mu,sigma):
    """
    计算标准正态分布的概率密度
    :param x: 样本点
    :param mu: 均值
    :param sigma: 标准差
    :return: 计算出来的概率密度
    """
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf

if __name__ == "__main__":
    x = [] 
    with open("./iris.txt",'r') as f:
        line = f.readline()
        while line:
            #print(line)
            res = line.split(",")
            x.append(float(res[0]))
            line = f.readline()
        f.close()

    mean = np.mean(x)
    std = np.std(x)
    print("均值： " + str(mean))
    print("标准差： " + str(std))

    # 设定 x 轴前两个数字是 X 轴的开始和结束，第三个数字表示步长，或者区间的间隔长度
    x = np.arange(1, 10, 0.1)
    # 设定 y 轴，载入刚才的正态分布函数
    y = normfun(x, mean, std)
    plt.plot(x, y)

    plt.title('norm distribution with mean = ' + str(mean)[0:6]+ ", var = " + str(std*std)[0:6])
    plt.xlabel('x')
    plt.ylabel('Probability')
    # 输出
    plt.show()
