# coding: UTF-8
from ctypes import *  # 锁屏

import tkinter as tk  # 模块重命名
import tkinter.font as tkFont  # 字体模块重命名
import tkinter.messagebox  # 提示弹窗模块重命名
import time  # 时间模块
# import winsound#声音模块只能播放.wav
import math  # 数字处理模块 用于了向上取余

# 创建主窗体
window = tk.Tk()
# 进入消息循环
window.wm_attributes('-topmost', 1)  # 窗口置顶
window.attributes("-alpha", 0.99)
window.title('计时器')  # 设置窗口名字
window.geometry('220x140')  # 设置窗口大小
cheak = 0


def clean_line():  # 清除进度条
    global cheak
    cheak = 0
    # fill_line = canvas.create_rectangle(1, 1, 0, 23, width=0, fill="white")
    # canvas.coords(fill_line, (0, 0, 200, 60))#括号内第三个删除是关键
    window.update()  # 更新窗口


def lockScreen():
    user32 = windll.LoadLibrary('user32.dll')
    user32.LockWorkStation()


def count_deep25():  # 25分钟倒计时
    global fre  # 声明使用全局变量 global是全局变量更改的函数
    global var
    global x
    global n
    clean_line()  # 清理进度条
    x = 0.1  # 细分了全长150 0.1*60*25
    n = 0  # 进度条累加的变量
    # fill_line = canvas.create_rectangle(1, 1, 0, 23, width=0, fill="green")#声明下面增加进度条的颜色，绘制矩形((a,b,c,d),值为左上角和右下角的坐标)；
    var = 25  # 倒计时25分钟
    # canvas.coords(fill_line, (0, 0, 75, 60))
    L3['text'] = str(var)  # 初始化页面的倒计时 例如00 → 25
    L3.update()  # 更新该项数值
    while var > 0:  # 当大于0进入循环
        time.sleep(1)  # 延时1秒 测试时候设置0.1快进10倍
        var = var - (1 / 60)  # 一分钟的1/60
        n = n + x  # 进度条累加
        # canvas.coords(fill_line,(0,0,n,60))#进度条延长？coords(ID) 返回对象的位置的两个坐标（4个数字元组）；
        window.update()  # 更新全局
        try:
            if var <= 9:  # 始终保持两位数 小于就前面补0
                L3['text'] = str(0) + str(math.ceil(var))  # 前面补0 # math.ceil作用是向上取整 0.99→1
                L3.update()
                if var < 1:
                    cheak = 1
            else:
                L3['text'] = str(math.ceil(var))
                L3.update()
        except:
            break
    fre = fre + 1  # 番茄个数加一
    L2['text'] = str(fre)  # 调用相关的初始化值
    L2.update()
    if cheak == 1:
        # winsound.PlaySound("tisimusic.wav", flags=1)#播放音乐
        tk.messagebox.showinfo('Prism提醒', '请休息一下吧！')  # 弹窗提示


def count_deep5():  # 倒计时5分钟 原理同上 改进写法 同一个函数写完即可 通过不同按钮提供不同的标志位加以判断即可
    global fre
    global var
    global x
    global n
    global cheak
    global resetVar
    resetVar = 1
    # clean_line()
    x = 0.5  # 划分进度条 0.5*60*5分钟
    n = 0
    # fill_line = canvas.create_rectangle(1, 1, 0, 23, width=0, fill="green")
    var = 5 * 60
    # canvas.coords(fill_line, (0, 0, 75, 60))
    L3['text'] = "05:00"
    L3.update()
    while var > 0:
        if resetVar == 0:
            # tk.messagebox.showinfo('提醒', '时间结束')
            break
        time.sleep(1)
        var = var - 1
        n = n + x
        # canvas.coords(fill_line,(0,0,n,60))
        # window.update()
        try:
            second = var % 60
            if second < 10:
                secondStr = "0" + str(second)
            else:
                secondStr = str(second)
            L3['text'] = str(0) + str(var // 60) + ":" + secondStr
            L3.update()
            if var < 1:
                cheak = 1;
        except:
            break
    if cheak == 1:
        # lockScreen()
        # winsound.PlaySound("tisimusic.wav",flags =1)
        tk.messagebox.showinfo('提醒', '时间结束')


def clean_fre():  # 清理按键 清理番茄个数的累计
    global fre
    fre = 0  # 将其归0
    L2['text'] = str(fre)
    L2.update()


def reset():  # 重置
    global resetVar
    resetVar = 0  # 将其归0
    L3['text'] = "05:00"
    L3.update()


# 设置文字
L1 = tk.Label(window, text='当前任务番茄个数:  ')
# L1.grid(row=1,column=1)
fre = 0  # 番茄钟个数
underline = 1
ft1 = tkFont.Font(underline=1)
L2 = tk.Label(window, text=str(fre), font=ft1)
# L2.grid(row=1, column=2)
var = 25  # 倒计时数字
ft = tkFont.Font(size=50)
L3 = tk.Label(window, text="05:00", font=ft, pady=20)
# L3.place(x=40, y=20)  # 直接使用坐标定位
L3.pack()  # 自动居中

# 设置进度条
# canvas = tk.Canvas(window, width=149, height=10, bg="white") #width 因为长了一点-1不美观 150-1=149
# canvas.place(x=20,y=98)
# def progress():
#     fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
#     x = 500
#     n = 465 / x
#     canvas.coords(fill_line,(0,0,n,60))
#     window.update()
#     time.sleep(0.02)

T25 = tk.Button(window, text='25分', command=count_deep25)  # 按键设置
# T25.place(x=20,y=115)
T05 = tk.Button(window, text='开始', pady=2, command=count_deep5)
# T05.place(x=20, y=115)
# T05.pack()
T05.place(relx=0.2, rely=0.7)
clean = tk.Button(window, text='重置', pady=2, command=reset)
# clean.place(x=120, y=115)
# clean.pack()
clean.place(relx=0.5, rely=0.7)



window.mainloop()  # 无限循环
