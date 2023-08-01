# -*- coding: utf-8 -*-
# @Time    : 2023/2/13 18:49
# @Author  : Yangyi
# @File    : Entropy.py
# @Software: PyCharm

import numpy as np

# 普通熵值法计算权重
def entropy(data):

    data_max, data_min = np.max(data, axis=0), np.min(data, axis=0)
    # 对所有指标进行归一化
    nor_data = (data - data_min) / (data_max - data_min + 1e-5)

    # 计算第j个指标下第i个样本的占比
    weight_ij = nor_data / (np.sum(nor_data, axis=0) + 1e-5)

    # 计算熵值
    K = 1 / np.log(data.shape[0])
    etro_j = -K * np.sum(weight_ij * np.log(weight_ij + 1e-5), axis=0)  # + 1e-5防止log数字溢出出现错误
    # 计算差异系数
    dif_j = 1 - etro_j
    # 计算各项权重
    weight = dif_j / np.sum(dif_j)


    return weight