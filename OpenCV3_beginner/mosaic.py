import cv2
import numpy as np

try:
    img = cv2.imread('C:/Source Codes/OpenCV3_beginner/images/sample.jpg')
    if img is None:
        print('ファイルを読み込めません．')
        import sys
        sys.exit()
    
    SCALE = 0.2
    height = img.shape[0]
    width = img.shape[1]

    dst = cv2.resize(img,(round(width*SCALE),round(height*SCALE)),interpolation= cv2.INTER_NEAREST)    
    dst = cv2.resize(dst,(width,height),interpolation=cv2.INTER_NEAREST)
    
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/mosaic.jpg',dst)
    cv2.imshow('dst',dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print ("Error:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
    