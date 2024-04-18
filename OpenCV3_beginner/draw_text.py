import cv2

try:
    img = cv2.imread('C:/Source Codes/OpenCV3_beginner/images/sample.jpg')
    if img is None:
        print('ファイルを読み込めません．')
        import sys
        sys.exit()
    
    cv2.circle(img,(225,70),30,(0,255,0),2)
    cv2.circle(img,(225,190),160,(255,255,0),6)
    cv2.circle(img,(225,280),40,(0,255,255),-1)
    cv2.line(img,(150,170),(300,170),(255,0,0))
    cv2.line(img,(150,220),(300,220),(0,255,0),5)
    cv2.putText(img,'Hello OpenCV',(155,150),cv2.FONT_HERSHEY_COMPLEX,0.62,(50,60,80),2)
    cv2.imwrite('C:/Source Codes/OpenCV3_beginner/images/puttext.jpg',img)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print ("Error:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
      

