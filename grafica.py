import wx
from random import randint
from Tkinter import *
import tkMessageBox
import win32api
matrice=[[4,1,7,3,6,9,8,2,5],[6,3,2,1,5,8,9,4,7],[9,5,8,7,2,4,3,1,6],[8,2,5,4,3,7,1,6,9,],[7,9,1,5,8,6,4,3,2],[3,4,6,9,1,2,7,5,8],[2,8,9,6,4,3,5,7,1],[5,7,3,2,9,1,6,8,4],[1,6,4,8,7,5,2,9,3]]
mateasy=[[4,1,7,3,6,9,8,2,5],[6,3,2,1,5,8,9,4,7],[9,5,8,7,2,4,3,1,6],[8,2,5,4,3,7,1,6,9,],[7,9,1,5,8,6,4,3,2],[3,4,6,9,1,2,7,5,8],[2,8,9,6,4,3,5,7,1],[5,7,3,2,9,1,6,8,4],[1,6,4,8,7,5,2,9,3]]
casute=[]
class fr(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'SUDOKU',size=(400,400))
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
		game.Show()
	def sudoku2(self,event):
		game=MyCustomFrame2(parent=None,id=-1)
		game.Show()
	def sudoku3(self,event):
		game=MyCustomFrame3(parent=None,id=-1)
		game.Show()
class fr2(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'How To Play Sudoku',pos=(500,200),size=(400,400))
		panel=wx.Panel(self)
		text=wx.StaticText(panel,-1,"Rules of playing sudoku", (150,30))
class MyCustomFrame(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'SUDOKU - Easy Mode',size=(481,553))
		panel=wx.Panel(self)
		font2 = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
		button_verificare=wx.Button(self, label="Verify", pos=(156,466), size=(152,46))	
		button_verificare.SetFont(font2)
		self.Bind(wx.EVT_BUTTON,self.Verify, button_verificare)
		self.Bind(wx.EVT_PAINT,self.OnPaint)
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
		a=0
		list_verif=[]
		for nr1 in range (9):
			aux=[]
			for nr2 in range (9):
				aux.append(int(casute[a].GetValue().strip()))
				a=a+1
			list_verif.append(aux)
		print(list_verif,"\n")
		print(matrice)
		if list_verif!=matrice:
			win32api.MessageBox(0,'Desole ! Il y a encore des chiffres mal mises !','Erreur')
		else:
			win32api.MessageBox(0,'Felicitations ! Vous avez fini le jeu !','Fin du jeu')
class MyCustomFrame2(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'SUDOKU - Medium Mode',size=(481,553))
		panel=wx.Panel(self)
		font2 = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
		button_verificare=wx.Button(self, label="Verify", pos=(156,466), size=(152,46))	
		button_verificare.SetFont(font2)
		self.Bind(wx.EVT_BUTTON,self.Verify, button_verificare)
		self.Bind(wx.EVT_PAINT,self.OnPaint)
		font1 = wx.Font(24, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
		for k in range(55):
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
		a=0
		list_verif=[]
		for nr1 in range (9):
			aux=[]
			for nr2 in range (9):
				aux.append(int(casute[a].GetValue().strip()))
				a=a+1
			list_verif.append(aux)
		print(list_verif,"\n")
		print(matrice)
		if list_verif!=matrice:
			win32api.MessageBox(0,'Desole ! Il y a encore des chiffres mal mises !','Erreur')
		else:
			win32api.MessageBox(0,'Felicitations ! Vous avez fini le jeu !','Fin du jeu')
class MyCustomFrame3(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'SUDOKU - Hard Mode',size=(481,553))
		panel=wx.Panel(self)
		font2 = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
		button_verificare=wx.Button(self, label="Verify", pos=(156,466), size=(152,46))	
		button_verificare.SetFont(font2)
		self.Bind(wx.EVT_BUTTON,self.Verify, button_verificare)
		self.Bind(wx.EVT_PAINT,self.OnPaint)
		font1 = wx.Font(24, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
		for k in range(60):
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
		a=0
		list_verif=[]
		for nr1 in range (9):
			aux=[]
			for nr2 in range (9):
				aux.append(int(casute[a].GetValue().strip()))
				a=a+1
			list_verif.append(aux)
		print(list_verif,"\n")
		print(matrice)
		if list_verif!=matrice:
			win32api.MessageBox(0,'Desole ! Il y a encore des chiffres mal mises !','Erreur')
		else:
			win32api.MessageBox(0,'Felicitations ! Vous avez fini le jeu !','Fin du jeu')
# class   MyCustomPanel(wx.Panel):
		# def __init__(self,parent,id):
			# wx.Panel.__init__(self,parent,id)
			# self.sz =   wx.GridSizer(5,5,0,0)
			# for i   in  range(25):
				# self.sz.Add(wx.StaticText(self,-1,str(i)))
			# self.SetSizer(self.sz)
			# self.Bind(wx.EVT_PAINT,self.OnPaint)
		# def OnPaint(self,evt):
			# self.dc =   dc  =   wx.PaintDC(self)
			# w,h = self.sz.GetSize()
			# nr = self.sz.GetRows()
			# nc = self.sz.GetCols()
			# cell_w = float(w)/nc
			# cell_h = float(h)/nr
			# hlines = [(0,i*cell_h,w,i*cell_h)for i in range(nr+1)]
			# vlines = [(i*cell_w,0,i*cell_w,h)for i in range(nc+1)]
			# self.dc.DrawLineList(hlines+vlines)
if __name__ == '__main__':
	app=wx.PySimpleApp()
	frame=fr(parent=None,id=-1)
	frame.Show()
	app.MainLoop()