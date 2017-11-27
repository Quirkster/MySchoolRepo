import pyautogui
def main():
    pyautogui.moveTo(100,27,duration=2)
    pyautogui.click(x=100, y=27, clicks=1, interval=1, button='left')
    pyautogui.scroll(600,x=682,y=155)
    pyautogui.click(x=541, y=35, clicks=1, interval=1, button='left')
    pyautogui.typewrite('anna is awesome\n', interval=1)
    pyautogui.typewrite(' \n', interval=3)
    pyautogui.click(x=479, y=28, clicks=1, interval=1, button='left')
    pyautogui.click(x=438,y=42,clicks=1,interval=1,button='left')
    pyautogui.click(x=316,y=39, clicks=1, interval=1, button='left')
if __name__ == '__main__':
    main()
