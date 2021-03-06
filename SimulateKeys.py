import keyboard
import win32gui
import re

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def simKeys():
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "windows" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0], 5)
            win32gui.SetForegroundWindow(i[0])
            break
    keyboard.send('F3')