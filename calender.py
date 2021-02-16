from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys 


class Window(QMainWindow): 

	def __init__(self): 
		super().__init__() 

		self.setWindowTitle("Python ") 
		self.setGeometry(100, 100, 600, 400) 
		self.UiComponents() 
		self.show() 

	def UiComponents(self): 

		calender = QCalendarWidget(self) 
		calender.setGeometry(10, 10, 400, 250) 

		title = "Calendar by shourov"
		calender.setWindowTitle(title) 

		
App = QApplication(sys.argv) 
window = Window() 
sys.exit(App.exec()) 
