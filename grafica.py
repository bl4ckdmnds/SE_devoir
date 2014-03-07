import wx
import time
from random import randint
from Tkinter import *
import tkMessageBox
import threading,sys,logging
from threading import Lock
import win32api
import copy
matrice_easy=[[4,1,7,3,6,9,8,2,5],[6,3,2,1,5,8,9,4,7],[9,5,8,7,2,4,3,1,6],[8,2,5,4,3,7,1,6,9,],[7,9,1,5,8,6,4,3,2],[3,4,6,9,1,2,7,5,8],[2,8,9,6,4,3,5,7,1],[5,7,3,2,9,1,6,8,4],[1,6,4,8,7,5,2,9,3]]
matrice_med=[[1,4,5,3,2,7,6,9,8],[8,3,9,6,5,4,1,2,7],[6,7,2,9,1,8,5,4,3],[4,9,6,1,8,5,3,7,2],[2,1,8,4,7,3,9,5,6],[7,5,3,2,9,6,4,8,1],[3,6,7,5,4,2,8,1,9],[9,8,4,7,6,1,2,3,5],[5,2,1,8,3,9,7,6,4]]
matrice_hard=[[1,7,3,9,8,2,6,5,4],[6,5,2,1,7,4,8,9,3],[9,8,4,5,3,6,1,2,7],[7,2,9,4,1,5,3,6,8],[8,4,1,3,6,9,2,7,5],[5,3,6,8,2,7,4,1,9],[2,6,5,7,4,3,9,8,1],[4,1,7,2,9,8,5,3,6],[3,9,8,6,5,1,7,4,2]]
mateasy=[]
matmed=[]
mathard=[]
casute=[]
mutex = Lock()
#mutex.release()
start_time = time.time()
timp = time.time()
class fr(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'SUDOKU',style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER,size=(390,390))
		panel=wx.Panel(self)
		font2 = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
		button_easy=wx.Button(panel, label="Easy", pos=(140,100), size=(90,40))
		button_medium=wx.Button(panel, label="Medium", pos=(140,150), size=(90,40))
		button_hard=wx.Button(panel, label="Hard", pos=(140,200), size=(90,40))
		button_easy.SetFont(font2)
		button_medium.SetFont(font2)
		button_hard.SetFont(font2)
		self.Bind(wx.EVT_BUTTON,self.sudoku1, button_easy)
		self.Bind(wx.EVT_BUTTON,self.sudoku2, button_medium)
		self.Bind(wx.EVT_BUTTON,self.sudoku3, button_hard)
		status=self.CreateStatusBar()
		menubar=wx.MenuBar()
		first=wx.Menu()
		second=wx.Menu()
		open=first.Append(wx.NewId(),"Open","This will open a new window")
		exit=first.Append(wx.NewId(),"Exit","Exit the program")
		high=second.Append(wx.NewId(),"Highscore","Shows the top of your performances")
		howto=second.Append(wx.NewId(),"HowTo","Shows the sudoku rules")
		menubar.Append(first,"File")
		menubar.Append(second,"Game")
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU,self.closegame,exit)
		self.Bind(wx.EVT_MENU,self.showhelp,howto)
	def closegame(self,event):
		self.Close(True)
	def showhelp(self,event):
		helpwindow=fr2(parent=None,id=-1)
		helpwindow.Show()
	def sudoku1(self,event):
		game=MyCustomFrame(parent=None,id=-1)
		start_time = time.time()
		game.Show()
	def sudoku2(self,event):
		game=MyCustomFrame2(parent=None,id=-1)
		game.Show()
		start_time = time.time()
	def sudoku3(self,event):
		game=MyCustomFrame3(parent=None,id=-1)
		game.Show()
		start_time = time.time()
class fr2(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'How To Play Sudoku',style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER,pos=(500,200),size=(390,390))
		panel=wx.Panel(self)
		text=wx.StaticText(panel,-1,"Rules of playing sudoku", (150,30))
