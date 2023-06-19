import cv2
import glob, os
import numpy as np
from matplotlib import pyplot as plt

height=600
width=1024

os.chdir("out")
types = ('*.nv12') # the tuple of file types
files_grabbed = []
for files in types:
    files_grabbed.extend(glob.glob(files))
    
files_grabbed.remove('.')
    
for imgfile in files_grabbed:
    print(imgfile)

    with open(imgfile, 'rb') as f:
        yuv = np.fromfile(f, dtype=np.uint8)

    framesize = height * width * 3 // 2

    bgr = cv2.cvtColor(yuv.reshape((int(height*3/2), width)), cv2.COLOR_YUV2BGR_NV12)
    cv2.imshow("YUV2BGR_NV12", bgr)
    cv2.waitKey(0)

    f.close()

    #顯示圖片
    #plt.imshow(bgr)
    #plt.show()
