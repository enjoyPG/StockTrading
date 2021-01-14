import pyautogui as pag
import time
from threading import Thread
import keyboard
import msvcrt as m

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

XY = []

def f():
    global XY
    while(1):
        t = ord(m.getch())
        if(t==47):
            XY.append(coord())
            print(XY)
    return

def begin():
    while(1):
        if keyboard.is_pressed('space'):
            time.sleep(0.2)
            print("동작")
            for i in range(len(XY)):
                click(XY[i])
        if keyboard.is_pressed('F5'):
            print("종료")
            break;
        time.sleep(0.03)

if __name__=='__main__':
        fth = Thread(target=f)
        fth.start()

        st = Thread(target=begin)
        st.start()

        print("사용법")
        print("좌표추가: /")
        print("실행 space")







