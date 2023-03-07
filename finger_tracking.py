import cv2
import mediapipe as mp

#initializing cv2
cap = cv2.VideoCapture(0)

#initializing mediapipe utilities
mp_draw = mp.solutions.drawing_utils
mp_draw_style = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

with mp_hands.Hands(model_complexity=0, min_detection_confidence=0.8, min_tracking_confidence=0.8) as hand:
  while cap.isOpened():
    success, img = cap.read()
    if not success:
      #Empty camera frame
      print("Empty Camera Frame")
      continue
     
