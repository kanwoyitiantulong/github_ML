#!/usr/bin/python
# -*-coding:utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy import stats


if __name__=='__main__':
    #计算均值，方差，偏度和峰度
    d=np.random.randn(100000)
    mu=np.mean(d)
    std=np.std(d)
    skew=stats.skew(d)
    kurt=stats.kurtosis(d)
    print("均值，方差，偏度，峰度：",mu, std, skew, kurt)

    #画二维高斯图像
    d=np.random.randn(100000,2)
    densty,edage=np.histogramdd(d,bins=30)
    print(densty,densty.shape)
    densty/=densty.max()
    x=y=np.arange(0, 30, 1)
    t=np.meshgrid(x, y)
    fig=plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(t[0], t[1],densty, c='r', s=50*densty, marker='o', depthshade=True)
    ax.plot_surface(t[0], t[1], densty, cmap=cm.Accent, rstride=1, cstride=1, alpha=0.9, lw=0.75)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('二元高斯分布，样本个数：%d' % d.shape[0], fontsize=15)
    plt.tight_layout(0.1)
    plt.show()
