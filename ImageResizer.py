# Raster Image Resizing
# Kobe Arthur Scofield
# 2018-03-29
# Build 34
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.4

# Warning:
# For crossing-platform adaptation, you'll have to input the path of the image by yourself.
# (Hard coding the path may cause some problem)

# Note: Sometimes I suspect the script 'dead' because of some turtle-speed operation.
# So some prints for diagnostic (especially for mental diagnostic)

import numpy as np; print("Module NumPy loaded.")
import matplotlib.pylab as plt; print("Module MatPlotLib loaded.", end = "\n\n")

# Filepath: input and return the file path
# msg: message wiss show on input
def filepath(msg):
    fpath = input(msg)
    if fpath[0] == '"':     # Sometimes the path may contain quotes and will make an error
        fpath = fpath[1:-1] # So have to delete the quote
    return fpath
# End of filepath

# imgplot: display the image array
def imgplot(imgdata, **kwargs):
    plt.imshow(imgdata, interpolation="none", **kwargs)
    plt.axis("off")     # axis should not be shown
    plt.show()
# End of imgplot

# imgsave: save the image
# imgdata: The image array
def imgsave(imgdata):
    savepath = filepath("Input where the image wanna save: ")
    plt.imsave(arr = imgdata, fname = savepath, format = "pdf") # Export as PDF format
# End of imgsave

img_path = filepath("Please input the path of the image (RGB or RGBA): ")
img_data = plt.imread(img_path)     # Read image data
print("Image size:", img_data.shape)

scale = int(input("Please input the scale of the image, positive for enlarging and negative for shrinking: "))
if scale < 0:   # shrink
    print("Process... Using interpolation.")
    newimg = np.zeros((img_data.shape[0] // (-scale), img_data.shape[1] // (-scale), img_data.shape[2]), dtype = img_data.dtype)    # Create target
    newimg = img_data[::-scale, ::-scale]   # Create data and store to target
    print("New image size:", newimg.shape)
    imgsave(newimg)
    imgplot(newimg)
elif scale > 0: # enlarge
    print("Process... Using interpolation.")
    print("Scale reset to 2.")
    scale = 2
    newimg = np.zeros((img_data.shape[0]*scale, img_data.shape[1]*scale, img_data.shape[2]), dtype= img_data.dtype) # Create target
    newimg[0::scale, 0::scale, ::] = img_data[::, ::, ::]   # Copy the origin grid
    # Average nearby pixels as interpolation
    newimg[1:-1:scale, 0:-1:scale, ::] = img_data[0:-1:, 0::, ::] / 2 + img_data[1::, 0::, ::] / 2      # Verticle
    newimg[0:-1:scale, 1:-1:scale, ::] = img_data[0::, 0:-1:, ::] / 2 + img_data[0::, 1::, ::] / 2      # Horizon
    newimg[1:-1:scale, 1:-1:scale, ::] = img_data[0:-1:, 0:-1:, ::] / 4 + img_data[1::, 1::, ::] / 4 +\
                                        img_data[1::, 0:-1:, ::] / 4 + img_data[0:-1:, 1::, ::] / 4    # Diagonal
    # Black border fixing
    newimg[-1] = newimg[-2]
    newimg[:, -1] = newimg[:, -2]
    newimg[-1, -1] =newimg[-2, -2]
    print("New image size:", newimg.shape)
    imgsave(newimg)
    imgplot(newimg)
else:
    print(scale, "is not what the program want.")
#
