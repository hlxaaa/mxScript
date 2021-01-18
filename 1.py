from tkinter import *
import win32gui
import win32con
import win32api
import re
import time
from ctypes import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import aircv as ac

def matchImg(imgsrc,imgobj,confidence=0.5):#imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
 
    match_result = ac.find_template(imsrc,imobj,confidence)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])#0为高，1为宽
    else:
        return None
    # return match_result#{'result': (669.5, 378.0), 'rectangle': ((652, 362), (652, 394), (687, 362), (687, 394)), 'confidence': 1.0, 'shape': (1020, 767)}
    a=match_result['result']
    x=int(a[0])
    y=int(a[1])+24
    return x,y


windowName2='新 梦 想 世 界 - 七星岩 - 丿丶喜欢丨Coff'
windowName1='新 梦 想 世 界 - 七星岩 - 不吃苦瓜'
windowName4='新 梦 想 世 界 - 七星岩 - 布布惊心'
windowName3='新 梦 想 世 界 - 七星岩 - 白白白白白白白'
windowName5='新 梦 想 世 界 - 七星岩 - 〃茶清味、'
cmd='mymymy'
heartstone='炉石传说'
xunleiyingyin='迅雷影音'
x1=0
y1=0
x2=0
y2=125
x3=400
y3=245
x5=896
y5=0
x4=896
y4=125

windowArr1=[windowName1,x1,y1]
windowArr2=[windowName2,x2,y2]
windowArr3=[windowName3,x3,y3]
windowArr4=[windowName4,x4,y4]
windowArr5=[windowName5,x5,y5]

def getPicLocation(windowname,pic):
    hwnd = win32gui.FindWindow(None, windowname)
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save("C:\workplace\python\pic\screenshot.bmp")
    pic='C:/workplace/python/pic/'+pic+'.bmp'
    a=matchImg(u'C:/workplace/python/pic/screenshot.bmp',pic,0.8)
    return a

def keydown(x):
    win32api.keybd_event(x,0,0,0);

def keyup(x):
    win32api.keybd_event(x,0,win32con.KEYEVENTF_KEYUP,0);

def clickL1(x,y):
    win32api.SetCursorPos([x,y]) #设置鼠标位置
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
def clickL(x,y):
    win32api.SetCursorPos([x,y]) #设置鼠标位置
    # time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

def clickR(x,y):
    win32api.SetCursorPos([x,y]) #设置鼠标位置
    # time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)

def reset_window_pos(targetTitle,x,y):  
    wrHd=win32gui.FindWindow(None,targetTitle)
    win32gui.SetWindowPos(wrHd, win32con.HWND_NOTOPMOST, x,y,1026,796, win32con.SWP_NOACTIVATE| win32con.SWP_NOOWNERZORDER|win32con.SWP_SHOWWINDOW)
    win32gui.SetForegroundWindow(wrHd)

def reset_window_pos(arr):  
    targetTitle=arr[0]
    x=arr[1]
    y=arr[2]
    wrHd=win32gui.FindWindow(None,targetTitle)
    win32gui.SetWindowPos(wrHd, win32con.HWND_NOTOPMOST, x,y,1026,796, win32con.SWP_NOACTIVATE| win32con.SWP_NOOWNERZORDER|win32con.SWP_SHOWWINDOW)
    win32gui.SetForegroundWindow(wrHd)

def showcmd(windowname):
    wrHd=win32gui.FindWindow(None,windowname)
    win32gui.SetWindowPos(wrHd, win32con.HWND_NOTOPMOST, 0,0,1026,796, win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE| win32con.SWP_NOOWNERZORDER|win32con.SWP_SHOWWINDOW|win32con.SWP_NOSIZE)
    win32gui.SetForegroundWindow(wrHd)
# reset_window_pos("windowName")

google=''
def showGoogle():
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h,t in hwnd_title.items():
        if t != "":
            if(t.find('Google Chrome')>0):
                google=t
                break
    showcmd(google)

hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})

# win32gui.EnumWindows(get_all_hwnd, 0)
# for h,t in hwnd_title.items():
#     if t is not "":
#         print(h, t)

# win32gui.EnumWindows(get_all_hwnd, 0)
# for h,t in hwnd_title.items():
#     if t is not "":
#         print(h, t)



def buju():
    reset_window_pos(windowArr1)
    reset_window_pos(windowArr2)
    reset_window_pos(windowArr3)
    reset_window_pos(windowArr4)
    reset_window_pos(windowArr5)

