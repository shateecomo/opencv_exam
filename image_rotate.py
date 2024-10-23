import cv2
import numpy as np
import requests


url="https://dimg.donga.com/wps/NEWS/IMAGE/2023/11/22/122304660.2.jpg"


response = requests.get(url, stream=True).raw
image = np.asarray(bytearray(response.read()),dtype="uint8")

src = cv2.imdecode(image,cv2.IMREAD_COLOR)

height, width, channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2,height/2),90,1)

dst = cv2.warpAffine(src,matrix,(width,height))


cv2.imshow("1",src)
cv2.waitKey()
cv2.imshow("2",dst)
cv2.waitKey()