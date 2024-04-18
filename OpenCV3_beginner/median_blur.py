import cv2

try:
    img = cv2.imread('C:/Source Codes/OpenCV3_beginner/images/sample.jpg')
    if img is None:
        print('ファイルを読み込めません．')
        import sys
        sys.exit()
    
    dst = cv2.medianBlur(img,11)    
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/medianBlur1.jpg',dst)
    cv2.imshow('dst1',dst)

    dst = cv2.medianBlur(img,33)    
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/medianBlur2.jpg',dst)
    cv2.imshow("dst2",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print ("Error:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
      

