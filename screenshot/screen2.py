# # -*- coding:utf-8 -*-  
# import tkinter
# import tkinter.filedialog
# import os
# from PIL import ImageGrab
# from time import sleep
# from tkinter import StringVar, IntVar
# #创建tkinter主窗口
# root = tkinter.Tk()
# #指定主窗口位置与大小
# root.geometry('200x80+400+300')
# #不允许改变窗口大小
# root.resizable(False, False)
# class MyCapture:
#     def __init__(self, png):
#         #变量X和Y用来记录鼠标左键按下的位置
#         self.X = tkinter.IntVar(value=0)
#         self.Y = tkinter.IntVar(value=0)
        
#         self.selectPosition=None
#         #屏幕尺寸
#         screenWidth = root.winfo_screenwidth()
#         #print(screenWidth)
#         screenHeight = root.winfo_screenheight()
#         #print(screenHeight)
#         #创建顶级组件容器
#         self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeight)
#         #不显示最大化、最小化按钮
#         self.top.overrideredirect(True)
#         self.canvas = tkinter.Canvas(self.top,bg='white', width=screenWidth, height=screenHeight)
#         #显示全屏截图，在全屏截图上进行区域截图
#         self.image = tkinter.PhotoImage(file=png)
#         self.canvas.create_image(screenWidth//2, screenHeight//2, image=self.image)
#         #鼠标左键按下的位置
#         def onLeftButtonDown(event):
#             self.X.set(event.x)
#             self.Y.set(event.y)
#             #开始截图
#             self.sel = True
#         self.canvas.bind('<Button-1>', onLeftButtonDown)
#         #鼠标左键移动，显示选取的区域
#         def onLeftButtonMove(event):
#             if not self.sel:
#                 return
#             global lastDraw
#             try:
#                 #删除刚画完的图形，要不然鼠标移动的时候是黑乎乎的一片矩形
#                 self.canvas.delete(lastDraw)
#             except Exception as e:
#                 pass
#             lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='black')
#         self.canvas.bind('<B1-Motion>', onLeftButtonMove)
#         #获取鼠标左键抬起的位置，保存区域截图
#         def onLeftButtonUp(event):
#             self.sel = False
#             try:
#                 self.canvas.delete(lastDraw)
#             except Exception as e:
#                 pass
#             sleep(0.1)
#             #考虑鼠标左键从右下方按下而从左上方抬起的截图
#             myleft, myright = sorted([self.X.get(), event.x])
#             mytop, mybottom = sorted([self.Y.get(), event.y])
#             self.selectPosition=(myleft,myright,mytop,mybottom)
# #             pic = ImageGrab.grab((left+1, top+1, right, bottom))
# #   
# #             #弹出保存截图对话框
# #  
# #             fileName = tkinter.filedialog.asksaveasfilename(title='保存截图', filetypes=[('JPG files', '*.jpg')])
# #  
# #             if fileName:
# #  
# #                 pic.save(fileName+'.jpg')
#             #关闭当前窗口
#             #print(left, '  ', top,'  ',right,'  ',bottom)
            
#             self.top.destroy()
            
#         self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
#         self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
#     #开始截图
# text = StringVar()
# text.set('old')
# def buttonCaptureClick():
#     #最小化主窗口
#     #root.state('icon')
#     #sleep(0.2)
    
#     filename = 'temp.png'
#     im = ImageGrab.grab()
#     im.save(filename)
#     # im.close()
#     #显示全屏幕截图
#     w = MyCapture(filename)
#     buttonCapture.wait_window(w.top)
#     # text.set(str(w.selectPosition))
    
#     #print(w.myleft,w.mybottom)
#     #截图结束，恢复主窗口，并删除临时的全屏幕截图文件
#     #label.config(text='Hello')
#     root.state('normal')
#     # os.remove(filename)
# label=tkinter.Label(root,textvariable=text)
# label.place(x=10, y=30, width=160, height=20)
# label.config(text='New test')
# buttonCapture = tkinter.Button(root, text='截图', command=buttonCaptureClick)
# buttonCapture.place(x=10, y=10, width=160, height=20)
# #启动消息主循环
# #root.update()
# root.Topmost= 'true'
# root.mainloop()





# import time
# import numpy as np
# from PIL import ImageGrab
# # 每抓取一次屏幕需要的时间约为1s,如果图像尺寸小一些效率就会高一些
# beg = time.time()
# debug = False
# for i in range(10):
#   img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
#   img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
# end = time.time()
# print(end - beg)








# import time
# import win32gui, win32ui, win32con, win32api
# def window_capture(filename):
#   hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
#   # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
#   hwndDC = win32gui.GetWindowDC(hwnd)
#   # 根据窗口的DC获取mfcDC
#   mfcDC = win32ui.CreateDCFromHandle(hwndDC)
#   # mfcDC创建可兼容的DC
#   saveDC = mfcDC.CreateCompatibleDC()
#   # 创建bigmap准备保存图片
#   saveBitMap = win32ui.CreateBitmap()
#   # 获取监控器信息
#   MoniterDev = win32api.EnumDisplayMonitors(None, None)
#   w = MoniterDev[0][2][2]
#   h = MoniterDev[0][2][3]
#   # print w,h　　　#图片大小
#   # 为bitmap开辟空间
#   saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
#   # 高度saveDC，将截图保存到saveBitmap中
#   saveDC.SelectObject(saveBitMap)
#   # 截取从左上角（0，0）长宽为（w，h）的图片
#   saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
#   saveBitMap.SaveBitmapFile(saveDC, filename)
# beg = time.time()
# for i in range(10):
#   window_capture("haha.jpg")
# end = time.time()
# print(end - beg)




