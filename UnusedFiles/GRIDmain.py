import Tkinter  # For Tkinter Widgets
import ttk      # For advanced tkinter widgets
from XMLEditor import *     # XML Updater in separate .py
from SimulateKeys import *  # Key Simulator in separate .py
import time

recordClickTime = time.time()   # used to prevent double clicks from starting/stopping recording

window = Tkinter.Tk()                   # Create Window
window.title("Stream Master")           # Window Title Name
width = window.winfo_screenwidth() - 20
height = window.winfo_screenheight()/4
window.geometry("%dx%d" % (width, height))  # Size Window
window.wm_iconbitmap('favicon.ico')     # Window Icon

def updatePlayers():    # updates XML for both players
    # print("Updating Both Players")
    XMLUpdate(1, P1Prefix.get(), P1Tag.get(), P1Score.get())
    XMLUpdate(2, P2Prefix.get(), P2Tag.get(), P2Score.get())

def recordingToggle():  # Toggles Starrt/Stop for recording
    global recordClickTime
    if (time.time() - recordClickTime) > 1:
        simKeys()   # Switches focus to OBS and hotkeys F4
        recordClickTime = time.time()
        if recordBtn['text'] == 'Start Recording':
            recordBtn.configure(text='Stop Recording')
        else:
            recordBtn.configure(text='Start Recording')

def updatePlayer1():    # Updates only P1 XML
    XMLUpdate(1, P1Prefix.get(), P1Tag.get(), P1Score.get())

def updatePlayer2():    # Updates only P2 XML
    XMLUpdate(2, P2Prefix.get(), P2Tag.get(), P2Score.get())

def swapPlayers():  # Swaps between both players info
    tempTag = P1Tag.get()
    tempPre = P1Prefix.get()
    tempSco = P1Score.get()

    P1Tag.delete(0, 'end')
    P1Prefix.delete(0, 'end')
    P1Score.delete(0, 'end')

    P1Tag.insert(0, P2Tag.get())
    P1Prefix.insert(0, P2Prefix.get())
    P1Score.insert(0, P2Score.get())

    P2Tag.delete(0, 'end')
    P2Prefix.delete(0, 'end')
    P2Score.delete(0, 'end')

    P2Tag.insert(0, tempTag)
    P2Prefix.insert(0, tempPre)
    P2Score.insert(0, tempSco)

def clearEntry(event):  # Clears entry text, only if 1st time
    if str(event.widget['foreground']) == '#cccccc':
        event.widget.delete(0, 'end')
        event.widget.configure(foreground='#000000')

def score1Plus():   # ++to score for P1
    scoreInt = int(P1Score.get())
    scoreInt += 1
    P1Score.delete(0, 'end')
    P1Score.insert(0, scoreInt)

def score1Minus():   # --to score for P1
    scoreInt = int(P1Score.get())
    scoreInt -= 1
    P1Score.delete(0, 'end')
    P1Score.insert(0, scoreInt)

def score2Plus():   # ++to score for P1
    scoreInt = int(P2Score.get())
    scoreInt += 1
    P2Score.delete(0, 'end')
    P2Score.insert(0, scoreInt)

def score2Minus():   # --to score for P1
    scoreInt = int(P2Score.get())
    scoreInt -= 1
    P2Score.delete(0, 'end')
    P2Score.insert(0, scoreInt)

# Create Frames to hold other widgets
PlayerFrame = ttk.LabelFrame(window, text='Player Info')
InfoFrame = ttk.LabelFrame(window, text='Other Info')

