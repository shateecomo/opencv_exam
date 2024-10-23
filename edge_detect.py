import cv2
import numpy as np
import requests

img_url="https://stsci-opo.org/STScI-01J74E05Z4PPBJAYVRS5ZND4Q5.png"

# img_url="https://us.123rf.com/450wm/boomkee2532z/boomkee2532z2108/boomkee2532z210800056/173357824-%ED%9D%91%EB%B0%B1-%EB%B6%80%EB%93%9C%EB%9F%AC%EC%9A%B4-%EA%B7%B8%EB%9D%BC%EB%8D%B0%EC%9D%B4%EC%85%98-%EB%B0%B0%EA%B2%BD-%EC%9D%B4%EB%AF%B8%EC%A7%80-%ED%9A%8C%EC%83%89.jpg"
# img_url="https://plus.unsplash.com/premium_photo-1672201106204-58e9af7a2888?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8JUVBJUI3JUI4JUVCJTlEJUJDJUVCJThEJUIwJUVDJTlEJUI0JUVDJTg1JTk4JTIwJUVCJUIwJUIwJUVBJUIyJUJEfGVufDB8fDB8fHww"

response = requests.get(img_url,stream=True).raw
image = np.asarray(bytearray(response.read()),dtype='uint8')

src = cv2.imdecode(image, cv2.IMREAD_COLOR)

# 캐니 윤곽선 검출 (컬러에서)
canny = cv2.Canny(src, 100,255)


# GRAY = 흑백으로 변환
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 행열의 가중치 변화를 검출
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
# 미분의 기울기값 검출
laplacian = cv2.Laplacian(gray, cv2.CV_8U,ksize=3)



cv2.imshow('ss',gray)
cv2.waitKey()
cv2.imshow('dd',canny)
cv2.waitKey()
