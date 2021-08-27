import tkinter as tk 
from tkinter import ttk 
import time
import random

#set font style & size
LARGEFONT =("Verdana", 35) 
font_style = ("Ubuntu Mono", 16)


class benchmarkApp(tk.Tk): 
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk 
		tk.Tk.__init__(self, *args, **kwargs) 
		
		# creating a container
		self.title("Benchmark")
		#self.iconbitmap('bcm.ico') 
		self.config(bg = "#f4f4f4")
		self.geometry("550x500")
		container = tk.Frame(self, bg = "#f4f4f4") 
		container.pack(side = "top", fill = "both", expand = True ) 

		# initializing frames to an empty array 
		self.frames = {} 

		# iterating through a tuple consisting of the different page layouts 
		for F in (StartPage, Cpupage, ProgressBarPage_CPU, Diskpage, ProgressBarPage_Disk, RAMpage, ProgressBarPage_RAM, Overallpage, ProgressBarPage_Overall, aboutpage): 

			frame = F(container, self) 

			# initializing frame of that object 
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew") 

		self.show_frame(StartPage) 

	# to display the current frame passed as parameter 
	def show_frame(self, cont): 
		frame = self.frames[cont] 
		frame.tkraise() 


# first window frame startpage 
class StartPage(tk.Frame): 
	def __init__(self, parent, controller): 
		#set up style of starter page
		tk.Frame.__init__(self, parent, bg = "#f4f4f4") 

		# set up label & button of frame welcome 
		label_welcome = ttk.Label(self, text = "Welcome to Benchmark Program", font=("Helvetica", 16))
		label_menu = ttk.Label(self, text = "Select the benchmark Test")
		button_CPU = ttk.Button(self, text = "CPU", 
							command = lambda : controller.show_frame(Cpupage))
		button_Disk = ttk.Button(self, text = "Disk Read Speed", 
							command = lambda : controller.show_frame(Diskpage)) 
		button_RAM = ttk.Button(self, text = "RAM", 
							command = lambda : controller.show_frame(RAMpage))
		button_OverallTest = ttk.Button(self, text = "Overall Test", 
							command = lambda : controller.show_frame(Overallpage))
		button_exit = ttk.Button(self, text = "Exit", command = self.quit)
		button_info = ttk.Button(self, text = "About", 
							command = lambda : controller.show_frame(aboutpage))
		
		# putting label and button to the screen
		label_welcome.grid(row = 0, column = 60, pady = 10)
		label_menu.grid(row = 1, column = 60, padx = 110, pady = 10)
		button_CPU.grid(row = 2, column = 60, pady = 10, ipadx = 38, ipady = 20)
		button_Disk.grid(row = 3, column = 60, pady = 10, ipadx = 28, ipady = 20)
		button_RAM.grid(row = 4, column = 60, pady = 10, ipadx = 38, ipady = 20)
		button_OverallTest.grid(row = 5, column = 60, pady = 10, ipadx = 38, ipady = 20)
		button_exit.grid(row = 6, column = 5, padx = 10, pady = 25)
		button_info.grid(row = 6, column = 61, padx = 5, pady = 25)


# second window frame CPU Test page 
class Cpupage(tk.Frame): 
	
	def __init__(self, parent, controller): 
		
		#set up style of starter page
		tk.Frame.__init__(self, parent, bg = "#f4f4f4") 

		# set up label & button of frame CPU page
		label_welcome = ttk.Label(self, text = "This is CPU Benchmark Test")
		lebel_about = ttk.Label(self, text = "How it works: ")
		lebel_info1 = ttk.Label(self, text = "use metrix for CPU Benchmark")
		lebel_info2 = ttk.Label(self, text = "highest score is 10 pts")
		label_welcome.grid(row = 0, column = 3, padx = 1, pady = 10 )
		lebel_about.grid(row = 1, column = 3, padx = 1, pady = 10)
		lebel_info1.grid(row = 2, column = 3, padx = 1, pady = 10)
		lebel_info2.grid(row = 3, column = 3, padx = 1, pady = 10)
		button_Yes = ttk.Button(self, text ="Yes",
							command = lambda : controller.show_frame(ProgressBarPage_CPU))
		button_Cancel = ttk.Button(self, text ="Cancel", 
							command = lambda : controller.show_frame(StartPage))
		button_back = ttk.Button(self, text ="Back", 
							command = lambda : controller.show_frame(StartPage)) 
		
		# putting the button and label to the sceen
		button_Yes.grid(row = 7, column = 2, padx = 5, pady = 10) 
		button_Cancel.grid(row = 7, column = 11, padx = 5, pady = 10) 
		button_back.grid(row = 10, column = 1, padx = 10, pady = 10) 


