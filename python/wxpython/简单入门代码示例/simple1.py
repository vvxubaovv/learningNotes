import wx

def x():
    app = wx.App(False)
    frame = wx.Frame(None,wx.ID_ANY,"hello world!")
    frame.Show(True)
    app.MainLoop()
    
class my_frame(wx.Frame):
    """We simple derive a new class of Frame"""
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

def x1():
    app = wx.App(False)
    frame = my_frame (None,'Small edior')
    app.MainLoop()
    


class my_frame1(wx.Frame):
    """We simple derive a new class of Frame"""
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE,)
        self.Show(True)
        self.CreateStatusBar()#创建窗口底部的状态栏
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_EXIT, "Exit", "Termanate the program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")#设置菜单的内容
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, u"设置")
        self.SetMenuBar(menuBar)#创建菜单条
        self.Show(True)
        
def x2():
    app = wx.App(False)
    frame = my_frame1(None, 'Small edior')
    app.MainLoop()
    
    
class my_frame3(wx.Frame):
    """We simple derive a new class of Frame"""
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE,)
        self.Show(True)
        self.CreateStatusBar()#创建窗口底部的状态栏

        filemenu = wx.Menu()
        menu_exit = filemenu.Append(wx.ID_EXIT, "Exit", "Termanate the program")
        filemenu.AppendSeparator()
        menu_about = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")#设置菜单的内容

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, u"设置")
        self.SetMenuBar(menuBar)#创建菜单条
        self.Show(True)

        self.Bind(wx.EVT_MENU, self.on_about, menu_about)
        self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)#把出现的事件，同需要处理的函数连接起来

    def on_about(self,e):#about按钮的处理函数
        dlg = wx.MessageDialog(self,"A samll text editor", "About sample Editor",wx.OK)#创建一个对话框，有一个ok的按钮
        dlg.ShowModal()#显示对话框
        dlg.Destroy()#完成后，销毁它。

    def on_exit(self,e):
        self.Close(True)
        
def x3():
    app = wx.App(False)
    frame = my_frame3(None, 'Small edior')
    app.MainLoop()
    
import os
class my_frame4(wx.Frame):
    """This is a simple text editor"""
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE,)
        self.Show(True)
        self.CreateStatusBar()#创建窗口底部的状态栏

        filemenu = wx.Menu()
        menu_open = filemenu.Append(wx.ID_OPEN,U"打开文件", " ")
        menu_exit = filemenu.Append(wx.ID_EXIT, "Exit", "Termanate the program")
        filemenu.AppendSeparator()
        menu_about = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")#设置菜单的内容

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, u"设置")
        self.SetMenuBar(menuBar)#创建菜单条
        self.Show(True)

        self.Bind(wx.EVT_MENU,self.on_open,menu_open)
        self.Bind(wx.EVT_MENU, self.on_about, menu_about)
        self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)#把出现的事件，同需要处理的函数连接起来

    def on_about(self,e):#about按钮的处理函数
        dlg = wx.MessageDialog(self,"A samll text editor", "About sample Editor",wx.OK)#创建一个对话框，有一个ok的按钮
        dlg.ShowModal()#显示对话框
        dlg.Destroy()#完成后，销毁它。

    def on_exit(self,e):
        self.Close(True)

    def on_open(self,e):
        """open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self,"Choose a file", self.dirname, "","*.*",wx.FD_OPEN)#调用一个函数打开对话框
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname,self.filename),"r")
        dlg.Destroy()
        
def x4():
    app = wx.App(False)
    frame = my_frame4(None, 'Small edior')
    app.MainLoop()
    
class my_frame5(wx.Frame):
    """This is a simple text editor"""
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,200))
        self.control = wx.TextCtrl(self, -1,u"请先打开要修改的文件", style=wx.TE_MULTILINE,)
        self.Show(True)
        self.CreateStatusBar()#创建窗口底部的状态栏

        filemenu = wx.Menu()
        menu_open = filemenu.Append(wx.ID_OPEN, U"打开文件", " ")
        menu_save = filemenu.Append(wx.ID_SAVE, U"保存修改",)
        menu_exit = filemenu.Append(wx.ID_EXIT, "Exit", "Termanate the program")
        filemenu.AppendSeparator()
        menu_about = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")#设置菜单的内容

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, u"选项")
        self.SetMenuBar(menuBar)#创建菜单条
        self.Show(True)

        self.Bind(wx.EVT_MENU, self.on_open, menu_open)
        self.Bind(wx.EVT_MENU, self.on_about, menu_about)
        self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)#把出现的事件，同需要处理的函数连接起来
        self.Bind(wx.EVT_MENU, self.on_save, menu_save)

    def on_about(self,e):#about按钮的处理函数
        dlg = wx.MessageDialog(self,"A samll text editor", "About sample Editor",wx.OK)#创建一个对话框，有一个ok的按钮
        dlg.ShowModal()#显示对话框
        dlg.Destroy()#完成后，销毁它。

    def on_exit(self,e):
        self.Close(True)

    def on_open(self,e):
        """open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self,"Choose a file", self.dirname, "","*.*",wx.FD_OPEN)#调用一个函数打开对话框
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.address = os.path.join(self.dirname,self.filename)
            f = open(self.address,"r")
            file = (f.read()).decode(encoding='utf-8')#解码，使文件可以读取中文
            f.close()
            self.control.Clear()
            self.control.AppendText(file)#把打开的文件内容显示在多行文本框内
        dlg.Destroy()

    def on_save(self, e):
        date = (self.control.GetValue()).encode(encoding="utf-8")#编码，使中文可以正确存储
        f = open(self.address, 'w')
        f.write(date)
        f.close()#把文本框内的数据写入并关闭文件
        dlg = wx.MessageDialog(self, u"文件已经成功保存", u"消息提示", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        self.control.Clear()
        self.control.AppendText(u'欢迎使用此软件，作者即刻')
        
def x5():
    app = wx.App(False)
    frame = my_frame5(None, u'迷你文本编辑器')
    app.MainLoop()
if __name__=="__main__":
#    x()
#    x1()
#    x2()
#    x3()
#    x4()
    x5()
