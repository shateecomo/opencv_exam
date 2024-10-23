import cv2
from pytube import YouTube

# 비디오 로드
filename = 'D:\다운\ideoplayback.mp4'
capture = cv2.VideoCapture(filename) 

# 키보드 입력있거나 끝날떄까지...플레이
while cv2.waitKey(25) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = capture.read()
    #플레이
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()

