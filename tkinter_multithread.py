from ctypes import windll
from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import messagebox
import PIL
from PIL import ImageTk
import cv2

window = Tk()
window.title("Tkinter OpenCV")

video = cv2.VideoCapture(0)
# ret, frame = video.read()
# cv2.imshow("W", frame)

canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH) #// 2
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT) #// 2

canvas = Canvas(window, width=canvas_w, height=canvas_h, bg="red")
canvas.pack()

bw = 0

def handleBW():
    global bw
    bw = 1 - bw

btn = Button(window, text="Black and white", command=handleBW)
btn.pack()

photo = None

def update_frame():
    global canvas, photo, bw
    ret, frame = video.read()
    frame = cv2.resize(frame, dsize=None, fx=1, fy=1)
    if bw == 0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    photo = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    window.after(15, update_frame)

update_frame()

window.mainloop()