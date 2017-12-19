#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import ast
import time
import sys
import datetime

import tam

PATH = "C:\\USERS\\TAMIR\\DESKTOP\\TAMIRNEEDHELP\\FORMS\\"
MONTH = "1"
YEAR = "Tashaach"
DAN_PHONE = "054-3213908"

OPEN_PORTAL = [(2405, 257)]
OPEN_FORM = [(2415, 759), (1841, 392), (1996, 458), (2141, 689)]
FILL_FORM = [(1954, 414), (1964, 436), (1696, 552), DAN_PHONE, (1898, 699), (1299, 720), "", 
(2076, 865), (2071, 890), "", (2057, 1020), (1360, 717), "", (1517, 838), (1730, 1014), "",
(1794, 1047), "year", (1684, 1050), "month", (2199, 1335),
(40, 1409), (559, 941)
]
DRAG_FILE = [(960, 63), "path", ]

def read_file(file):
    buffer = ""
    # first read entire file
    with open(file) as f:
        while True:
            buf = f.read()
            if buf  == "":
                break
            buffer += buf
    return buffer

def do_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    
def drag(x1, y1, x2, y2, buttonPress="left"):
    pyautogui.moveTo(x1, y1)
    pyautogui.mouseDown(); 
    time.sleep(1)
    pyautogui.moveTo(x2, y2)
    pyautogui.mouseUp()
    
    
def do_lst(lst):
    for action in lst:
        time.sleep(0.5)
        if type(action) == tuple:
            do_click(action[0], action[1])
        else:
            type_string(action)
    
def type_string(str):
    pyautogui.typewrite(str)
    pyautogui.press('enter')
    
def main():
    if len(sys.argv) > 1:
        while True:
            time.sleep(0.1)
            print(pyautogui.position())
        return

        
    
    # read the file and parse 
    for row in read_file("items.csv").split('\n')[1:-1]:
        name, id, sum, num = tuple(row.split(','))
        FILL_FORM[6] = id
        if id == "209896174" or id == "319042800":
            sum = sum + "0"
        FILL_FORM[9] = sum
        FILL_FORM[12] = num
        FILL_FORM[15] = sum
        FILL_FORM[17] = str(datetime.datetime.now().year)
        FILL_FORM[19] = str(datetime.datetime.now().month)
        DRAG_FILE[1] = PATH + name.upper()
        
        cont = input("Next up: " + name + "\nReady for him?\n")
        print(cont)
        if not (cont.upper() == "YES" or cont.upper() == "Y"):
            break
        
        do_lst(OPEN_PORTAL)
        do_lst(OPEN_FORM)
        do_lst(FILL_FORM)
              
        time.sleep(0.2)
              
        pyautogui.keyDown('win')
        pyautogui.press('up')
        pyautogui.keyUp('win')
               
        time.sleep(0.2)
               
        pyautogui.keyDown('win')
        pyautogui.press('left')
        pyautogui.keyUp('win')
        
        time.sleep(0.2)
        
        do_lst(DRAG_FILE)
        drag(342, 200, 2112, 1264)
        do_click(1844, 1264)
        
        pyautogui.keyDown('win')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.keyUp('win')
        
        time.sleep(1)
        do_click(1229, 17)
        time.sleep(1)
        
        pyautogui.keyDown('win')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.keyUp('win')

        
    print("Goodbye Yagever")
    print(tam.TAM)


if __name__ == "__main__":
    main()