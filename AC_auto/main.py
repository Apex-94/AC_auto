# import numpy as np
# from PIL import ImageGrab
# import cv2
# import time
#
# last_time =time.time()
#
# while(True):
#     printscreen_pil =  ImageGrab.grab(bbox=(0,40,800,640))
#     # printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')
#     # .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
#     print('lopp took {} secounds'.format(time.time()-last_time))
#     last_time = time.time()
#     cv2.imshow('window', cv2.cvtColor(np.array(printscreen_pil), cv2.COLOR_BGR2RGB))
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
#

import mss
import time

import cv2
import mss
import numpy
from directkeys import PressKey, W, A, S, D, ReleaseKey


def process_img(og_img):
    processed_img = cv2.cvtColor(og_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

# for i in list(range(5))[::-1]:
#     print(i+1)
#     time.sleep(1)
#
#
# PressKey(W)
# time.sleep(1)
# ReleaseKey(W)
# PressKey(S)
# time.sleep(1)
# ReleaseKey(S)




with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 40, "left": 0, "width": 800, "height": 640}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        screen = numpy.array(sct.grab(monitor))

        new_screen = process_img(screen)
        # Display the picture
        cv2.imshow("window", new_screen)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print("fps: {}".format(1 / (time.time() - last_time)))
        # print('lopp took {} secounds'.format(time.time()-last_time))
        # last_time = time.time()
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


