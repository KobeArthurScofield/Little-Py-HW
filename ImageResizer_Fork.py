# Raster Image Resizing
# Kobe Arthur Scofield
# 2018-03-29
# Build 20
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.4

# Warning:
# For crossing-platform adaptation, you'll have to input the path of the image by yourself.
# (Hard coding the path may cause some problem)

# Note: Sometimes I suspect the script 'dead' because of some turtle-speed operation.
# So some prints for diagnostic (especially for mental diagnostic)

import numpy as np; print("Module NumPy loaded.")
import matplotlib.pylab as plt; print("Module MatPlotLib loaded.", end = "\n\n")

def imgplot(imgdata, **kwargs):
    plt.imshow(imgdata, interpolation="none", **kwargs)
    plt.axis("off")
    plt.show()
#

img_path = input("Please input the path of the image: ")
if img_path[0] == '"':
    img_path = img_path[1:-1]
img_data = plt.imread(img_path)
print("Image size:", img_data.shape)

print("Process... Using interpolation.")
scale = 2
newimg = np.zeros((img_data.shape[0]*scale, img_data.shape[1]*scale, img_data.shape[2]), dtype=img_data.dtype)
newimg[0::2, 0::2, ::] = img_data[::, ::, ::]
# Devil here :-)
newimg[1:-1:2, 0::2, ::] = (img_data[0:-1:, ::, ::] + img_data[1::, ::, ::]) // 2
newimg[0::2, 1:-1:2, ::] = (img_data[::, 0:-1:, ::] + img_data[::, 1::, ::]) // 2
newimg[1:-1:2, 1:-1:2, ::] = (img_data[0:-1:, 0:-1:, ::] + img_data[1::, 1::, ::]) // 2
imgplot(img_data)
imgplot(newimg)
