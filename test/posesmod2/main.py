import cv2
import mediapipe as mp
import numpy as np
import PoseModule as pm



cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
direction = 0
form = 0
feedback = "Corregir"


while cap.isOpened():
    ret, img = cap.read() #640 x 480
    #Determine dimensions of video - Help with creation of box in Line 43
    width  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `width`
    height = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float `height`
    # print(width, height)
    
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        elbow = detector.findAngle(img, 11, 13, 15)
        shoulder = detector.findAngle(img, 13, 11, 23)
        hip = detector.findAngle(img, 11, 23,25)
        
        # % de flexiones correctas
        per = np.interp(elbow, (90, 160), (0, 100))
        
        #Barra para Mostrar el progreso de flexiones
        bar = np.interp(elbow, (90, 160), (380, 50))

        #Check to ensure right form before starting the program
        if elbow > 160 and shoulder > 40 and hip > 160:
            form = 1
    
        #Check for full range of motion for the pushup
        if form == 1:
            if per == 0:
                if elbow <= 90 and hip > 160:
                    feedback = "Arriba"
                    if direction == 0:
                        count += 0.5
                        direction = 1
                else:
                    feedback = "Corregir"
                    
            if per == 100:
                if elbow > 160 and shoulder > 40 and hip > 160:
                    feedback = "Abajo"
                    if direction == 1:
                        count += 0.5
                        direction = 0
                else:
                    feedback = "Corregir"
                        # form = 0
                
                    
    
        print(count)
        
        #Barra
        if form == 1:
            cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
            cv2.rectangle(img, (580, int(bar)), (600, 380), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{int(per)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 0), 2)


        #contar flexiones
        cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5)
        
        #Devoluciones 
        cv2.rectangle(img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
        cv2.putText(img, feedback, (500, 40 ), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 255, 0), 2)

        
    cv2.imshow('Conteo Flexiones', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()