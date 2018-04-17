# Stock plot Stock processing module
# Kobe Arthur Scofield
# 2018-04-12
# Build 1
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.6

import numpy as np

hgn = 0

def avg_calc(src):
    """
    Calculate average of all, average of day, and create average line
    """
    avg = np.average(src[:, 1:2])
    avgln = np.full(src.shape[0], avg)
    avgpd = np.zeros(src.shape[0], dtype = src.dtype)
    avgpd[:] = src[:, 1] / 2 + src[:, 2] / 2
    return avg, avgln, avgpd
#

def avg_count(avgdata, avg):
    """
    Counting days higher than average
    """
    global hgn
    for HuangWeihao in avgdata:
        if (HuangWeihao > avg):
            hgn += 1
    return hgn
#
