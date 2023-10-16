import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

mp_drawing=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands

cap=cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret,frame=cap.read()

        #detection
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        #flip on horizontal
        image=cv2.flip(image,1)
        
        #set flag
        image.flags.writeable=False

        #detection
        results=hands.process(image)

        #set flag to true
        image.flags.writeable=True

        #RGB to BGR
        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        cv2.putText(image,'Press button q to exit',(10,60),cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 0), 1, cv2.LINE_AA)

        #rendering results
        if results.multi_hand_landmarks:
            for num,hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,0,0),thickness=2,circle_radius=2),
                mp_drawing.DrawingSpec(color=(0,255,0),thickness=2,circle_radius=2))

        cv2.imshow('Hand Tracking',image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()