import cv2
import numpy as np

try:
    img1 = cv2.imread('C:/Source Codes/OpenCV3_beginner/images/sample.jpg')
    img2 = cv2.imread('C:/Source Codes/OpenCV3_beginner/images/20230609.jpg')

    if img1 is None or img2 is None:
        print('ファイルを読み込めません．')
        import sys
        sys.exit()

    height = img1.shape[0]
    width = img1.shape[1]
    img2 = cv2.resize(img2,(width,height))
    dst = cv2.add(img1,img2)
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/add.jpg',dst)
    cv2.imshow('dst',dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print ("Error:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
    