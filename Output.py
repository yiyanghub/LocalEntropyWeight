# -*- coding: utf-8 -*-
# @Time    : 2023/2/13 19:01
# @Author  : Yangyi
# @File    : Output.py
# @Software: PyCharm

import numpy as np
import pandas as pd

# 结果输出
def to_excel(localweight, data):

    data_max, data_min = np.max(data, axis=0), np.min(data, axis=0)
    nor_data = (data - data_min) / (data_max - data_min + 1e-5)


    v = np.sum(localweight * nor_data, axis=1).reshape(-1, 1)
    pd.DataFrame(v).to_excel('localweight_v_result.xlsx')

    return 0