# -*- coding: utf-8 -*-
# @Time    : 2023/2/13 18:59
# @Author  : Yangyi
# @File    : Main.py
# @Software: PyCharm

import time
import pandas as pd
import numpy as np
from ReadDistance import read_TAZ_distance
from LocalWeight import get_local_weight
import Output

if __name__ == '__main__':

    st = time.perf_counter()  # 计时

    # 获取路径，得到txt权重数据
    filepath1 = 'TAZWeight_5000meters_GeoDa.txt'
    # 获取三类活力值
    filepath2 = 'Vitality.xlsx'


    df = pd.DataFrame(pd.read_excel(filepath2))
    # 数据分别为文化活力值、经济活力值、社会（人口）活力值
    data = df[['cul', 'light', 'work']].values
    # 通过矩阵运算，得到利用距离更新后的活力值
    distance_matrix = read_TAZ_distance(filepath1)

    localweight = get_local_weight(data, distance_matrix)
    #Output.to_excel(localweight, data)

    print(np.mean(localweight, axis=0))

    et = time.perf_counter()
    print('time:', et - st)