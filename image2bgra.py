import cv2
import glob, os
from matplotlib import pyplot as plt

os.chdir("img")
types = ('*.bmp', '*.jpg', '*.png') # the tuple of file types
files_grabbed = []
for files in types:
    files_grabbed.extend(glob.glob(files))
    
for imgfile in files_grabbed:
    img = cv2.imread(imgfile)
    #cv2.imshow(imgfile, img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    buf_bgra = cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA)

    # 使用 Matplotlib 顯示圖片
    plt.imshow(buf_bgra)
    plt.show()

    root, extension = os.path.splitext(imgfile)
    newFile = open(root+".bgra", "wb")
    newFile.write(bytearray(buf_bgra))
    newFile.close()
