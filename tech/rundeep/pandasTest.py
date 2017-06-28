# -*- coding: utf-8 -*-
# __author__ = 'Administrator'
import pandas as pd
import numpy as np
"""
pandas绘图
"""


def main():
    ts = pd.Series(np.random.randn(1000), index=pd.date_range("20170621", periods=1000))
    ts = ts.cumsum()
    print ts
    from pylab import *
    ts.plot()
    show()


if __name__ == '__main__':
    main()
