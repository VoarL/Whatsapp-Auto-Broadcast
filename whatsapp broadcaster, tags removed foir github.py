#all these are installed from pip at 32bit location
#python 3.7 script
from PIL import ImageGrab, Image, ImageDraw
import os
import time
import win32api, win32con #pywin32
import pyautogui
import pydirectinput
import webbrowser
import pyodbc
import extcolors
from datetime import datetime


# Globals
# ------------------ 
x_pad = 0#-14 # Using 3840x2160 at 125% zoom so use pads to for other res
y_pad = 0#-35
x_coded_res = 3840
y_coded_res = 2160
zoom_coded_res = 100
x_res = x_coded_res#3440
y_res = y_coded_res#1440
zoom_res = 100
error_reset = False

def screenGrab():
    box = (x_pad+1, y_pad+1, 1920,1080)
    #box = ()
    im = ImageGrab.grab()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print ("Click.")          #completely optional. But nice for debugging purposes.
    time.sleep(.4)

def leftclickFast():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)

def mousePos(cord):
    win32api.SetCursorPos((x_pad+int(cord[0]*(x_res/x_coded_res)*(zoom_res/zoom_coded_res)), y_pad+int(cord[1]*(y_res/y_coded_res)*(zoom_res/zoom_coded_res))))
    
def loop_get_cords():
    while(1):
        x,y = win32api.GetCursorPos()
        #x = x - x_pad
        #y = y - y_pad
        print (x,y)
        time.sleep(0.5)
  
def get_cords():
    x,y = win32api.GetCursorPos()
    #x = x - x_pad
    #y = y - y_pad
    print (x,y)

def return_cords():
    x,y = win32api.GetCursorPos()
    #x = x - x_pad
    #y = y - y_pad
    return x, y

def start():
    #location of first menu
    mousePos((182, 225))
    leftClick()
    time.sleep(.1)


def keyboard():
    pyautogui.keyDown("alt")
    time.sleep(.1)
    pyautogui.press("tab")
    time.sleep(.1)
    pyautogui.press("tab")
    time.sleep(.1)
    #pyautogui.press("tab")
    pyautogui.keyUp("alt")
    try:
        while True:
            pyautogui.scroll(-10000)
    except KeyboardInterrupt:
        pass

def whatsapp_broadcast_all_contacts():
    #4k screen, samsung dex full on s20 fe 5g, whatsapp on left side of screen

    #first start broadcast page
    #mousePos((1865, 128))
    #leftClick()
    #time.sleep(0.5)
    #mousePos((1650, 225))
    #leftClick()
    #time.sleep(0.5)

    #search button, nvm manually locate first text
    #mousePos((1855, 129))

    #select contacts
    count = 0
    
    while(count < 243):
        count2 = 0
        while(count2 < 13):
            r1,g1,b1 = return_color(110,477+count2*128)
            if r1 >= 245 and g1 >= 245 and b1 >= 245:
                mousePos((823, 427+count2*128))
                leftclickFast()    
            count2 += 1
            time.sleep(0.08)
            
        count += 13
        count2 = 0
        while(count2 < 13):
            pyautogui.scroll(-1000)
            time.sleep(0.05)
            count2 += 1
        time.sleep(0.2)
    
 


def main():
    whatsapp_broadcast_all_contacts()
 
if __name__ == '__main__':
    main()

def cordDictionary(cord_type):
    if cord_type == "post_button":
        if x_res == 3840 and y_res == 2160 and zoom_res == 125:
            return (256, 1368)
        elif x_res == 3840 and y_res == 2160 and zoom_res == 100:
            return (255, 1582)
        
