import pyautogui as pg
import webbrowser,time

mathhw = pg.confirm('Would you like to open your math homework?', 'math', ['yes', 'no'])
spanishw = pg.confirm('Would you like to open your spanish homework?', 'spanish', ['yes', 'no'])
englishhw = pg.confirm('Would you like to open your english homework?', 'english', ['yes', 'no'])
sciencehw = pg.confirm('Would you like to open your science homework?', 'science', ['yes', 'no'])
historyhw = pg.confirm('Would you like to open your history homework?', 'history', ['yes', 'no'])
webbrowser.open('https://mail.google.com')
time.sleep(1)
#pg.hotkey('winleft','up')
if mathhw == 'yes':
    math = pg.confirm('Which teacher do you have?', 'math', ['Donnalley','Spooner','Bixler','Carnegie','Bates','Basinet'])
    if math == 'Donnalley':
        webbrowser.open('https://docs.google.com/spreadsheets/u/0/d/1XCutu8j7jy6_HFJSNhbu_84J0msWd26Gsub6dfFRKTU/edit?usp=drive_web')
        pg.hotkey('enter')
        pg.hotkey('winleft','up')
    if math == 'Spooner':
        webbrowser.open('https://docs.google.com/spreadsheets/d/1z9UbIhHXRF8fkYxGdHQGGGu_LhLzAVOn3EWQWAR7bKg/edit#gid=1609266901')
        pg.hotkey('enter')
        pg.hotkey('winleft','up')
if spanishw == 'yes':
    #pg.hotkey('ctrl','t')
    webbrowser.open('https://senorsalazarspanishclass.wordpress.com/')
    #pg.hotkey('enter')
if englishhw == 'yes':
    #pg.hotkey('ctrl','t')
    webbrowser.open('https://docs.google.com/document/d/1YchlqX5JcEXXj1OBtWJRVhWjGqUmua90ChHbWr3vCoY/edit')
    #pg.hotkey('enter')
if sciencehw == 'yes':
    #pg.hotkey('ctrl','t')
    webbrowser.open('https://classroom.google.com/c/NTEwNTg0Mjk1NVpa')
    #pg.hotkey('enter')
if historyhw == 'yes':
    #pg.hotkey('ctrl','t')
    webbrowser.open('https://sites.google.com/a/gcds.net/spencer-history-8/')
    #pg.hotkey('enter')
