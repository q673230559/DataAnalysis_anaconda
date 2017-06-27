# encoding: utf-8
import numpy as np
"""
from http://www.imooc.com/learn/843
3.2 demo
"""


def main():
    import matplotlib.pyplot as plt
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="COS", alpha=0.5)
    plt.plot(x, s, "r*", label="SIN")
    plt.title("COS & SIN")
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    plt.legend(loc="upper left")
    plt.grid()
    plt.axis([-2, 2, -0.5, 1])
    plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color="green", alpha="0.25")
    t = 1
    plt.plot([t, t], [0, np.cos(t)], "y", linestyle="--")
    plt.annotate("cos(1)",xy=(t, np.cos(1)), xycoords="data", xytext=(+10, +30),
                 textcoords="offset points", arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    plt.show()

if __name__ == '__main__':
    main()
