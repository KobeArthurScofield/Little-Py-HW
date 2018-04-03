# Cluster BINNING
# Kobe Arthur Scofield
# 2018-03-30
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
def imgsave(imgdata, **kwargs):
    savepath = filepath("Input where the image wanna save: ")
    plt.imsave(arr = imgdata, fname = savepath, format = "pdf", **kwargs) # Export as PDF format
# End of imgsave

img_path = filepath("Please input the image path: ")
img_data = plt.imread(img_path)
print("RAW CCD image size: ", img_data.shape, img_data.dtype)
BINNING = int(input("Please input BINNING value: "))            # BINNING value here
proc_img = np.zeros((img_data.shape[0]//BINNING, img_data.shape[1]//BINNING), dtype= img_data.dtype)    # Prepare an empty array to as the new image
img_data = img_data[:(proc_img.shape[0]*BINNING), :(proc_img.shape[1]*BINNING)]                         # Cutting edge (Error prevent)
print("Process...")
for dpy in range(0, BINNING):       # Row interleaving
    for dpx in range(0, BINNING):   # Line interleaving
        proc_img[::] = img_data[dpy::BINNING, dpx::BINNING] / (BINNING**2) + proc_img[::]   # Process each cluster and calculate average in the mean time
print("Done.")
imgsave(proc_img, cmap="gray")
print("Image saved.")
imgplot(proc_img, cmap="gray")