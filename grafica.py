import wx


class fr(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'SUDOKU',size=(400,400))
		panel=wx.Panel(self)
		button1=wx.Button(panel, label="Easy", pos=(170,100), size=(60,40))
		button2=wx.Button(panel, label="Medium", pos=(170,150), size=(60,40))
		button3=wx.Button(panel, label="Hard", pos=(170,200), size=(60,40))
		
		self.Bind(wx.EVT_BUTTON,self.sudoku, button1)
		self.Bind(wx.EVT_BUTTON,self.sudoku, button2)
		self.Bind(wx.EVT_BUTTON,self.sudoku, button3)
		
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
		#panel=wx.Panel(self)
		
		
		#text=wx.StaticText(panel,-1,"Rules of playing sudoku", (150,30))
		#custom.SetForegroundColour('blue')
		#custom.SetBackgroundColour('white')
	
class gameframe(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Sudoku v2.0',pos=(500,200),size=(400,400))
		panel=wx.Panel(self)
		self.edit = wx.TextCtrl(self, -1, pos=(10, 30))
		self.edit.Bind(wx.EVT_TEXT_ENTER, self.onAction)
	def onAction(self, event):
		raw_value = self.edit.GetValue().strip()
		if all(x in '0123456789.+-' for x in raw_value):
			self.value = round(float(raw_value), 2)
			self.edit.ChangeValue(str(self.value))
		else:
			self.edit.ChangeValue("Number only")
		
		
class MyCustomFrame(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,size=(600,600))
		panel=wx.Panel(self)
		self.Bind(wx.EVT_PAINT,self.OnPaint)
		self.edit = wx.TextCtrl(self, -1, pos=(0, 0),size=(50,50))
		self.edit.Bind(wx.EVT_TEXT_ENTER, self.onAction)
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
	
