# -*- coding: utf-8 -*-
import numpy as np
from scipy import linalg as lg
import json
"""
# 行列式
# 中文乱码问题，如何转码：
http://m.blog.csdn.net/buptlrw/article/details/48027657
"""


def main():
    print isinstance("你好", str)
    arr = np.array([[1, 2], [3, 4]])
    print "行列式：", lg.det(arr)
    print("行列式：", lg.det(arr))
    print json.dumps(("行列式:", lg.det(arr)), encoding='utf-8', ensure_ascii=False)


if __name__ == '__main__':
    main()