class ProgressBarPage_CPU(tk.Frame):
	def __init__(self, parent, controller): 
		
		#set up style of CPU Speed Test page
		tk.Frame.__init__(self, parent, bg = "#f4f4f4") 

		# set up label & button of frame CPU benchmark page
		label_welcome = ttk.Label(self, text = "This is CPU Benchmark Test")
		lebel_about = ttk.Label(self, text = "How it works: ")
		lebel_info1 = ttk.Label(self, text = "use metrix for CPU benchmark")
		lebel_info2 = ttk.Label(self, text = "highest score is 10 pts")
		lebel_wait = ttk.Label(self, text = "Let's start Wait a moment....")
		button_Cancel = ttk.Button(self, text ="Cancel", 
							command = lambda : controller.show_frame(StartPage))
		button_runbenchmark = ttk.Button(self, text = "Run Benchmark", command = self.run_progressbar)
		button_back = ttk.Button(self, text ="Back", 
							command = lambda : controller.show_frame(StartPage))

		# putting label and button to the screen
		label_welcome.grid(row = 0, column = 3, padx = 1, pady = 10 )
		lebel_about.grid(row = 1, column = 3, padx = 1, pady = 10)
		lebel_info1.grid(row = 2, column = 3, padx = 1, pady = 10)
		lebel_info2.grid(row = 3, column = 3, padx = 1, pady = 10)
		button_Yes = ttk.Button(self, text ="Yes", state=tk.DISABLED)
		button_Yes.grid(row = 5, column = 2, padx = 1, pady = 10) 
		lebel_wait.grid(row = 6, column = 3, padx = 1, pady = 10)
		button_Cancel.grid(row = 5, column = 5, padx = 1, pady = 10) 
		button_runbenchmark.grid(row = 7, column = 3, pady = 5)
		button_back.grid(row = 11, column = 1, padx = 7, pady = 10) 

		#create a progress bar
		self.progress_bar = ttk.Progressbar(self, orient = 'horizontal', length = 286, mode = 'determinate')

		#put progress bar show on the screen
		self.progress_bar.grid(row = 8, column = 3, pady = 10)

	#create function start benchmark test
	def run_progressbar(self):
		matrix = [] 
		matrix_add = [] #เก็บค่า matrix บวกmatrix
		matrix_mul = [] #เก็บค่าการคูณค่าคงที่กับ matrix
		constrant = random.randint(0,1000) #สุ่มค่าคงที่

		#ระยะจำนวนช่องภายในprogress bar
		self.progress_bar["maximum"] = 3

		matrix = [] 
		matrix_add = [] #เก็บค่า matrix บวกmatrix
		matrix_mul = [] #เก็บค่าการคูณค่าคงที่กับ matrix
		constrant = random.randint(0,1000) #สุ่มค่าคงที่
		#define time from start 
		time_start = time.time()

		#วนเพื่อเริ่มการทำงานbenchmark
		for i in range(1):
			for j in range(2500):
				col = []
				for k in range(2500):
					col.append(random.uniform(0,1))
					matrix.append(col)
			
			#update status of progress bar
			self.progress_bar["value"] = 1
			self.progress_bar.update()

		for i in range(2):
			for j in range(2500):
				col = []
				for k in range(2500):
					add = matrix[j][k] + matrix[j][k] 
					col.append(add)
				matrix_add.append(col)

			self.progress_bar["value"] = 2
			self.progress_bar.update()

		for i in range(3):
			for j in range(2500):
				col = []
				for k in range(2500):
					multiple = constrant * matrix[j][k]
					col.append(multiple)
				matrix_mul.append(col)
			
			self.progress_bar["value"] = 3
			self.progress_bar.update()

		time_end = time.time() - time_start
		score = 10 - (time_end * (1/25))
		score_4decimal = format(score, '.4f')

		# label of frame score benchmark test 
		label_score = ttk.Label(self, text = "Your CPU speed scores: " + str(score_4decimal) + " Pts")
		
		# putting label score benchmark test to the screen
		label_score.grid(row = 10, column = 3, padx = 1, pady = 10)

	"""
	def stop_progress(self, *args):
		value = self.progress_bar['value']
		self.progress_bar.stop()
		self.progress_bar['value'] = value 
	"""

