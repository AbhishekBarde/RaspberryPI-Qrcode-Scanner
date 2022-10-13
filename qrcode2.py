import cv2
from pyzbar.pyzbar import decode

def scan():
    cap = cv2.VideoCapture(1)
    i12=0
    while i<1:
        _,frame = cap.read()
	
        decodeobj = decode(frame)
        for obj in decodeobj:
            print(obj.data)
            i+=1
        cv2.imshow('Frame',frame)
	
        cv2.waitKey(2)
        cv2.destroyAllWindows

scan()
