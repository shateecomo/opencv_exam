import cv2

#카메라(캠) 세팅
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while cv2.waitKey(33)<0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES,0)
    
    #frame = 정지화면, ret = return(제대로 읽었는지 확인하기위한 변수?) frame이랑 대조해보는듯...
    ret,frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    
    
capture.release()

cv2.destroyAllWindows()
