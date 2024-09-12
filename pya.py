'''
Using PyAutoGUI
- To open vscode
- install clangd from extension
- install c++ testmate from extension
- install c++ helper from extension
- install cmake from extension
- install cmake tools from extension
'''
import pyautogui
import time
import subprocess


def open_vscode():
    subprocess.Popen(['code'])
    time.sleep(10)  

def install_extensions():
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    
    pyautogui.write('clangd')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=176, y=233)  
    time.sleep(2)
    pyautogui.click(x=532, y=261)  
    time.sleep(5)  
    pyautogui.click(x=168, y=154)
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.write('c++ testmate')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=176, y=233)  
    time.sleep(2)
    pyautogui.click(x=532, y=261)  
    time.sleep(5)  
    pyautogui.click(x=168, y=154)
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.write('c++ helper')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=176, y=233)  
    time.sleep(2)
    pyautogui.click(x=532, y=261)  
    time.sleep(5)  
    pyautogui.click(x=168, y=154)
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.write('cmake')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=176, y=233)  
    time.sleep(2)
    pyautogui.click(x=532, y=261)  
    time.sleep(5) 
    pyautogui.click(x=168, y=154)
    time.sleep(2)

    
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.write('cmake tools')
    time.sleep(2)    
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=176, y=233)  
    time.sleep(2)
    pyautogui.click(x=532, y=261)  
    time.sleep(5)  
    pyautogui.click(x=168, y=154)
    time.sleep(2)

def main():
    open_vscode()
    install_extensions()

if __name__ == '__main__':
    main()
