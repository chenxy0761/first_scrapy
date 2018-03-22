# -*- coding:utf-8 -*-

from __future__ import division
from numpy.random import randn
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

np.random.seed(12345)

from pandas import Series,DataFrame
import pandas as pd
np.set_printoptions(precision=4)
if __name__ == '__main__':
    # print(pd.read_table('../data/data3.txt',sep='\s+'))
    import json
    obj = \
    """
    {"姓名":"张三",
    "住处":["天朝","挖煤国","英国"],
    "宠物":null,
    "兄弟":[{"姓名":"李四","年龄":25,"宠物":"汪星狗"},{"姓名":"王五","年龄":23,"宠物":"火星猫"}]
    }
    """
    # result = json.dump()
    # print(result)
