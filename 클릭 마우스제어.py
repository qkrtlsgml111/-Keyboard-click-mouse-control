import keyboard           

import pyautogui as auto  
import time                   
  
while True:          
    try:
        if keyboard.is_pressed('f1'):   
            print("F1")                      
            time.sleep(0.1)              
        elif keyboard.is_pressed('f2'):
            print("F2")           
            time.sleep(0.1)
        elif keyboard.is_pressed('f3'):
            print("F3")           
            time.sleep(0.1)
        elif keyboard.is_pressed('f4'):
            print("F4")           
            time.sleep(0.1)
        elif keyboard.is_pressed('f5'):
            print("F5")           
            time.sleep(0.1)
        elif keyboard.is_pressed('f6'):
            print("F6")           
            time.sleep(0.1)
        elif keyboard.is_pressed('f7'):
            print("F7")           
            time.sleep(0.1)
        elif keyboard.is_pressed('f8'):
            print("F8")           
            time.sleep(0.1)
        elif keyboard.is_pressed('f9'):
            print("F9")           
            time.sleep(0.1)
        elif keyboard.is_pressed('f10'):
            print("F10")           
            time.sleep(0.1)            
        elif keyboard.is_pressed('w'):
            print("w")             
            auto.move(0, -10)
            time.sleep(0.1)            
        elif keyboard.is_pressed('a'):
            print("a")              
            auto.move(-10, 0)
            time.sleep(0.1)            
        elif keyboard.is_pressed('s'):
            print("s")              
            auto.move(0, 10)
            time.sleep(0.1)            
        elif keyboard.is_pressed('d'):
            print("d")               
            auto.move(10, 0)
            time.sleep(0.1)            
        else:
            pass
    except:
        pass