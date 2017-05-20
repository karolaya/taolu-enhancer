import tkinter as tk
from PIL import Image, ImageTk
import time


class Application(tk.Frame):
	def __init__(self, master=tk.Tk()):
		super().__init__(master, width=1024, height=512, bg='black')
		self.root = master
		self.root.title('Taolu  Enhancer - no active session')
		self.photo = 1
		self.pack()

		# initialize elements
		self._menubar = tk.Menu(master)
		self._video_holder = tk.Label(self) 
		self.loadMenu()
		
		

	def loadMenu(self):
		self._menubar.add_command(label='File', command=self.hello)
		self._menubar.add_command(label='Exit', command=self.root.quit)
		self.root.config(menu=self._menubar)

	# LoadVideoHolder receives a numpy array as a parameter
	def loadVideoHolder(self, img):
		img = Image.fromarray(img, 'RGB')
		self.photo = ImageTk.PhotoImage(img)
		self._video_holder.imgtk = self.photo
		self._video_holder.config(image = self.photo)
		self._video_holder.pack()

	def hello(self):
		print('hello')