class MyCustomFrame(wx.Frame,threading.Thread):
		# if mutex.locked():
			# print("ERROR!!")
		# else:		
			def __init__(self,parent,id):
				mateasy=copy.deepcopy(matrice_easy)
				mutex.acquire()
				threading.Thread.__init__(self)
				wx.Frame.__init__(self,parent,id,'SUDOKU - Easy Mode',style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER,size=(471,543))
				panel=wx.Panel(self)
				font2 = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
				button_verificare=wx.Button(self, label="Verify", pos=(156,466), size=(152,46))	
				button_verificare.SetFont(font2)
				self.Bind(wx.EVT_BUTTON,self.Verify, button_verificare)
				self.Bind(wx.EVT_PAINT,self.OnPaint)
				self.Bind(wx.EVT_CLOSE,self.closewindow)
				font1 = wx.Font(24, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
				for k in range(45):
					x=randint(0,8)
					y=randint(0,8)
					if mateasy[x][y]!=' ':
						mateasy[x][y]=' '
					else: 
						k=k-1
				for i in range(9):
					for j in range(9):
						if (mateasy[i][j]!=' '):
							b=self.edit = wx.TextCtrl(self, style=wx.TE_CENTER|wx.TE_READONLY, pos=(52*i, 52*j),size=(48,48))
						else:
							b=self.edit = wx.TextCtrl(self, style=wx.TE_CENTER, pos=(52*i, 52*j),size=(48,48))
							b.SetForegroundColour(wx.BLUE)
						b.SetValue(str(mateasy[i][j]).strip())
						b.SetFont(font1)
						casute.append(b)
						b.Bind(wx.EVT_TEXT_ENTER, self.onAction)
			def closewindow(self,event):
				self.Destroy()
				mutex.release()
			def run(self):
				#logging.info("From %s(thread_name)\n" % {"thread_name":self.getName()})
				Thread1 = MyCustomFrame(parent=None,id=-1)
				print "Starting " + self.name
				Thread1 = Thread(target = MyCustomFrame.__init__)
				Thread1.start()
			def OnPaint(self,evt):
				self.dc = dc = wx.PaintDC(self)
				dc.BeginDrawing()
				dc.SetPen(wx.Pen("BLACK", 4))
				dc.DrawLine(154,0,154,462)
				dc.DrawLine(310,0,310,462)
				dc.DrawLine(0,154,462,154)
				dc.DrawLine(0,310,462,310)
				self.dc.EndDrawing()
			def onAction(self, event):
				raw_value = self.edit.GetValue().strip()
				if all(x in '0123456789.+-' for x in raw_value):
					self.value = round(float(raw_value), 2)
					self.edit.ChangeValue(str(self.value))
				else:
					self.edit.ChangeValue("Number only")
			def Verify(self, event):
				try:
					a=0
					list_verif=[]
					for nr1 in range (9):
						aux=[]
						for nr2 in range (9):
							aux.append(int(casute[a].GetValue().strip()))
							a=a+1
						list_verif.append(aux)
					print(list_verif,"\n")
					print(matrice_easy)
					if list_verif!=matrice_easy:
						win32api.MessageBox(0,'Desole ! Il y a encore des chiffres mal mises !','Erreur')
					else:
						timp = time.time() - start_time
						score=3000-int(timp)
						win32api.MessageBox(0,'Felicitations ! Vous avez fini le jeu avec le score: '+str(score)+' !','Fin du jeu')
				except:
					win32api.MessageBox(0,'Completez seulement avec des chiffres entre 1 et 9!','Erreur')
			#mutex.release()
class MyCustomFrame2(wx.Frame,threading.Thread):
		# if mutex.locked():
			# print("ERROR!!")
		# else:	
			def __init__(self,parent,id):
				mutex.acquire()
				mat_med=copy.deepcopy(matrice_med)
				threading.Thread.__init__(self)
				wx.Frame.__init__(self,parent,id,'SUDOKU - Medium Mode',style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER,size=(471,543))
				panel=wx.Panel(self)
				font2 = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
				button_verificare=wx.Button(self, label="Verify", pos=(156,466), size=(152,46))	
				button_verificare.SetFont(font2)
				self.Bind(wx.EVT_BUTTON,self.Verify, button_verificare)
				self.Bind(wx.EVT_PAINT,self.OnPaint)
				self.Bind(wx.EVT_CLOSE,self.closewindow)
				font1 = wx.Font(24, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
				for k in range(53):
					x=randint(0,8)
					y=randint(0,8)
					if mat_med[x][y]!=' ':
						mat_med[x][y]=' '
					else: 
						k=k-1
				for i in range(9):
					for j in range(9):
						if (mat_med[i][j]!=' '):
							b=self.edit = wx.TextCtrl(self, style=wx.TE_CENTER|wx.TE_READONLY, pos=(52*i, 52*j),size=(48,48))
						else:
							b=self.edit = wx.TextCtrl(self, style=wx.TE_CENTER, pos=(52*i, 52*j),size=(48,48))
							b.SetForegroundColour(wx.BLUE)
						b.SetValue(str(mat_med[i][j]).strip())
						b.SetFont(font1)
						casute.append(b)
						b.Bind(wx.EVT_TEXT_ENTER, self.onAction)
			def OnPaint(self,evt):
				self.dc = dc = wx.PaintDC(self)
				dc.BeginDrawing()
				dc.SetPen(wx.Pen("BLACK", 4))
				dc.DrawLine(154,0,154,462)
				dc.DrawLine(310,0,310,462)
				dc.DrawLine(0,154,462,154)
				dc.DrawLine(0,310,462,310)
				self.dc.EndDrawing()
			def run(self):
				#logging.info("From %s(thread_name)\n" % {"thread_name":self.getName()})
				Thread2 = MyCustomFrame2(parent=None,id=-1)
				print "Starting " + self.name
				Thread2 = Thread(target = self.__init__)
				Thread2.start()
			def closewindow(self,event):
				mutex.release()
				self.Destroy()
			def onAction(self, event):
				raw_value = self.edit.GetValue().strip()
				if all(x in '0123456789.+-' for x in raw_value):
					self.value = round(float(raw_value), 2)
					self.edit.ChangeValue(str(self.value))
				else:
					self.edit.ChangeValue("Number only")
			def Verify(self, event):
				try:
					a=0
					list_verif=[]
					for nr1 in range (9):
						aux=[]
						for nr2 in range (9):
							aux.append(int(casute[a].GetValue().strip()))
							a=a+1
						list_verif.append(aux)
					print(list_verif,"\n")
					if list_verif!=matrice_med:
						win32api.MessageBox(0,'Desole ! Il y a encore des chiffres mal mises !','Erreur')
					else:
						timp = time.time() - start_time
						score=4000-int(timp)
						win32api.MessageBox(0,'Felicitations ! Vous avez fini le jeu avec le score: '+str(score)+' !','Fin du jeu')
				except:
					win32api.MessageBox(0,'Completez seulement avec des chiffres entre 1 et 9!','Erreur')
class MyCustomFrame3(wx.Frame,threading.Thread):
		# if mutex.locked():
			# print("ERROR!!")
		# else:		
			def __init__(self,parent,id):
				mutex.acquire()
				mat_hard=copy.deepcopy(matrice_hard)
				threading.Thread.__init__(self)
				wx.Frame.__init__(self,parent,id,'SUDOKU - Hard Mode',style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER,size=(471,543))
				panel=wx.Panel(self)
				font2 = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
				button_verificare=wx.Button(self, label="Verify", pos=(156,466), size=(152,46))	
				button_verificare.SetFont(font2)
				self.Bind(wx.EVT_BUTTON,self.Verify, button_verificare)
				self.Bind(wx.EVT_PAINT,self.OnPaint)
				self.Bind(wx.EVT_CLOSE,self.closewindow)
				font1 = wx.Font(24, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
				for k in range(60):
					x=randint(0,8)
					y=randint(0,8)
					if mat_hard[x][y]!=' ':
						mat_hard[x][y]=' '
					else: 
						k=k-1
				for i in range(9):
					for j in range(9):
						if (mat_hard[i][j]!=' '):
							b=self.edit = wx.TextCtrl(self, style=wx.TE_CENTER|wx.TE_READONLY, pos=(52*i, 52*j),size=(48,48))
						else:
							b=self.edit = wx.TextCtrl(self, style=wx.TE_CENTER, pos=(52*i, 52*j),size=(48,48))
							b.SetForegroundColour(wx.BLUE)
						b.SetValue(str(mat_hard[i][j]).strip())
						b.SetFont(font1)
						casute.append(b)
						b.Bind(wx.EVT_TEXT_ENTER, self.onAction)
			def OnPaint(self,evt):
				self.dc = dc = wx.PaintDC(self)
				dc.BeginDrawing()
				dc.SetPen(wx.Pen("BLACK", 4))
				dc.DrawLine(154,0,154,462)
				dc.DrawLine(310,0,310,462)
				dc.DrawLine(0,154,462,154)
				dc.DrawLine(0,310,462,310)
				self.dc.EndDrawing()
			def run(self):
				#logging.info("From %s(thread_name)\n" % {"thread_name":self.getName()})
				Thread3 = MyCustomFrame3(parent=None,id=-1)
				print "Starting " + self.name
				Thread3 = Thread(target = self.__init__)
				Thread3.start()
			def closewindow(self,event):
				mutex.release()
				self.Destroy()
			def onAction(self, event):
				raw_value = self.edit.GetValue().strip()
				if all(x in '0123456789.+-' for x in raw_value):
					self.value = round(float(raw_value), 2)
					self.edit.ChangeValue(str(self.value))
				else:
					self.edit.ChangeValue("Number only")
			def Verify(self, event):
				try:
					a=0
					list_verif=[]
					for nr1 in range (9):
						aux=[]
						for nr2 in range (9):
							aux.append(int(casute[a].GetValue().strip()))
							a=a+1
						list_verif.append(aux)
					print(list_verif,"\n")
					#print(matrice)
					if list_verif!=matrice_hard:
						win32api.MessageBox(0,'Desole ! Il y a encore des chiffres mal mises !','Erreur')
					else:
						timp = time.time() - start_time
						score=5000-int(timp)
						win32api.MessageBox(0,'Felicitations ! Vous avez fini le jeu avec le score: '+str(score)+' !','Fin du jeu')
				except:
					win32api.MessageBox(0,'Completez seulement avec des chiffres entre 1 et 9!','Erreur')
if __name__ == '__main__':
	app=wx.PySimpleApp()
	frame=fr(parent=None,id=-1)
	frame.Show()
	app.MainLoop()