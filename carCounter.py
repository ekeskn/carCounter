import cv2

backsub = cv2.createBackgroundSubtractorMOG2()
capture = cv2.VideoCapture("video.avi")

i = 0
j=0
minArea=2300
line = 0
while True:
    _,frame = capture.read()
    fgmask=backsub.apply(frame,None,0.02)
    erode=cv2.erode(fgmask,None,iterations=4)
    moments=cv2.moments(erode,True)
    if moments['m00'] >= minArea:
        x = int(moments['m10'] / moments['m00'])
        y = int(moments['m01'] / moments['m00'])
        print(" moment: " + str(moments["m00"]) + " x: " + str(x) + " y: " + str(y))

        if (x > 40 and x < 55 and y > 50 and y <65):
            i += 1
            print("left line" + str(i))
        elif(x>100 and x< 110and y> 105 and y< 130):
            i+=1
            print("right line" + str(i) )

    cv2.putText(frame,"cars: "+ str(i),(200,30),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,0),2 )


    cv2.imshow('video',frame)
    key=cv2.waitKey(25)
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

