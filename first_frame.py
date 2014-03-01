import wx

class fr(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'IULIA',size=(300,200))
		
if __name__ == '__main__':
	app=wx.PySimpleApp()
	frame=fr(parent=None,id=-1)
	frame.Show()
	app.MainLoop()
	
