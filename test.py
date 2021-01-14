# coding=<utf-8>
from msvcrt import getch

print("d")

while True:
    key = ord(getch())
    if(key!=255):
        print(key)
    if key == 27: #ESC
        break
    elif key == 13: #Enter
        print('Enter')
    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())
        if key == 80: #Down arrow
            print('down')
        elif key == 72: #Up arrow
            print('up')