def teamPress(x):
    reset_window_pos(windowArr1)
    time.sleep(0.1)
    keydown(x)
    keyup(x)

    reset_window_pos(windowArr2)
    time.sleep(0.1)
    keydown(x)
    keyup(x)

    reset_window_pos(windowArr3)
    time.sleep(0.1)
    keydown(x)
    keyup(x)

    reset_window_pos(windowArr4)
    time.sleep(0.1)
    keydown(x)
    keyup(x)

    reset_window_pos(windowArr5)
    time.sleep(0.1)
    keydown(x)
    keyup(x)

def fangyuTwice():
    reset_window_pos(windowArr1)
    time.sleep(0.1)
    keydown(18)
    keydown(68)
    keyup(68)
    keydown(68)
    time.sleep(0.1)

    reset_window_pos(windowArr2)
    time.sleep(0.1)
    keydown(18)
    keydown(68)
    keyup(68)
    keydown(68)
    time.sleep(0.1)

    reset_window_pos(windowArr3)
    time.sleep(0.1)
    keydown(18)
    keydown(68)
    keyup(68)
    keydown(68)
    time.sleep(0.1)

    reset_window_pos(windowArr4)
    time.sleep(0.1)
    keydown(18)
    keydown(68)
    keyup(68)
    keydown(68)
    time.sleep(0.1)

    reset_window_pos(windowArr5)
    time.sleep(0.1)
    keydown(18)
    keydown(68)
    keyup(68)
    keydown(68)
    time.sleep(0.1)
    keyup(18)
    keyup(68)

def ctrlA():
    reset_window_pos(windowArr1)
    time.sleep(0.1)
    keydown(17)
    keydown(65)
    keyup(65)
    keydown(65)
    # time.sleep(0.1)

    reset_window_pos(windowArr2)
    time.sleep(0.1)
    keydown(17)
    keydown(65)
    keyup(65)
    keydown(65)
    # time.sleep(0.1)

    reset_window_pos(windowArr3)
    time.sleep(0.1)
    keydown(17)
    keydown(65)
    keyup(65)
    keydown(65)
    # time.sleep(0.1)

    reset_window_pos(windowArr4)
    time.sleep(0.1)
    keydown(17)
    keydown(65)
    keyup(65)
    keydown(65)
    # time.sleep(0.1)

    reset_window_pos(windowArr5)
    time.sleep(0.1)
    keydown(17)
    keydown(65)
    keyup(65)
    keydown(65)
    time.sleep(0.1)
    keyup(17)
    keyup(65)

def clickArr(arr):
    reset_window_pos(windowArr1)
    time.sleep(0.1)
    for x,y in arr:
        clickL1(x1+x,y1+y)
        time.sleep(0.2)

    reset_window_pos(windowArr2)
    time.sleep(0.1)
    for x,y in arr:
        clickL1(x2+x,y2+y)
        time.sleep(0.2)
    
    reset_window_pos(windowArr3)
    time.sleep(0.1)
    for x,y in arr:
        clickL1(x3+x,y3+y)
        time.sleep(0.2)

    reset_window_pos(windowArr4)
    time.sleep(0.1)
    for x,y in arr:
        clickL1(x4+x,y4+y)
        time.sleep(0.2)
    
    reset_window_pos(windowArr5)
    time.sleep(0.1)
    for x,y in arr:
        clickL1(x5+x,y5+y)
        time.sleep(0.2)

def teamClick(x,y):
    reset_window_pos(windowArr1)
    time.sleep(0.1)
    # x=286
    # y=283
    clickL(x1+x,y1+y)
    time.sleep(0.1)

    reset_window_pos(windowArr2)
    time.sleep(0.1)
    clickL(x2+x,y2+y)
    time.sleep(0.1)

    reset_window_pos(windowArr3)
    time.sleep(0.1)
    clickL(x3+x,y3+y)
    time.sleep(0.1)

    reset_window_pos(windowArr4)
    time.sleep(0.1)
    clickL(x4+x,y4+y)
    time.sleep(0.1)

    reset_window_pos(windowArr5)
    time.sleep(0.1)
    clickL(x5+x,y5+y)
    time.sleep(0.1)

