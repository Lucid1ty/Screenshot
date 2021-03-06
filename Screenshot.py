# _*_ coding : utf-8 _*_
# @Time : 2022/4/20 22:09
"""
使用环境：Anaconda：py38
运行后按：e 即可截图一张
结束运行直接点 stop
运行需要安装如下的一些库
"""
from PIL import ImageGrab
import time
import pynput
import os


num = 1  # 从第一张开始截图(图片文件名将会是：1.jpg 2.jpg ...)
dir_name = '/Screenshot Result'   # 截图存放的文件夹
# 如果不存在这个文件则在当前目录下创建
if not os.path.exists('Screenshot Result'):
    os.mkdir('./' + dir_name)


# 以最左下角为(0,0),前两个参数是你选取的左下角的坐标,后面两个参数是右上角的坐标
region = (960-320, 540-320, 960+320, 540+320)    # 截图范围(截取屏幕中央往外扩散的640*640像素的图片)
# img = ImageGrab.grab(region)  # 截图
# img.save("PILImage13.jpg")   # 将截图另存为
# print(img.size)  # 打印截图的分辨率
# print(img.mode)  # 打印图片的模式


def on_press(key):
    global num
    # 如果按下e
    if key == pynput.keyboard.KeyCode(char='e'):
        time.sleep(2)
        img = ImageGrab.grab(region)  # 截图
        img.save('./' + dir_name + '/' + str(num) + '.jpg')  # 保存截图到 Screenshot Result 文件夹下
        num += 1


def on_release(key):
    pass


listener = pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    pass
