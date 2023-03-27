
import time
import cv2
import mediapipe as mp
import serial
from struct import *
import sys
import math
#initializing cv2 and Serial
cap = cv2.VideoCapture(0)
mp_draw = mp.solutions.drawing_utils
mp_draw_style = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
with mp_hands.Hands(model_complexity=0, min_detection_confidence=0.6, min_tracking_confidence=0.9, max_num_hands=1) as hand:
    while cap.isOpened():
      success, img = cap.read()
      if not success:
      #Empty camera frame
        print("Empty Camera Frame")
        continue
    #Get the window dimensions
      h,w,c=img.shape
      img.flags.writeable = False
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      results = hand.process(img)
      img.flags.writeable = True
      img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # getting the landmark list and drawing it
      lmList=[]
      dir(results)
      if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          mp_draw.draw_landmarks(
          img,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_draw_style.get_default_hand_landmarks_style(),
          mp_draw_style.get_default_hand_connections_style())
        
        myHand=results.multi_hand_landmarks[0]
        for id,lm in enumerate(myHand.landmark):
          cx,cy,cz = int(lm.x*w),int(lm.y*h),int(lm.z*1000000000)
          lmList.append([id,cx,cy,cz])
        print(lmList[0])
        #distY = lmList[0][2] - lmList[5][2]
        #distYf = [dist(lmList[0][1]-lmList[4][1],lmList[0][2]-lmList[4][2]),dist(lmList[0][1]-lmList[8][1],lmList[0][2]-lmList[8][2]), dist(lmList[0][1]-lmList[12][1],lmList[0][2]-lmList[12][2]),dist(lmList[0][1]-lmList[16][1],lmList[0][2]-lmList[16][2]),dist(lmList[0][1]-lmList[20][1],lmList[0][2]-lmList[20][2])]
        #print(distYf)    
        cv2.putText(img,str(1), (lmList[4][1],lmList[4][2]), cv2.FONT_HERSHEY_SIMPLEX,1,(209,80,0,255),3)
        cv2.putText(img,str(2), (lmList[8][1],lmList[8][2]), cv2.FONT_HERSHEY_SIMPLEX,1,(209,80,0,255),3)
        cv2.putText(img,str(3), (lmList[12][1],lmList[12][2]), cv2.FONT_HERSHEY_SIMPLEX,1,(209,80,0,255),3)
        cv2.putText(img,str(4), (lmList[16][1],lmList[16][2]), cv2.FONT_HERSHEY_SIMPLEX,1,(209,80,0,255),3)
        cv2.putText(img,str(5), (lmList[20][1],lmList[20][2]), cv2.FONT_HERSHEY_SIMPLEX,1,(209,80,0,255),3)
        cv2.line(img,(lmList[0][1],lmList[0][2]),(lmList[5][1],lmList[5][2]),(255,255,255),4)
        cv2.circle(img, ((lmList[0][1] + lmList[5][1])//2, (lmList[0][2] + lmList[5][2])//2), 0,(0,0,0),8)
        #cv2.putText(img,str(distY), ((lmList[0][1] + lmList[5][1])//2, (lmList[0][2] + lmList[5][2])//2), cv2.FONT_HERSHEY_SIMPLEX,1,(209,80,0,255),3)
        '''if distY>0:
          isHandDetected = 1
        else:
          isHandDetected = 0'''
      img = cv2.flip(img, 1)
      cv2.imshow('MediaPipe Hands', cv2.flip(img, 1))
      key = cv2.waitKey(1)
      if key==ord("q"):
        val = 1
        print("done")
        break
cap.release()
cv2.destroyAllWindows()