def leaveMg():
    reset_window_pos(windowArr1)
    time.sleep(0.1)
    keydown(114)
    time.sleep(0.2)
    clickL(x1+544,y1+400)
    time.sleep(0.2)
    clickL(x1+307,y1+413)
    time.sleep(0.2)
    
    reset_window_pos(windowArr2)
    time.sleep(0.1)
    keydown(114)
    time.sleep(0.2)
    clickL(x2+544,y2+400)
    time.sleep(0.2)
    clickL(x2+307,y2+413)
    time.sleep(0.2)
    
    reset_window_pos(windowArr3)
    time.sleep(0.1)
    keydown(114)
    time.sleep(0.2)
    clickL(x3+544,y3+400)
    time.sleep(0.2)
    clickL(x3+307,y3+413)
    time.sleep(0.2)
    
    reset_window_pos(windowArr4)
    time.sleep(0.1)
    keydown(114)
    time.sleep(0.2)
    clickL(x4+544,y4+400)
    time.sleep(0.2)
    clickL(x4+307,y4+413)
    time.sleep(0.2)
    
    reset_window_pos(windowArr5)
    time.sleep(0.1)
    keydown(114)
    time.sleep(0.2)
    clickL(x5+544,y5+400)
    time.sleep(0.2)
    clickL(x5+307,y5+413)
    time.sleep(0.2)
    
    keyup(114)

def teamOper():
    reset_window_pos(windowArr1)
    time.sleep(0.1)
    keydown(18)
    keydown(84)
    time.sleep(0.2)
    clickL(x1+356,y1+582)
    time.sleep(0.2)

    reset_window_pos(windowArr2)
    time.sleep(0.1)
    keydown(18)
    keydown(84)
    time.sleep(0.2)
    clickL(x2+356,y2+582)
    time.sleep(0.2)

    reset_window_pos(windowArr3)
    time.sleep(0.1)
    keydown(18)
    keydown(84)
    time.sleep(0.2)
    clickL(x3+356,y3+582)
    time.sleep(0.2)

    reset_window_pos(windowArr4)
    time.sleep(0.1)
    keydown(18)
    keydown(84)
    time.sleep(0.2)
    clickL(x4+356,y4+582)
    time.sleep(0.2)

    reset_window_pos(windowArr5)
    time.sleep(0.1)
    keydown(18)
    keydown(84)
    time.sleep(0.2)
    clickL(x5+356,y5+582)
    time.sleep(0.2)

    keyup(18)
    keyup(84)

def fbdianguai(x,y):
    reset_window_pos(windowArr1)
    time.sleep(0.1)
    clickR(x1+x,y1+y) 
    time.sleep(0.1)   
    clickL(x1+x,y1+y)
    time.sleep(0.1)

    reset_window_pos(windowArr2)
    time.sleep(0.1)
    clickR(x2+x,y2+y)
    time.sleep(0.1)
    clickL(x2+x,y2+y)
    time.sleep(0.1)

    reset_window_pos(windowArr3)
    time.sleep(0.1)
    clickR(x3+x,y3+y)
    time.sleep(0.1)
    clickL(x3+x,y3+y)
    time.sleep(0.1)

    reset_window_pos(windowArr4)
    time.sleep(0.1)
    clickR(x4+x,y4+y)
    time.sleep(0.1)
    clickL(x4+x,y4+y)
    time.sleep(0.1)

    reset_window_pos(windowArr5)
    time.sleep(0.1)
    keydown(17)
    keydown(65)
    keyup(65)
    keydown(65)
    time.sleep(0.1)
    keyup(17)
    keyup(65)

def dianguai(x,y):
    reset_window_pos(windowArr1)
    time.sleep(0.1)
    clickR(x1+x,y1+y) 
    time.sleep(0.1)   
    clickL(x1+x,y1+y)
    time.sleep(0.1)

    reset_window_pos(windowArr2)
    time.sleep(0.1)
    clickR(x2+x,y2+y)
    time.sleep(0.1)
    clickL(x2+x,y2+y)
    time.sleep(0.1)

    reset_window_pos(windowArr3)
    time.sleep(0.1)
    clickR(x3+x,y3+y)
    time.sleep(0.1)
    clickL(x3+x,y3+y)
    time.sleep(0.1)

    reset_window_pos(windowArr4)
    time.sleep(0.1)
    clickR(x4+x,y4+y)
    time.sleep(0.1)
    clickL(x4+x,y4+y)
    time.sleep(0.1)

    reset_window_pos(windowArr5)
    time.sleep(0.1)
    clickR(x5+x,y5+y)
    time.sleep(0.1)
    clickL(x5+x,y5+y)
    time.sleep(0.1)

