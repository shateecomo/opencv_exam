import cv2
import numpy as np
import requests


def filt(img_url,fltname):
    response = requests.get(img_url,stream=True).raw
    image = np.asarray(bytearray(response.read()),dtype='uint8')

    src = cv2.imdecode(image,cv2.IMREAD_COLOR)
    dst = cv2.applyColorMap(src,fltname)

    #cv2.imshow('ss',src)
    #cv2.waitKey()
    cv2.imshow('dd',dst)
    cv2.waitKey()
    return 0

#--------------------------------------------------------------------------


img_url="https://stsci-opo.org/STScI-01J74E05Z4PPBJAYVRS5ZND4Q5.png"
#fltn=cv2.COLORMAP_DEEPGREEN
#fltn=cv2.COLORMAP_PLASMA
fltn=cv2.COLORMAP_PINK
 
filt(img_url,fltn)


