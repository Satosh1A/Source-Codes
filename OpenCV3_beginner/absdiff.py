import cv2
import math
import numpy as np

try:
    def create_cos(rows,cols):
        weight = np.zeros((rows,cols,3),np.float32)
        center = (rows/2,cols/2)
        radius = math.sqrt(center[0]**2+center[1]**2)

        for r in range(rows):
            for c in range(cols):
                distance = math.sqrt((center[0]-r)**2+(center[1]-c)**2)

                radian = (distance/radius)*math.pi

                Y =(math.cos(radian)+1.0)/2.0
                weight[r,c]=[Y,Y,Y]
        
        return weight
    
    img1 = cv2.imread('C:/Source Codes/OpenCV3_beginner/images/sample.jpg').astype(np.float32)/255
    img2 = cv2.imread('C:/Source Codes/OpenCV3_beginner/images/20230609.jpg').astype(np.float32)/255

    if img1 is None or img2 is None:
        print('ファイルを読み込めません．')
        import sys
        sys.exit()

    height = img1.shape[0]
    width = img1.shape[1]
    img2 = cv2.resize(img2,(width,height))
    
    rows,cols=img1.shape[:2]
    weight = create_cos(rows,cols)
    i_weight = 1.0-weight
    int_src1 = cv2.multiply(img1,weight)
    int_src2 = cv2.multiply(img2,i_weight)
    dst = cv2.absdiff(img1,img2)
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/absdiff.jpg',dst)
    cv2.imshow('dst1',dst)
    blue = np.zeros((height,width,3),np.float32)
    blue[:,:] = [128.0,0.0,0.0]
    dst = cv2.absdiff(img1,blue)
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/absdiffScalar.jpg',dst)
    cv2.imshow('dst2',dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print ("Error:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
    