# -*- coding: utf-8 -*-

# from selenium import webdriver
# import time


# def take_screenshot(url, save_fn="capture.png"):
#     # browser = webdriver.Firefox() # Get local session of firefox
#     #谷歌浏览器截取当前窗口网页
#     chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#     browser = webdriver.Chrome(chromedriver)
#     #phantomjs截取整张网页
#     # browser = webdriver.PhantomJS()
#     browser.set_window_size(1200, 900)
#     browser.get(url) # Load page
#     #将页面的滚动条拖到最下方，然后再拖回顶部
#     browser.execute_script("""
#         (function () {
#             var y = 0;
#             var step = 100;
#             window.scroll(0, 0);

#             function f() {
#                 if (y < document.body.scrollHeight) {
#                     y += step;
#                     window.scroll(0, y);
#                     setTimeout(f, 100);
#                 } else {
#                     window.scroll(0, 0);
#                     document.title += "scroll-done";
#                 }
#             }

#             setTimeout(f, 1000);
#         })();
#     """)



#     for i in xrange(30):
#         if "scroll-done" in browser.title:
#             break
#         time.sleep(10)

#     browser.save_screenshot(save_fn)
#     browser.close()


# if __name__ == "__main__":

#     take_screenshot("http://www.baidu.com")










# -*- coding: utf-8 -*-

# from selenium import webdriver
# import time


# def take_screenshot(url, save_fn="capture.png"):
#     # browser = webdriver.Firefox() # Get local session of firefox
#     chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#     browser = webdriver.Chrome(chromedriver)
#     # browser = webdriver.PhantomJS()
#     browser.set_window_size(1200, 900)
#     browser.get(url) # Load page
    #将页面的滚动条拖到最下方，然后再拖回顶部
    # browser.execute_script("""
    #     (function () {
    #         var y = 0;
    #         var step = 100;
    #         window.scroll(0, 0);
    # 
    #         function f() {
    #             if (y < document.body.scrollHeight) {
    #                 y += step;
    #                 window.scroll(0, y);
    #                 setTimeout(f, 100);
    #             } else {
    #                 window.scroll(0, 0);
    #                 document.title += "scroll-done";
    #             }
    #         }
    # 
    #         setTimeout(f, 1000);
    #     })();
    # """)
    # 
    # for i in xrange(30):
    #     if "scroll-done" in browser.title:
    #         break
    #     time.sleep(10)

    #只截取编程派网站右侧的二维码，可以执行这样一段JQuery代码：siblings().remove()移除兄弟姐妹元素
#     browser.execute_script("""
#         $('#main').siblings().remove();
#         $('#aside__wrapper').siblings().remove();
#         $('.ui.sticky').siblings().remove();
#         $('.follow-me').siblings().remove();
#         $('img.ui.image').siblings().remove();
#         """)

#     browser.save_screenshot(save_fn)
#     # browser.close()


# if __name__ == "__main__":

#     take_screenshot("http://codingpy.com/article/take-screenshot-of-web-page-using-selenium/")
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
import pyautogui as pag
import tkinter

mytime = 2

#判断时间是否合法
def safe():         
    text = getmytime.get();
    #小数点个数
    point = 0
    if(text==""):
        return False
    for i in text:
        if(i>='0' and i<='9'and point<2):
            continue
        elif(i=='.'):
            point = point + 1
        else:
            return False
    return True
def get():
    global mytime
    if(safe()):
        mytime = float(getmytime.get())
        
        #不知道为何下面的这个if没用
        if(mytime>7.0):
            showpos.delete(0,tkinter.END)
            showpos.insert(0,"请耐心等候")
    
        time.sleep(mytime) #几秒后返回位置
        x , y = pag.position()
        showpos.delete(0,tkinter.END)
        showpos.insert(0,str(x)+','+str(y))
    else:
        showpos.delete(0,tkinter.END)
        showpos.insert(0,"输入非法哟~")

 
root = tkinter.Tk()
root.resizable(0,0)

tip1 = tkinter.Label(root,text="点击按钮获取")
tip1.place(relx=0.1,rely=0.1)
getmytime = tkinter.Entry(root,width=3)
getmytime.place(relx=0.6,rely=0.1)
getmytime.insert(0,str(mytime))
tip2 = tkinter.Label(root,text="s后的")
tip2.place(relx=0.8,rely=0.1)

tip3 = tkinter.Label(root,text="光标位置:")
tip3.place(relx=0.1,rely=0.3)
showpos = tkinter.Entry(root,width=10)
showpos.place(relx=0.5,rely=0.3)
do = tkinter.Button(root,text="按钮",command=get) #点击获取位置
do.place(relx=0.8,rely=0.6)


root.mainloop()
