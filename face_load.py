import cv2
import os
import sys

# cascade_file = "/Document/Project/face_cascade.xml"
cascade_file = "/usr/local/Cellar/opencv/4.1.0_1/share/opencv4/haarcascades/haarcascade_frontalface_default.xml"
# 얼굴 인식 특징 파일 읽어 들이기
cascade = cv2.CascadeClassifier(cascade_file)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#Tracking 저장
TrackingROI = (0,0,0,0)

# #
#  Tracking Trigger
# 0 : Not Face
# 1 : Tracking Face 
# #
tracking_trigger = 0

while True:
    ret, frame = capture.read()

    frame = cv2.flip(frame, -1)

    height, width, channel = frame.shape
    matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
    frame = cv2.warpAffine(frame, matrix, (width, height))

    #그레이 스케일로 변환
    capture_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #히스토그램 평활화
    capture_gs = cv2.equalizeHist(capture_gs)

    # face_list = cascade.detectMultiScale(capture_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))
    # face_list = cascade.detectMultiScale(capture_gs, 1.3, 5)
    if tracking_trigger==0:
        face_list = cascade.detectMultiScale(capture_gs, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        print(face_list)
        
        if len(face_list) > 0:
            x,y,w,h = face_list[0]
            TrackingROI = (x,y,w,h)
            p1 = (int(TrackingROI[0]), int(TrackingROI[1]))
            p2 = (int(TrackingROI[0] + TrackingROI[2]), int(TrackingROI[1] + TrackingROI[3]))
            cv2.rectangle(frame, p1, p2, (0,255,0), thickness=8)
            tracker = cv2.TrackerKCF_create()
            tracker.init(frame,TrackingROI)
            tracking_trigger = 1
    else:
        search, TrackingROI = tracker.update(frame)
        if search:
            #추적 성공했다면
            p1 = (int(TrackingROI[0]), int(TrackingROI[1]))
            p2 = (int(TrackingROI[0] + TrackingROI[2]), int(TrackingROI[1] + TrackingROI[3]))
            #화면에 박스로 표시 (파랑)
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            print('success x %d ' % (int(TrackingROI[0])) + 'y %d ' % (int(TrackingROI[1])) +'w %d ' % (int(TrackingROI[2])) + 'h %d ' % (int(TrackingROI[3])))
        else:
            print('Tracking failed')
            tracking_trigger = 0
        

    # color = (0, 0, 255)
    # for face in face_list:
    #     x, y, w, h = face
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), color, thickness=8)
        
    cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(1) > 0:
        break


capture.release()
cv2.destroyAllWindows()