def findPicClickL(pic,windowArr):
    a=getPicLocation(windowArr[0],pic)
    if(a is None):
        return
    x=windowArr[1]+a[0]
    y=windowArr[2]+a[1]
    clickL(x,y)
    time.sleep(0.1)

def findPicClickR(pic,windowArr):
    a=getPicLocation(windowArr[0],pic)
    if(a is None):
        print('没找到'+pic)
        return
    x=windowArr[1]+int(a[0])
    y=windowArr[2]+int(a[1])
    # print(x,y)
    clickR(x,y)
    time.sleep(0.1)

def switchBag(n,windowArr):
    bag='bag1'
    if(n==2):
        bag='bag2'
    a=getPicLocation(windowArr[0],bag)
    if(a is None):
        print('没找到bag')
        return
    # print(a)
    reset_window_pos(windowArr)
    time.sleep(0.1)
    # print(float(a[0]),float(a[1]))
    x=windowArr[1]+int(a[0])
    y=windowArr[2]+int(a[1])
    clickL(x,y)
    time.sleep(0.1)

def clearAllBag():
    ctrlA()
    teamPress(27)

def clearBag(windowArr):
    reset_window_pos(windowArr)
    time.sleep(0.1)
    keydown(18)
    keydown(69)
    time.sleep(0.1)
    keyup(18)
    keyup(69)
    switchBag(1,windowArr)
    time.sleep(0.1)
    findPicClickR(pic,windowArr)
    time.sleep(0.2)
    switchBag(2,windowArr)
    time.sleep(0.1)
    findPicClickR(pic,windowArr)


def rtnkey(event=None):
    str=e.get()
    if str=='0':
        teamPress(27)
    elif str=='00':
        buju()
    elif str=='1':
        ctrlA()
        # ctrlA()
    elif str=='3':
        ctrlA()
        teamPress(27)
        teamOper()
    elif str=='31':
        leaveMg()
    elif str=='41':
        teamClick(465,525)
    elif str=='42':
        teamClick(465,500)
    elif str=='5':
        fbdianguai(287,282)
    elif str=='51':
        dianguai(87,370)
    elif str=='52':
        dianguai(194,330)
    elif str=='53':
        dianguai(287,282)
    elif str=='54':
        dianguai(375,220)
    elif str=='55':
        dianguai(479,185)
    elif str=='6':
        fangyuTwice()
    elif str=='8':
        clickArr([[918,58],[838,287],[631,334],[542,452],[424,391]])
    elif str=='9':
        teamPress(120)
    elif str=='10':
        clearBag(windowArr1,'xitang')
    else:
        ctrlA()
        # a=getPicLocation(windowName1,'bag2')
        # if(a is None):
        #     return
        # print(a)
        # reset_window_pos(windowArr1)
        # time.sleep(0.1)
        # print(float(a[0]),float(a[1]))
        # clickL(int(a[0]),int(a[1]))
        # time.sleep(0.1)

    showcmd(cmd)
    entry.delete(0, END)
    showGoogle()
    showcmd(cmd)
    time.sleep(0.2)
    showcmd(heartstone)
    showcmd(xunleiyingyin)
    showcmd(cmd)
    entry.focus()


root = Tk()
root.title("mymymy") 
root.geometry("600x500")
e = StringVar()
entry = Entry(root, validate='key', textvariable=e, width=20)
# entry.pack()
entry.grid(row=10, column=5)
entry.focus()
entry.bind('<Return>', rtnkey)

label00 = Label(root, text="布局：00")
label0 = Label(root, text="ESC：0")
label1 = Label(root, text="自动攻击：1")
label3 = Label(root, text="归队离队：3")
label31 = Label(root, text="离开迷宫：31")
label41 = Label(root, text="副本确定：41")
label42 = Label(root, text="mgxz确定：42")
label5 = Label(root, text="点主：5")
label6 = Label(root, text="防御2次：6")
label8 = Label(root, text="卖体力：8")
label9 = Label(root, text="F9：9")

# label4.grid(row=1, column=1)
label00.grid(row=0, column=0)
label0.grid(row=0, column=1)
label1.grid(row=1, column=0)
label3.grid(row=3, column=0)
label31.grid(row=3, column=1)
label41.grid(row=4, column=0)
label42.grid(row=4, column=1)
label5.grid(row=5, column=0)
label6.grid(row=6, column=0)
label8.grid(row=8, column=0)
label9.grid(row=9, column=0)
# root.title('测试回车获取文本框内容')
root.mainloop()