# Creates Entries for Crew names, Tags, and Score for P1
P1Prefix = Tkinter.Entry(PlayerFrame, width=5, foreground='#cccccc')
P1Tag = Tkinter.Entry(PlayerFrame, width=25, foreground='#cccccc')
P1Prefix.insert(0, "Crew")
P1Tag.insert(0, "Player Tag")
P1Tag.bind('<FocusIn>', clearEntry)
P1Prefix.bind('<FocusIn>', clearEntry)
P1Score = Tkinter.Entry(PlayerFrame, width=2)
P1Score.insert(0, '0')
P1Score.configure(font=('default' , 24), justify='center')
P1ScorePlus = Tkinter.Button(PlayerFrame, text='+', width=2, height=1, command=score1Plus)
P1ScoreMinus = Tkinter.Button(PlayerFrame, text='-', width=2, height=1, command=score1Minus)

# Creates Entries for Crew names, Tags, and Score for P2
P2Prefix = Tkinter.Entry(PlayerFrame, width=5, foreground='#cccccc')
P2Tag = Tkinter.Entry(PlayerFrame, width=25, foreground='#cccccc')
P2Prefix.insert(0, "Crew")
P2Tag.insert(0, "Player Tag")
P2Tag.bind('<FocusIn>', clearEntry)
P2Prefix.bind('<FocusIn>', clearEntry)
P2Score = Tkinter.Entry(PlayerFrame, width=2)
P2Score.insert(0, '0')
P2Score.configure(font=('default' , 24), justify='center')
P2ScorePlus = Tkinter.Button(PlayerFrame, text='+', width=2, height=1, command=score2Plus)
P2ScoreMinus = Tkinter.Button(PlayerFrame, text='-', width=2, height=1, command=score2Minus)

# Creates Buttons for updating and swapping info, also recording toggle
P1Update = Tkinter.Button(PlayerFrame, text="Update", command=updatePlayer1)
P2Update = Tkinter.Button(PlayerFrame, text="Update", command=updatePlayer2)
DoubleUpdate = Tkinter.Button(PlayerFrame, text='Update All', command=updatePlayers)
SwapPlayers = Tkinter.Button(PlayerFrame, text='Swap', command=swapPlayers)
recordBtn = Tkinter.Button(InfoFrame, text='Start Recording', command=recordingToggle)

# Creates Separators to organize widgets
PlayerLine = ttk.Separator(PlayerFrame, orient='vertical')
PlayerSplit = ttk.Separator(PlayerFrame, orient='horizontal')

# Creates Label with Logo
logoIMG = Tkinter.PhotoImage(file="StreamMasterLogo.gif")
logo = Tkinter.Label(window, image=logoIMG)

# Add Elements to Window in order
logo.grid(row=0, column=0, sticky='w')

PlayerFrame.grid(row=1, column=0, sticky='w', ipadx=3, ipady=3)

P1Prefix.grid(row=1, column=0, sticky='w')
P1Tag.grid(row=1, column=10, rowspan=1, sticky='w')
P1Update.grid(row=2, column=0, sticky='w')
P1Score.grid(row=1,column=11, sticky='w')
P1ScorePlus.grid(row=1, column=12, sticky='n', columnspan=1, rowspan=1)
P1ScoreMinus.grid(row=1, column=12, sticky='s', columnspan=1, rowspan=1)

PlayerLine.grid(row=0, column=13, sticky='ns', rowspan=3, padx=10, pady=0)
PlayerSplit.grid(row=3, column=0, sticky='ew', columnspan=30, padx=3, pady=7)

P2Prefix.grid(row=1, column=14, sticky='w')
P2Tag.grid(row=1, column=24, rowspan=1, sticky='w')
P2Update.grid(row=2, column=14, sticky='w')
P2Score.grid(row=1,column=25, sticky='w')
P2ScorePlus.grid(row=1, column=26, sticky='n', columnspan=1, rowspan=1)
P2ScoreMinus.grid(row=1, column=26, sticky='s', columnspan=1, rowspan=1)

SwapPlayers.grid(row=4, column=13)
DoubleUpdate.grid(row=4, column=24, sticky='e')

InfoFrame.grid(row=1, column=15, sticky='e', ipadx=3, ipady=3)
recordBtn.grid(row=1, column=1, sticky='w')

# Start Window
window.mainloop()
