# 03/30/17
# Author: Kun Tian (io.kuntian@gmail.com)
# Python 2.7

from __future__ import print_function, division
import numpy as np


def update(func, y_init, t_len, cc, params, tstep):
    num_vars = len(y_init)
    y = np.zeros((t_len, num_vars))
    y[0] = y_init

    # Euler
    # for i in range(0, t_len - 1):
    #     y[i+1] = y[i] + f(y[i],cc[i], params) * tstep
    #
    # return y


    ## rk 4th
    # for i in range(0, t_len - 1):
    #     xi1 = y[i]
    #     k1 = f(xi1, tspan[i], cc, params)
    #     xi2 = y[i] + (tstep / 2) * k1
    #     k2 = f(xi2, tspan[i] + (tstep / 2), cc, params)
    #     xi3 = y[i] + (tstep / 2) * k2
    #     k3 = f(xi3, tspan[i] + (tstep / 2), cc, params)
    #     xi4 = y[i] + tstep * k3
    #     k4 = f(xi4, tspan[i + 1], cc, params)
    #     y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6 * tstep

    ## exponential Euler
    for i in range(0, t_len):
        if i <= t_len - 2:
            y[i+1] = func(y[i], cc[i], params, tstep)

            # if i % 1000 == 0:
            #   print(i)

    return y