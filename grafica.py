import wx

class fr(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'SUDOKU',size=(400,400))
		panel=wx.Panel(self)
		button1=wx.Button(panel, label="Easy", pos=(170,100), size=(60,40))
		button2=wx.Button(panel, label="Medium", pos=(170,150), size=(60,40))
		button3=wx.Button(panel, label="Hard", pos=(170,200), size=(60,40))
		
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
		

	
class fr2(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'How To Play Sudoku',pos=(500,200),size=(400,400))
		panel=wx.Panel(self)
		
		text=wx.StaticText(panel,-1,"Rules of playing sudoku", (150,30))
		#custom.SetForegroundColour('blue')
		#custom.SetBackgroundColour('white')
		
if __name__ == '__main__':
	app=wx.PySimpleApp()
	frame=fr(parent=None,id=-1)
	frame.Show()
	app.MainLoop()
	
