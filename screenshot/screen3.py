# -*- coding:utf-8 -*-  
import tkinter
import tkinter.filedialog
import os
from PIL import ImageGrab
from time import sleep
from tkinter import StringVar, IntVar
import time
import win32gui, win32ui, win32con, win32api


def winsst(argw=0,argh=0,argtopleft=(0,0)):
    '''截图，输出Bitmapsbits的列表
    argw=0表示全宽，argh=0表示全高
    '''
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    hwndDC = win32gui.GetWindowDC(hwnd) # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)  # 根据窗口的DC获取mfcDC
    saveDC = mfcDC.CreateCompatibleDC() # mfcDC创建可兼容的DC
    saveBitMap = win32ui.CreateBitmap() # 创建bigmap准备保存图片
    MoniterDev = win32api.EnumDisplayMonitors(None, None)   # 获取监控器信息
    # 判断是否设置截图区域
    w = MoniterDev[0][2][2] if argw==0 else argw
    h = MoniterDev[0][2][3] if argh==0 else argh
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)  # 为bitmap开辟空间
    saveDC.SelectObject(saveBitMap) # 高度saveDC，将截图保存到saveBitmap中
    # 截取从左上角（0，0）或者 tmptl 长宽为（w，h）的图片
    tx=0 if argtopleft[0] <=0 else argtopleft[0]
    ty=0 if argtopleft[1]<=0 else argtopleft[1]
    tmptl=(tx,ty)
    saveDC.BitBlt((0,0), (w, h), mfcDC,tmptl, win32con.SRCCOPY) # 目标矩形顶点(0,0)长宽(w,h),源设备mfcDC,源矩形顶点tmptl
    rtns = saveBitMap.GetBitmapBits()
    # # 绘制辅助框 暂时未解决透明问题
    hPen = win32gui.CreatePen(win32con.PS_SOLID,1,win32api.RGB(255,0,255)) # 定义框颜色
    win32gui.SelectObject(hwndDC,hPen)
    hbrush = win32gui.GetStockObject(win32con.NULL_BRUSH) # 定义透明画刷，这个很重要！！
    prebrush=win32gui.SelectObject(hwndDC,hbrush)
    win32gui.Rectangle(hwndDC,tx-1,ty-1,tx+w+2,ty+h+2) # 左上到右下的坐标
    win32gui.SelectObject(hwndDC,prebrush)
    # # 回收资源
    # mfcDC.DeleteDC()
    # saveDC.DeleteDC()
    # win32gui.DeleteObject(hPen)
    # win32gui.DeleteObject(hbrush)
    # win32gui.DeleteObject(prebrush)
    # win32gui.ReleaseDC(hwnd,hwndDC)
    # rtns = saveBitMap.SaveBitmapFile(saveDC, filename)
   

    # # 绘制辅助框 暂时未解决透明问题
    memDC = win32gui.CreateCompatibleDC(0) # 创建辅助绘图设备
    win32gui.SetBkColor(memDC,win32con.TRANSPARENT)
    hBitmap = win32gui.CreateCompatibleBitmap(memDC,w+2,h+2) # 创建掩码位图(画布)
    win32gui.SelectObject(memDC,hBitmap) # 画布贴在绘图设备上
    hPen = win32gui.CreatePen(win32con.PS_SOLID,1,win32api.RGB(255,0,255))
    win32gui.SelectObject(memDC,hPen)
    hbrush = win32gui.GetStockObject(win32con.NULL_BRUSH)
    prebrush=win32gui.SelectObject(memDC,hbrush)
    win32gui.Rectangle(memDC,tx-1,ty-1,tx+w+2,ty+h+2) # 画布上画矩形    
    win32gui.SelectObject(hwndDC,prebrush)
    win32gui.BitBlt(hwndDC,tx-1,ty-1,w+2,h+2,memDC,0,0,win32con.SRCCOPY)
    return rtns
if __name__ == '__main__':
    winsst()