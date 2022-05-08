# _*_ coding : utf-8 _*_
# @Time : 2022/4/20 22:09
from PIL import ImageGrab
import time
import pynput
import os


num = 1  # 从第一张开始截图
dir_name = '/Picture'   # 截图存放的路径
# 如果不存在这个文件则在当前目录下创建
if not os.path.exists('Picture'):
    os.mkdir('./' + dir_name)


# 以最左下角为(0,0),前两个参数是你选取的左下角的坐标,后面两个参数是右上角的坐标
region = (960-320, 540-320, 960+320, 540+320)    # 截图范围
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
        img.save('./' + dir_name + '/' + str(num) + '.jpg')  # 保存截图到Picture下
        num += 1


def on_release(key):
    pass


listener = pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    pass