#"_________________________________________________________________________________________________________"


# second window frame Disk Read Speed Test page 
class Diskpage(tk.Frame): 
	
	def __init__(self, parent, controller): 
		
		#set up style of  Disk Read Speed Test page
		tk.Frame.__init__(self, parent, bg = "#f4f4f4") 

		# create label and button of frame Disk Page 
		label_welcome = ttk.Label(self, text = "This is Storage Disk Read Benchmark Test")
		lebel_about = ttk.Label(self, text = "How it works: ")
		lebel_info1 = ttk.Label(self, text = "Use read file for Disk read Benchmark")
		lebel_info2 = ttk.Label(self, text = "highest score is 10 pts")
		button_Yes = ttk.Button(self, text ="Yes", 
							command = lambda : controller.show_frame(ProgressBarPage_Disk))
		button_Cancel = ttk.Button(self, text ="Cancel", 
							command = lambda : controller.show_frame(StartPage))
		button_back = ttk.Button(self, text ="Back", 
							command = lambda : controller.show_frame(StartPage)) 

		# putting label and button to the screen
		label_welcome.grid(row = 0, column = 3, padx = 1, pady = 10 )
		lebel_about.grid(row = 1, column = 3, padx = 1, pady = 10)
		lebel_info1.grid(row = 2, column = 3, padx = 1, pady = 10)
		lebel_info2.grid(row = 3, column = 3, padx = 1, pady = 10)
		button_Yes.grid(row = 7, column = 2, padx = 5, pady = 10) 
		button_Cancel.grid(row = 7, column = 11, padx = 5, pady = 10) 
		button_back.grid(row = 10, column = 1, padx = 10, pady = 10) 

