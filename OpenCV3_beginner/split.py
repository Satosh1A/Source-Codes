import cv2

try:
    img = cv2.imread('C:/Source Codes/OpenCV3_beginner/images/sample.jpg')
    if img is None:
        print('ファイルを読み込めません．')
        import sys
        sys.exit()
    
    rgb = cv2.split(img)
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/b.jpg',blue)
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/g.jpg',green)
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/r.jpg',red)
    cv2.imshow("blue",blue)
    cv2.imshow("green",green)
    cv2.imshow("red",red)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print ("Error:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
      

