#!/usr/bin/python
# -*-conding:utf8-*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D



#混合正态分布

if __name__=='__main__':
    x1=[1, 2, 3]
    x2=[4, 5, 6]
    x=np.stack((x1, x2), axis=0)
    print(x.shape)
    print(x)
    x1, x2 = np.mgrid[-5:5:51j, -5:5:51j]#创建网格
    # print(x1.shape)
    x = np.stack((x1, x2), axis=0)#合并axis决定矩阵方式
    # print(x.shape)
    # mpl.rcParams['axes.unicode_minus'] = False
    # mpl.rcParams['font.sans-serif'] = 'SimHei'
    plt.figure(figsize=(9, 8), facecolor='w')
    sigma = (np.identity(2), np.diag((3, 3)), np.diag((2, 5)), np.array(((2, 1), (1, 5))))
    for i in np.arange(4):
        ax = plt.subplot(2, 2, i + 1, projection='3d')
        norm = stats.multivariate_normal((0, 0), sigma[i])
        y = norm.pdf(x)
        ax.plot_surface(x1, x2, y, cmap=cm.Accent, rstride=2, cstride=2, alpha=0.9, lw=0.3)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
    plt.suptitle('二元高斯分布方差比较', fontsize=18)
    plt.tight_layout(1.5)
    plt.show()