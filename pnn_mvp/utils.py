import cv2
import mediapipe as mp 
import pandas as pd 
import numpy as np 
from PIL import Image, ImageTk


def reset_counter():
	global counter
	counter = 0

def detect(cap, mp_drawing, mp_pose, counter, pose, lmain, counter_box, prob_box,class_box):
	global current_stage
	#global counter
	global body_language_class
	global body_language_prob
	body_language_prob  = np.array([0,0])
	body_language_class =  ''
	cap = cv2.VideoCapture(0)
	current_stage = ''
	counter = 0  
	ret , frame = cap.read()
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	result = pose.process(image)
	mp_drawing.draw_landmarks(image, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
		mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
		mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2),
		)


	try:
		row = np.array([[res.x, res.y, res.z, res.visibility] for res in result.pose_landmarks.landmark]).flatten().tolist()
		x = pd.DataFrame([row], columns= landmarks)
		body_language_prob = model.predict_proba(x)[0]
		body_language_class= model.predict(x)[0]
		
		if body_language_class or body_language_prob:
			print('predicted')
		else :
			print('prediction error')

		if body_language_class == "derecha" and body_language_prob[body_language_prob.argmax()] >= 0.7:
			current_stage = "derecha"
			
		elif current_stage=="derecha" and body_language_class=="izquierda" and body_language_prob[body_language_prob.argmax()] >= 0.7:
			current_stage = "izquierda"
			counter +=1
		
	except Exception as e:
		print(e)

	img = image[:, :460, :]
	imgarr = Image.fromarray(img)
	imgtk = ImageTk.PhotoImage(imgarr)
	lmain.imgtk = imgtk
	lmain.configure(image = imgtk)
	lmain.after(10, detect)

	counter_box.configure(text=counter)
	prob_box.configure(text=body_language_prob[body_language_prob.argmax()])
	class_box.configure(text=current_stage)