# Stock plot
# Kobe Arthur Scofield
# 2018-04-12
# Build 2
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.6

import numpy as np
import matplotlib.pyplot as plt
print("Main Library Ready")

from llib import fileop as fop
from llib import stckproc as stk
print("All Library Ready")


rdin = fop.read_stock_file(fop.filepath_trim(input("Input file location or path: ")))
date, stcdata, volume = fop.data_unpack(rdin)
lblt = ["Open", "High", "Low", "Close"]
avg, avgln, avgpd = stk.avg_calc(stcdata)
print("The average price is %f" % avg)
highday = stk.avg_count(avgpd, avg)
print("%d day's average is higer than the period average." % highday)


plt.figure()
# plt.boxplot(stcdata[1:2])
for HuangWeihao in [0, 1, 2, 3]:
    plt.plot(date, stcdata[:, HuangWeihao], label = lblt[HuangWeihao])
plt.plot(date, avgln, label = "Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.savefig(fop.filepath_trim(input("Input file location or path for saving: ")))
plt.show()
