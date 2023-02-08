import tkinter as tk

import customtkinter as ctk

import pandas as pd 
import numpy as np 
import pickle 
import mediapipe as mp 
import cv2 
from PIL import Image, ImageTk
from landmarks import landmarks

app = tk.Tk()
app.geometry('480x700')
app.title('Detecta Poses App')
ctk.set_appearance_mode('dark')

class_label   = ctk.CTkLabel(app, height=40, width=120, text_font=('Arial', 20), text_color='black')
class_label.place(x=10, y =1)
class_label.configure(text='ESTADO')

counter_label = ctk.CTkLabel(app, height=40, width=120, text_font=('Arial', 20), text_color='black')
counter_label.place(x=160,y=1)
counter_label.configure(text='CONTAR')

prob_label    = ctk.CTkLabel(app, height=40, width=120, text_font=('Arial', 20), text_color='black')
prob_label.place(x=300, y=1)
prob_label.configure(text='PROBA')

class_box      = ctk.CTkLabel(app, height=40, width=120, text_font=('Arial', 20), text_color='black', fg_color='blue')
class_box.place(x=10, y=41)
class_box.configure(text='0')

counter_box		= ctk.CTkLabel(app, height=40, width=120, text_font=('Arial', 20), text_color='white', fg_color='blue')
counter_box.place(x=160, y=41)
counter_box.configure(text='0')

prob_box		= ctk.CTkLabel(app, height=40, width=120, text_font=('Arial', 20), text_color='white', fg_color='blue')
prob_box.place(x=300, y=41)
prob_box.configure(text='0')


def reset_counter():
	global counter
	counter = 0


button = ctk.CTkButton(app, text='RESET', command=reset_counter,  height=40, width=120, text_font=('Arial', 20), text_color='white', fg_color='blue')
button.place(x=10, y=650)

frame = tk.Frame(height=480, width=480)
frame.place(x=10, y=90)
lmain = tk.Label(frame)
lmain.place(x=0, y=0)


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)

with open('manos.pkl', 'rb') as f:
	model = pickle.load(f)

cap = cv2.VideoCapture(0)
current_stage = ''
counter = 0

body_language_prob  = np.array([0,0])
body_language_class =  ''


def detect():
	global current_stage
	global counter
	global body_language_class
	global body_language_prob

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


detect()





app.mainloop()


