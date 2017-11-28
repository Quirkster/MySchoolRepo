import pyautogui
def main():
    #pyautogui.moveTo(100,27,duration=1)
    pyautogui.click(x=24, y=738, clicks=1, interval=1, button='left')
    pyautogui.typewrite('chrome\n', interval=0.1)
    pyautogui.click(x=100, y=27, clicks=1, interval=0.5, button='left')
    pyautogui.scroll(600,x=682,y=155)
    pyautogui.hotkey('ctrl','t')
    pyautogui.typewrite('anna is awesome\n', interval=0.5)
    pyautogui.typewrite(' \n', interval=3)
    pyautogui.click(x=479, y=28, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=438,y=42,clicks=1,interval=0.5,button='left')
    pyautogui.click(x=316,y=39, clicks=2, interval=0.5, button='left')
if __name__ == '__main__':
    main()
