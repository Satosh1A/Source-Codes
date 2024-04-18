import cv2

try:
    img = cv2.imread('C:/Source Codes/OpenCV3_beginner/images/sample.jpg')
    if img is None:
        print('ファイルを読み込めません．')
        import sys
        sys.exit()
        raise ValueError('ファイルを読み込めません')
    
    cv2.line(img,(150,170),(300,170),(255,0,0))
    cv2.line(img,(150,220),(300,220),(0,255,0),5)
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/LinesOnImage.jpg',img)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except ValueError as e:
    print(e)
except:
    import sys
    print ("Error:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
      

