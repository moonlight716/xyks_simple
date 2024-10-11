import pyautogui
import keyboard
import time
import os
# $ pip install pyautogui
# $ pip install keyboard

# 安装pyautogui用于鼠标绘制和点击
# 安装keyboard方便使用esc退出
# 运行python程序


# 指针每步移动所需时间
speed = 0.15 
# 等待墨迹清除的最短时间
wait_time = 0.7

# 绘制区域的起始位置
draw_x, draw_y = 300, 1200  
# “开心收下”按钮的位置，可以使用截图查看电脑像素位置
place1_x, place1_y = 405, 780
# “再练一局”按钮的位置
place2_x, place2_y = 585, 1325

def draw_greater_than(draw_x, draw_y):
    pyautogui.mouseDown(draw_x, draw_y)
    pyautogui.moveTo(draw_x + 100, draw_y + 50, duration=speed)
    pyautogui.moveTo(draw_x, draw_y + 160, duration=speed)
    pyautogui.mouseUp()

def draw_less_than(draw_x, draw_y):
    pyautogui.mouseDown(draw_x, draw_y)
    pyautogui.moveTo(draw_x - 100, draw_y + 50, duration=speed)
    pyautogui.moveTo(draw_x, draw_y + 160, duration=speed)
    pyautogui.mouseUp()

def draw_equal(draw_x, draw_y):
    pyautogui.mouseDown(draw_x, draw_y)
    pyautogui.moveTo(draw_x + 50, draw_y, duration=speed)
    pyautogui.mouseUp()
    pyautogui.mouseDown(draw_x, draw_y + 50)
    pyautogui.moveTo(draw_x + 50, draw_y + 50, duration=speed)
    pyautogui.mouseUp()

def clicktonext():
    pyautogui.mouseDown(place1_x, place1_y)
    time.sleep(0.2)
    pyautogui.mouseUp()
    pyautogui.mouseDown(place2_x, place2_y)
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(1)

guess_time = 0
def main():
    global guess_time
    keyboard.add_hotkey('esc', lambda: os._exit(0))
    while True:
        draw_greater_than(draw_x, draw_y)
        time.sleep(wait_time)
        draw_less_than(draw_x, draw_y)
        time.sleep(wait_time)
        if(guess_time % 3 == 0):
            draw_equal(draw_x, draw_y)
            time.sleep(wait_time)
        if(guess_time == 9):
            clicktonext()

        print("guess time:", guess_time)
        guess_time = (guess_time + 1) % 10


if __name__ == "__main__":
    main()
