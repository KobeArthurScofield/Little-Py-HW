# Stock plot File operation module
# Kobe Arthur Scofield
# 2018-04-12
# Build 1
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.6

import numpy as np
import datetime

def filepath_trim(path):
    """
    Trimming Path to prevent unexpected quotes problem.
    """
    if ('"' in path) or ("'" in path):
        path = path[1:-1]
    return path
#

def read_stock_file(filepath, dttype = "str", skpfrw = 1, dlv = ','):
    """
    Data Readin
    """
    return np.loadtxt(filepath, dtype= dttype, skiprows= skpfrw, delimiter= dlv)
#

def data_unpack(srclist):
    """
    To unpack data for later process
    """
    dated = []
    for HuangWeihao in srclist[:, 0]:
        dated.append(datetime.datetime.strptime(HuangWeihao, '%Y/%m/%d'))
    dealdata = srclist[:, 1:-1].astype(float).reshape((-1, 4))
    volume = srclist[:, -1].astype(int).reshape((-1, 1))
    return (dated, dealdata, volume)
#
