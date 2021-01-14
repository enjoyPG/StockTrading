#사용법
#1. F1키 주
#2. F2키 금액
#3. F3키 조건추가
#4. F4키 감시선택
#종목을 선택하고 금액입력 후 space를 누르면 됨
#종료할 땐 F5키

import pyautogui as pag
import time
from threading import Thread
import keyboard

def coord():
    XY = []
    x,y = pag.position()
    XY.append(x)
    XY.append(y)
    print(XY)
    return XY

def click(coord):
    pag.moveTo(x=coord[0], y=coord[1], duration=0.1)
    pag.mouseDown()
    pag.mouseUp()
    time.sleep(0.6)
    return

first_order = [-1,-1]
second_money = [-1,-1]
third_append = [-1,-1]
fourth_detect =[-1,-1]

def f():
    global first_order
    while(1):
        if keyboard.is_pressed('F1'):
            first_order = coord()
        if first_order[0] != -1:
            print('Set => first_detect!!')
            break;
        time.sleep(0.1)
    return

def s():
    global second_money
    while(1):
        if keyboard.is_pressed('F2'):
            second_money = coord()
        if second_money[0] != -1:
            print('Set => second_detect!!')
            break;
        time.sleep(0.1)
    return

def t():
    global third_append
    while(1):
        if keyboard.is_pressed('F3'):
            third_append = coord()
        if third_append[0] != -1:
            print('Set => third_detect!!')
            break;
        time.sleep(0.1)
    return

def fo():
    global fourth_detect
    while(1):
        if keyboard.is_pressed('F4'):
            fourth_detect = coord()
        if fourth_detect[0] != -1:
            print('Set => fourth_detect!!')
            break;
        time.sleep(0.1)
    return

def begin():
    while(1):
        if keyboard.is_pressed('space'):
            print("동작")
            click(first_order)
            click(second_money)
            click(third_append)
            click(fourth_detect)
        if keyboard.is_pressed('F5'):
            print("종료")
            break;
        time.sleep(0.1)



#def begin():
fth = Thread(target=f)
fth.start()
sth = Thread(target=s)
sth.start()
tth = Thread(target=t)
tth.start()
foth = Thread(target=fo)
foth.start()
st = Thread(target=begin)
st.start()








