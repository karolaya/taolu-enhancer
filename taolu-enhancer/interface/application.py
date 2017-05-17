import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=tk.Tk()):
		super().__init__(master, width=1024, height=512)
		self.root = master
		self.root.title('Taolu  Enhancer - no active session')

		self.pack()
		
		# initialize menubar
		self._menubar = tk.Menu(master)
		self.load_menu()

	def load_menu(self):
		self._menubar.add_command(label='File', command=self.hello)
		self._menubar.add_command(label='Exit', command=self.root.quit)
		self.root.config(menu=self._menubar)

	def hello(self):
		print('hellos')