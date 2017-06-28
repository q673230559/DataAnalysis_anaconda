# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
"""
from http://www.imooc.com/learn/843
慕课 3.2 demo
"""


def main():
    # scatter
    fig = plt.figure()
    # fig.add_subplot(3, 3, 1)
    ax = fig.add_subplot(3, 3, 1)
    n = 128
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(X, Y)
    # plt.axes([0.025, 0.025, 0.95, 0.95])
    ax.scatter(X, Y, s=75, c=T, alpha=.5)
    plt.xlim(-1.5, 1.5), plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")

    # bar
    fig.add_subplot(332)
    n = 10
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    plt.bar(X, +Y1, facecolor="#9999ff", edgecolor="white")
    plt.bar(X, -Y2, facecolor="#ff9999", edgecolor="white")
    for x, y in zip(X, Y1):
        plt.text(x+0.4, y+0.5, "%.2f" % y, ha="center", va="bottom")
    for x, y in zip(X, Y2):
        plt.text(x+0.4, -y-0.5, "%.2f" % y, ha="center", va="top")

    plt.show()


if __name__ == '__main__':
    main()
