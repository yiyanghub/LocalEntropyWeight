# -*- coding: utf-8 -*-
# @Time    : 2023/2/13 18:51
# @Author  : Yangyi
# @File    : ReadDistance.py
# @Software: PyCharm


import numpy as np

# 获得距离矩阵
def read_TAZ_distance(filepath1):
    with open(filepath1, 'r') as f:
        lines = f.readlines()[1:]

    dataset = np.zeros((len(lines), 3), dtype='float32')  # 存储地块1、地块2、距离

    i = 0
    for line in lines:
        dataset[i][0] = line.split()[0].strip()
        dataset[i][1] = line.split()[1].strip()
        dataset[i][2] = line.split()[2].strip()
        i += 1

    """
    dataset结构
    [[   0.      292.     3051.0037]
     [   0.      318.     3116.7854]
     [   0.      301.     3225.3655]
     ...
     [5512.     1967.     4901.89  ]
     [5512.     1942.     4984.915 ]
     [5512.     4530.     4951.4126]]
    """

    # 将dataset转化为n*n的矩阵
    distance_matrix = np.zeros((5513, 5513))  # 地块距离矩阵
    for j in range(len(dataset)):
        row, col = int(dataset[j][0]), int(dataset[j][1])
        distance_matrix[row][col] = dataset[j][2]


    return distance_matrix