class ProgressBarPage_Disk(tk.Frame):
	def __init__(self, parent, controller): 
		
		#set up style of  Disk Read Speed Test page
		tk.Frame.__init__(self, parent, bg = "#f4f4f4") 

		# create label and button of frame Disk Page
		label_welcome = ttk.Label(self, text = "This is Storage Disk Read Benchmark Test")
		lebel_about = ttk.Label(self, text = "How it works:  ") 
		lebel_info1 = ttk.Label(self, text = "Use read file for Disk read Benchmark")
		lebel_info2 = ttk.Label(self, text = "highest score is 10 pts")
		button_Yes = ttk.Button(self, text ="Yes", state=tk.DISABLED)
		lebel_wait = ttk.Label(self, text = "Let's start Wait a moment....")
		button_Cancel = ttk.Button(self, text ="Cancel", 
							command = lambda : controller.show_frame(StartPage))
		button_runbenchmark = ttk.Button(self, text = "Run Benchmark", command = self.run_progressbar)
		button_back = ttk.Button(self, text ="Back", 
							command = lambda : controller.show_frame(StartPage)) 

		# putting label and button to the screen
		label_welcome.grid(row = 0, column = 3, padx = 1, pady = 10 )
		lebel_about.grid(row = 1, column = 3, padx = 1, pady = 10)
		lebel_info1.grid(row = 2, column = 3, padx = 1, pady = 10)
		lebel_info2.grid(row = 3, column = 3, padx = 1, pady = 10)
		button_Yes.grid(row = 5, column = 2, padx = 1, pady = 10) 
		lebel_wait.grid(row = 6, column = 3, padx = 1, pady = 10)
		button_runbenchmark.grid(row = 7, column = 3, pady = 5)
		button_back.grid(row = 11, column = 1, padx = 7, pady = 10)
		button_Cancel.grid(row = 5, column = 5, padx = 1, pady = 10) 

		#create a progress bar
		self.progress_bar = ttk.Progressbar(self, orient = 'horizontal', length = 286, mode = 'determinate')

		#put progress bar show on the screen
		self.progress_bar.grid(row = 8, column = 3, pady = 10)
	
	#create function start benchmark test
	def run_progressbar(self, *args):
		#Open file IO
		my_file = open("read a.txt","r")

		#ระยะจำนวนช่องภายในprogress bar
		self.progress_bar["maximum"] = int((25769790582/4000) / 10000)

		#define time from start 
		time_start = time.time()

		#วนเพื่อเริ่มการทำงานbenchmark
		for i in range( int((25769790582/4000) / 10000) ):
			# พยายามอ่านไฟล์ให้แบ่งเป็น 100 ตัว
			for j in range(10000):
				#read the file text
				my_file.read()
			
			#update status of progress bar
			self.progress_bar["value"] = i
			self.progress_bar.update()

		finishtime = time.time() - time_start
		score = 10 -(finishtime* (1/25))
		score_4decimal = format(score, '.4f')

		# label of frame score benchmark test 
		lebel_point = ttk.Label(self, text = "Your Disk Read speed score : " + str(score_4decimal) + " Pts")

		# putting label score benchmark test to the screen
		lebel_point.grid(row = 10, column = 3, padx = 1, pady = 10)

		#Close file IO
		my_file.close()
	"""
	def stop_progress(self, *args):
		value = self.progress_bar['value']
		self.progress_bar.stop()
		self.progress_bar['value'] = value 
	"""
#"_________________________________________________________________________________________________________"


# third window frame Disk Write Speed Test page 
class RAMpage(tk.Frame): 
	
	def __init__(self, parent, controller): 
		
		#set up style of starter page
		tk.Frame.__init__(self, parent, bg = "#f4f4f4") 

		# create label and button of frame RAM Page
		label_welcome = ttk.Label(self, text = "This is RAM Benchmark Test")
		lebel_about = ttk.Label(self, text = "How it works:  ")
		lebel_info1 = ttk.Label(self, text = "use random for RAM Brenchmark")
		lebel_info2 = ttk.Label(self, text = "highest score is 10 pts")
		button_Yes = ttk.Button(self, text ="Yes", 
							command = lambda : controller.show_frame(ProgressBarPage_RAM))
		button_Cancel = ttk.Button(self, text ="Cancel", 
							command = lambda : controller.show_frame(StartPage))

		# putting label and button to the screen
		label_welcome.grid(row = 0, column = 3, padx = 1, pady = 10 )
		lebel_about.grid(row = 1, column = 3, padx = 1, pady = 10)
		lebel_info1.grid(row = 2, column = 3, padx = 1, pady = 10)
		lebel_info2.grid(row = 3, column = 3, padx = 1, pady = 10)
		button_back = ttk.Button(self, text ="Back", 
							command = lambda : controller.show_frame(StartPage)) 
		button_Yes.grid(row = 7, column = 2, padx = 5, pady = 10) 
		button_Cancel.grid(row = 7, column = 11, padx = 5, pady = 10) 
		button_back.grid(row = 10, column = 1, padx = 10, pady = 10) 

