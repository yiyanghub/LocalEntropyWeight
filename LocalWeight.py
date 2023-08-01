# -*- coding: utf-8 -*-
# @Time    : 2023/2/13 19:03
# @Author  : Yangyi
# @File    : LocalWeight.py
# @Software: PyCharm


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Entropy import entropy

def get_local_weight(data_0, distance_matrix):

    localweight = []
    for i in range(data_0.shape[0]):
        distance_i = distance_matrix[i, :].reshape(-1, 1)
        data = np.where(data_0 * distance_i > 0, data_0, 0)
        # 删除全0行
        data_i = data[~(data == 0).all(1)]
        distance_i = distance_i[~(distance_i == 0).all(1)]
        # 根据距离进行加权，获得三种活力值
        data_i = data_i * distance_i * distance_i / np.sum(distance_i * distance_i, axis=0)
        # 计算熵权
        local_weight_i = entropy(data_i)
        localweight.append(local_weight_i.tolist())

    localweight = np.array(localweight)
    print(localweight)

    # 直方图绘制(某指标)
    fig, axes = plt.subplots()
    pd.DataFrame(localweight[:,0]).plot.hist(bins=50, ax=axes, label=None, fontsize=20)
    axes.set_title('Culture', fontsize=20)  # 设置直方图的标题
    axes.set_xlabel('Weight', fontsize=20)
    plt.show()


    #pd.DataFrame(localweight).to_excel('localweight.xlsx')

    return localweight