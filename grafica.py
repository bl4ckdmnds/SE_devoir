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
		button_easy=wx.Button(panel, label="Easy", pos=(170,100), size=(60,40))
		button_medium=wx.Button(panel, label="Medium", pos=(170,150), size=(60,40))
		button_hard=wx.Button(panel, label="Hard", pos=(170,200), size=(60,40))
		
		self.Bind(wx.EVT_BUTTON,self.sudoku, button_easy)
		self.Bind(wx.EVT_BUTTON,self.sudoku, button_medium)
		self.Bind(wx.EVT_BUTTON,self.sudoku, button_hard)
		
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
		
	def sudoku(self,event):
		game=MyCustomFrame(parent=None,id=-1)
		#panel2=MyCustomPanel(game,-1)
		game.Show()
		
	
class fr2(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'How To Play Sudoku',pos=(500,200),size=(400,400))
		panel=wx.Panel(self)
		
		
		text=wx.StaticText(panel,-1,"Rules of playing sudoku", (150,30))
		#custom.SetForegroundColour('blue')
		#custom.SetBackgroundColour('white')
	
# class gameframe(wx.Frame):
	# def __init__(self,parent,id):
		# wx.Frame.__init__(self,parent,id,'Sudoku v2.0',pos=(500,200),size=(400,400))
		# panel=wx.Panel(self)
		# self.edit = wx.TextCtrl(self, -1, pos=(10, 30))
		# self.edit.Bind(wx.EVT_TEXT_ENTER, self.onAction)
	# def onAction(self, event):
		# raw_value = self.edit.GetValue().strip()
		# if all(x in '0123456789.+-' for x in raw_value):
			# self.value = round(float(raw_value), 2)
			# self.edit.ChangeValue(str(self.value))
		# else:
			# self.edit.ChangeValue("Number only")
		
		
class MyCustomFrame(wx.Frame):
	
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,size=(600,600))
		panel=wx.Panel(self)
		button_verificare=wx.Button(self, label="Verify", pos=(200,500), size=(60,40))	
		self.Bind(wx.EVT_BUTTON,self.Verify, button_verificare)
		
		self.Bind(wx.EVT_PAINT,self.OnPaint)
		
		
		
		for k in range(3):
			x=randint(0,8)
			y=randint(0,8)
			if mateasy[x][y]!=' ':
				mateasy[x][y]=' '
			else: 
				k=k-1
				
		for i in range(9):
			for j in range(9):
				b=self.edit = wx.TextCtrl(self, -1, pos=(50*i, 50*j),size=(50,50))
				#style=wx.TE_READONLY
				b.SetValue(str(mateasy[i][j]))
				casute.append(b)
				b.Bind(wx.EVT_TEXT_ENTER, self.onAction)
 	
		
		#casute[80].SetValue('8')
		#casute[80].SetDefaultStyle(wx.TE_READONLY)
	def OnPaint(self,evt):
		self.dc = dc = wx.PaintDC(self)
		p1 = [0,0]
		p2 = [450,0]
		for i in range(10):
			dc.DrawLine(p1[0],p1[1],p2[0],p2[1])
			p1 = [p1[0],p1[1]+50]
			p2 = [p2[0],p2[1]+50]
		p1=[0,0]
		p2 = [0,450]
		for i in range(10):
			dc.DrawLine(p1[0],p1[1],p2[0],p2[1])
			p1 = [p1[0]+50,p1[1]]
			p2 = [p2[0]+50,p2[1]]
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
			win32api.MessageBox(0,'Boule','Eroare')
		else:
			win32api.MessageBox(0,'Bravo','Anunt')
			# tkMessageBox.showerror(title="Tk Info box",message="This is a Tk Info/Message box used to display output")
		# else:
			# tkMessageBox.showerror(title="Tk Info box",message="Bravo")
			
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
	