class ProgressBarPage_RAM(tk.Frame):
	def __init__(self, parent, controller): 
		
		#set up style of CPU Speed Test page
		tk.Frame.__init__(self, parent, bg = "#f4f4f4") 

		# create label and button of frame RAM Page
		label_welcome = ttk.Label(self, text = "This is RAM Benchmark Test")
		lebel_about = ttk.Label(self, text = "How it works: ")
		lebel_info1 = ttk.Label(self, text = "use random for RAM Brenchmark")
		lebel_info2 = ttk.Label(self, text = "highest score is 10 pts")
		button_Yes = ttk.Button(self, text ="Yes", state=tk.DISABLED)
		lebel_wait = ttk.Label(self, text = "Let's start Wait a moment....")
		button_Cancel = ttk.Button(self, text ="Cancel", 
							command = lambda : controller.show_frame(StartPage))
		button_runbenchmark = ttk.Button(self, text = "Run Benchmark", command = self.run_progressbar)
		button_back = ttk.Button(self, text ="Back", 
							command = lambda : controller.show_frame(StartPage)) 

		# putting label and button to the screen
		label_welcome.grid(row = 0, column = 3, padx = 1, pady = 10 )
		lebel_about.grid(row = 1, column = 3, padx = 1, pady = 10)
		lebel_info1.grid(row = 2, column = 3, padx = 1, pady = 10)
		lebel_info2.grid(row = 3, column = 3, padx = 1, pady = 10)
		button_Yes.grid(row = 5, column = 2, padx = 1, pady = 10) 
		lebel_wait.grid(row = 6, column = 3, padx = 1, pady = 10)
		button_Cancel.grid(row = 5, column = 5, padx = 1, pady = 10) 
		button_runbenchmark.grid(row = 7, column = 3, pady = 5)
		button_back.grid(row = 11, column = 1, padx = 7, pady = 10)
		
		#create a progress bar
		self.progress_bar = ttk.Progressbar(self, orient = 'horizontal', length = 286, mode = 'determinate')

		#put progress bar show on the screen
		self.progress_bar.grid(row = 8, column = 3, pady = 10)

		#create function start benchmark test
	def run_progressbar(self):

		list_RAM = []
		#ระยะจำนวนช่องภายในprogress bar
		self.progress_bar["maximum"] = int(50000000 / 10000)

		#define time from start 
		time_start = time.time()

		#วนเพื่อเริ่มการทำงานbenchmark
		for i in range( int(50000000 / 10000) ):
			# พยายามอ่านไฟล์ให้แบ่งเป็น 100 ตัว
			for j in range(10000):
				add = random.random()
				list_RAM.append(add)
			
			#update status of progress bar
			self.progress_bar["value"] = i
			self.progress_bar.update()

		finaltime = time.time() - time_start
		score = 10-(finaltime*(1/20))
		score_4decimal = format(score, '.4f')
		
		# create label score benchmark test 
		lebel_score = ttk.Label(self, text = "Your RAM Score : " + str(score_4decimal) + " Pts")

		# putting label score benchmark test to the screen
		lebel_score.grid(row = 10, column = 3, padx = 1, pady = 10)
#"_________________________________________________________________________________________________________"


