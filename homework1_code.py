#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.pylab import *

mpl.rcParams["font.sans-serif"] = ['SimHei']

#计算点积
def computeDot(x,y):
    x = np.array(x)
    y = np.array(y)
    return np.dot(x,y)

#计算第一范式
def computeNorm1(x):
    return np.linalg.norm(x,1)

#计算第二范式
def computeNorm2(x):
    x = np.array(x)
    return np.linalg.norm(x,2)

if __name__ == "__main__":
    x = []
    y = []
    with open("./iris.txt",'r') as f:
        line = f.readline()#一行行读取数据
        while line:
            #print(line)
            res = line.split(",")#按照逗号分割，读取前两列数据为花萼长度和宽度
            x.append(float(res[0]))
            y.append(float(res[1]))
            line = f.readline()
        f.close()
    print("花萼长度数据: " + str(x))
    print("花萼宽度数据: " + str(y))

    #点积  范数  二范数的举例
    point1 = [x[4],y[4]]
    point2 = [x[8],y[8]]
    dot = computeDot(point1,point2)
    norm1 = computeNorm1(point1)
    norm2 = computeNorm2(point1)
    print("点" + str(point1) + "和点" + str(point2) + "的点积结果为： " + str(dot))
    print("点" + str(point1) + "第一范式为： " + str(norm1))
    print("点" + str(point1) + "第二范式为： " + str(norm2))

    #绘制散点图
    plt.title("iris数据集2D散点图")
    plt.xlim(xmax=8,xmin=4)
    plt.ylim(ymax=5,ymin=2)
    plt.xlabel("X1:sepal length")
    plt.ylabel("X2:sepal width")
    plt.plot(x,y,'ro')
    plt.show()