# forth window frame Overall benchmark test page 
class Overallpage(tk.Frame): 
	
	def __init__(self, parent, controller): 
		
		#set up style of Overall benchmark page
		tk.Frame.__init__(self, parent, bg = "#f4f4f4") 

		# create label and button of frame Overall benchmark page
		label_welcome = ttk.Label(self, text = "This is Overall Benchmark Test")
		lebel_about = ttk.Label(self, text = "How it works:  ")
		lebel_info1 = ttk.Label(self, text = "CPU Score + Disk Score + RAM Score")
		lebel_info2 = ttk.Label(self, text = "highest score is 30 pts.")
		button_Yes = ttk.Button(self, text ="Yes", 
							command = lambda : controller.show_frame(ProgressBarPage_Overall))
		button_Cancel = ttk.Button(self, text ="Cancel", 
							command = lambda : controller.show_frame(StartPage))
		button_back = ttk.Button(self, text ="Back", 
							command = lambda : controller.show_frame(StartPage)) 

		# putting label and button to the screen
		label_welcome.grid(row = 0, column = 3, padx = 1, pady = 10 )
		lebel_about.grid(row = 1, column = 3, padx = 1, pady = 10)
		lebel_info1.grid(row = 2, column = 3, padx = 1, pady = 10)
		lebel_info2.grid(row = 3, column = 3, padx = 1, pady = 10)
		button_Yes.grid(row = 7, column = 2, padx = 5, pady = 10) 
		button_Cancel.grid(row = 7, column = 11, padx = 5, pady = 10) 
		button_back.grid(row = 10, column = 1, padx = 10, pady = 10)

class ProgressBarPage_Overall(tk.Frame):
	def __init__(self, parent, controller): 
		
		#set up style of Overall benchmark test pag
		tk.Frame.__init__(self, parent, bg = "#f4f4f4") 

		# create label and button of frame Overall benchmark page
		label_welcome = ttk.Label(self, text = "This is Overall Benchmark Test")
		lebel_about = ttk.Label(self, text = "How it works: ")
		lebel_info1 = ttk.Label(self, text = "CPU Score + Disk Score + RAM Score")
		lebel_info2 = ttk.Label(self, text = "highest score is 30 pts.")
		button_Yes = ttk.Button(self, text ="Yes", state=tk.DISABLED)
		lebel_wait = ttk.Label(self, text = "Let's start Wait a moment....")
		button_Cancel = ttk.Button(self, text ="Cancel", 
							command = lambda : controller.show_frame(StartPage))
		button_runbenchmark = ttk.Button(self, text = "Run Benchmark", command = self.run_progressbar)
		button_back = ttk.Button(self, text ="Back", 
							command = lambda : controller.show_frame(StartPage)) 

		# putting label welcome to the screen
		label_welcome.grid(row = 0, column = 3, padx = 1, pady = 10 )
		lebel_about.grid(row = 1, column = 3, padx = 1, pady = 10)
		lebel_info1.grid(row = 2, column = 3, padx = 1, pady = 10)
		lebel_info2.grid(row = 3, column = 3, padx = 1, pady = 10)
		button_Yes.grid(row = 5, column = 2, padx = 1, pady = 10) 
		lebel_wait.grid(row = 6, column = 3, padx = 1, pady = 10)
		button_Cancel.grid(row = 5, column = 5, padx = 1, pady = 10) 
		button_runbenchmark.grid(row = 7, column = 3, pady = 5)
		button_back.grid(row = 11, column = 1, padx = 7, pady = 10) 

		#create a progress bar
		self.progress_bar = ttk.Progressbar(self, orient = 'horizontal', length = 286, mode = 'determinate')

		#put progress bar show on the screen
		self.progress_bar.grid(row = 8, column = 3, pady = 10)

	#create function start benchmark test
	def run_progressbar(self):

		matrix = [] 
		matrix_add = [] #เก็บค่า matrix บวกmatrix
		matrix_mul = [] #เก็บค่าการคูณค่าคงที่กับ matrix
		constrant = random.randint(0,1000) #สุ่มค่าคงที่

		#ระยะจำนวนช่องภายในprogress bar
		self.progress_bar["maximum"] = 10

		matrix = [] 
		matrix_add = [] #เก็บค่า matrix บวกmatrix
		matrix_mul = [] #เก็บค่าการคูณค่าคงที่กับ matrix
		constrant = random.randint(0,1000) #สุ่มค่าคงที่
		#define time from start 
		time_start_CPU = time.time()

		#วนเพื่อเริ่มการทำงานbenchmark
		for i in range(2):
			for j in range(2500):
				col = []
				for k in range(2500):
					col.append(random.uniform(0,1))
					matrix.append(col)
			
			#update status of progress bar
			self.progress_bar["value"] = 2
			self.progress_bar.update()

		for i in range(4):
			for j in range(2500):
				col = []
				for k in range(2500):
					add = matrix[j][k] + matrix[j][k] 
					col.append(add)
				matrix_add.append(col)

			self.progress_bar["value"] = 4
			self.progress_bar.update()

		for i in range(6):
			for j in range(2500):
				col = []
				for k in range(2500):
					multiple = constrant * matrix[j][k]
					col.append(multiple)
				matrix_mul.append(col)
			
			self.progress_bar["value"] = 6
			self.progress_bar.update()

		time_end_CPU = time.time() - time_start_CPU
		score_CPU = 10 - (time_end_CPU * (1/25))
		score_4decimal_CPU = format(score_CPU, '.4f')


		#Open file IO
		my_file = open("read a.txt","r")

		#define time from start 
		time_start_Disk = time.time()

		#วนเพื่อเริ่มการทำงานbenchmark
		for i in range( 8 ):
			for j in range(int((1073741824/4000))):
				#read the file text
				my_file.read()
			
			#update status of progress bar
			self.progress_bar["value"] = 8
			self.progress_bar.update()

		finishtime_Disk = time.time() - time_start_Disk
		score_Disk = 10 -( finishtime_Disk * (1/25))
		score_4decimal_Disk = format(score_Disk, '.4f')
		

		list_RAM = []
		#define time from start 
		time_start_RAM = time.time()

		#วนเพื่อเริ่มการทำงานbenchmark
		for i in range( 10 ):
			for j in range(int(5000)):
				add = random.random()
				list_RAM.append(add)
			
			#update status of progress bar
			self.progress_bar["value"] = 10
			self.progress_bar.update()

		finaltime_RAM = time.time() - time_start_RAM
		score_RAM = 10 - ( finaltime_RAM * (1/20) )
		score_4decimal_RAM  = format(score_RAM, '.4f')

		total_score = score_CPU + score_Disk + score_RAM
		score_4decimal_total  = format(total_score, '.4f')
		
		label_total_score = ttk.Label(self, text = "Your Overall Score : " + str(score_4decimal_total) + " Pts")

		# putting label score benchmark test to the screen
		label_total_score.grid(row = 9, column = 3, padx = 1, pady = 10)
#"_________________________________________________________________________________________________________"


# fifth window frame about this program 
class aboutpage(tk.Frame): 

	def __init__(self, parent, controller): 

		#set up style of aboute page
		tk.Frame.__init__(self, parent, bg = "gray") 

		# create label and button of frame about page
		label_welcome = ttk.Label(self, text = "This is Benchmark Test Program for CN210")
		label_about = ttk.Label(self, text = "made from :")
		label_info1 = ttk.Label(self, text = "M Irsyad Bahy Arkan   6210742281")
		label_info2 = ttk.Label(self, text = "Natdanai Lornimitdee   6210742224")
		label_info3 = ttk.Label(self, text = "Thitiporn tangkantitham   6210743131")
		label_info4 = ttk.Label(self, text = "Witchayada Sirirangsiyothai  6210743016")
		button_back = ttk.Button(self, text ="Back", 
							command = lambda : controller.show_frame(StartPage))

		# putting label and button to the screen
		label_welcome.grid(row = 0, column = 60, pady = 10 )
		label_about.grid(row = 1, column = 60, padx = 90, pady = 10)
		label_info1.grid(row = 2, column = 60, padx = 90, pady = 10)
		label_info2.grid(row = 3, column = 60, padx = 90, pady = 10)
		label_info3.grid(row = 4, column = 60, padx = 90, pady = 10)
		label_info4.grid(row = 5, column = 60, padx = 90, pady = 10)
		button_back.grid(row = 10, column = 1, padx = 10, pady = 10) 
#"_________________________________________________________________________________________________________"


# Driver Code 
app = benchmarkApp() 
app.mainloop() 
