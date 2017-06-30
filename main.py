import Tkinter  # For Tkinter Widgets
import ttk      # For advanced tkinter widgets
from XMLEditor import *     # XML Updater in separate .py
from SimulateKeys import *  # Key Simulator in separate .py
from FileOpen import *      # File Explorer in separate .py
from PlayerImport import *
import time



# Global Variables
recordClickTime = time.time()   # used to prevent double clicks from starting/stopping recording



def updatePlayers():    # updates XML for both players
    # print("Updating Both Players")
    XMLPlayerUpdate(1, P1Prefix.get(), P1Tag.get(), P1Score.get())
    XMLPlayerUpdate(2, P2Prefix.get(), P2Tag.get(), P2Score.get())

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
    XMLPlayerUpdate(1, P1Prefix.get(), P1Tag.get(), P1Score.get())

def updatePlayer2():    # Updates only P2 XML
    XMLPlayerUpdate(2, P2Prefix.get(), P2Tag.get(), P2Score.get())

def updateMatch():
    XMLMatchUpdate(matchPreVar.get(), matchRVar.get(), matchNumVar.get(), GameInfo.get(), OtherInfo1.get(), OtherInfo2.get())

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

def clearAllPlayer():
    P1Prefix.delete(0, 'end')
    P1Prefix.insert(0, 'Crew')
    P1Prefix.configure(foreground='#cccccc')
    P1Tag.delete(0, 'end')
    P1Tag.insert(0, "Player Tag")
    P1Tag.configure(foreground='#cccccc')
    P1Score.delete(0, 'end')
    P1Score.insert(0, '0')

    P2Prefix.delete(0, 'end')
    P2Prefix.insert(0, 'Crew')
    P2Prefix.configure(foreground='#cccccc')
    P2Tag.delete(0, 'end')
    P2Tag.insert(0, "Player Tag")
    P2Tag.configure(foreground='#cccccc')
    P2Score.delete(0, 'end')
    P2Score.insert(0, '0')

def clearAllMatch():
    matchPreVar.set('')
    matchRVar.set('')
    matchNumVar.set('')

    GameInfo.delete(0, 'end')
    GameInfo.insert(0, 'Game')
    GameInfo.configure(foreground='#cccccc')
    OtherInfo1.delete(0, 'end')
    OtherInfo1.insert(0, 'Other Info')
    OtherInfo1.configure(foreground='#cccccc')
    OtherInfo2.delete(0, 'end')
    OtherInfo2.insert(0, 'Other Info')
    OtherInfo2.configure(foreground='#cccccc')

def updatePlayerList(pList):
    pList.delete(0, 'end')
    for player in givePlayers():
        pList.insert('end', player)

def removePlayerFromList(playerList):
    # player = str(playerList.get(playerList.curselection()))
    player = playerList.get('anchor')
    removePlayer(player)
    updatePlayerList(playerList)

def addPlayerToList(pre, tag, pList):
    addPlayer(pre.get(), tag.get())
    updatePlayerList(pList)

def openImportPlayers():
    # Create Top Window
    playerImportWindow = Tkinter.Toplevel()
    playerImportWindow.title("Player Import")
    playerImportWindow.geometry('%dx%d+1390+730' % (width/4, height))

    # Create LabelFrame
    playerInfoFrame = ttk.LabelFrame(playerImportWindow, text='Player Info')

    # Create Entries
    playerAddPre = Tkinter.Entry(playerInfoFrame, foreground='#cccccc')
    playerAddPre.configure(font=('default', 16))
    playerAddPre.insert(0, "Crew")
    playerAddPre.bind('<FocusIn>', clearEntry)

    playerAddTag = Tkinter.Entry(playerInfoFrame, foreground='#cccccc')
    playerAddTag.configure(font=('default', 16))
    playerAddTag.insert(0, "Player Tag")
    playerAddTag.bind('<FocusIn>', clearEntry)

    # Create ListBox
    scrollbar = Tkinter.Scrollbar(playerInfoFrame, orient='vertical')
    playerList = Tkinter.Listbox(playerInfoFrame, yscrollcommand=scrollbar.set)
    scrollbar.configure(command=playerList.yview)
    updatePlayerList(playerList)

    # Create Button
    removeBtn = Tkinter.Button(playerInfoFrame, text='Remove Player',
    command=lambda playerList=playerList: removePlayerFromList(playerList))
    addBtn = Tkinter.Button(playerInfoFrame, text='Add Player',
    command=lambda playerAddTag=playerAddTag, playerAddPre=playerAddPre, playerList=playerList: addPlayerToList(playerAddPre, playerAddTag, playerList))

    # Place Elements
    playerInfoFrame.place(x=5, y=5, anchor='nw', width=470, height=270)
    playerAddPre.place(x=5, y=5, anchor='nw', height=30, width=70)
    playerAddTag.place(x=85, y=5, anchor='nw', height=30, width=170)
    playerList.place(x=265, y=5, anchor='nw', width=185, height=190)
    scrollbar.place(x=450, y=5, width=15, height=190)
    addBtn.place(x=265, y=205, anchor='nw', height=30, width=90)
    removeBtn.place(x=365, y=205, anchor='nw', width=90, height=30)


# Test Functions
def printPlayers():
    print(givePlayers())



# Create Window
window = Tkinter.Tk()
window.title("Stream Master")           # Window Title Name
width = window.winfo_screenwidth()-15
height = window.winfo_screenheight()/4
window.geometry("%dx%d+0+730" % (width, height))  # Size Window
window.wm_iconbitmap('favicon.ico')     # Window Icon



# Create Frames to hold other widgets
PlayerFrame = ttk.LabelFrame(window, text='Player Info')
MatchFrame = ttk.LabelFrame(window, text='Match Info')
OtherFrame = ttk.LabelFrame(window, text='Other')



# Creates Entries for Crew names, Tags, and Score for P1
# P1 Prefix
P1Prefix = Tkinter.Entry(PlayerFrame, foreground='#cccccc')
P1Prefix.configure(font=('default', 16))
P1Prefix.insert(0, "Crew")
P1Prefix.bind('<FocusIn>', clearEntry)
# P1 Tag
P1Tag = Tkinter.Entry(PlayerFrame, foreground='#cccccc')
P1Tag.configure(font=('default', 16))
P1Tag.insert(0, "Player Tag")
P1Tag.bind('<FocusIn>', clearEntry)
# P1 Score
P1Score = Tkinter.Entry(PlayerFrame)
P1Score.insert(0, '0')
P1Score.configure(font=('default', 30), justify='center')
# P1 Score + -
P1ScorePlus = Tkinter.Button(PlayerFrame, text='+', command=score1Plus)
P1ScoreMinus = Tkinter.Button(PlayerFrame, text='-', command=score1Minus)



# Creates Entries for Crew names, Tags, and Score for P2
# P2 Prefix
P2Prefix = Tkinter.Entry(PlayerFrame, foreground='#cccccc')
P2Prefix.configure(font=('default', 16))
P2Prefix.insert(0, "Crew")
P2Prefix.bind('<FocusIn>', clearEntry)
# P2 Tag
P2Tag = Tkinter.Entry(PlayerFrame, foreground='#cccccc')
P2Tag.configure(font=('default', 16))
P2Tag.insert(0, "Player Tag")
P2Tag.bind('<FocusIn>', clearEntry)
# P2 Score
P2Score = Tkinter.Entry(PlayerFrame)
P2Score.insert(0, '0')
P2Score.configure(font=('default', 30), justify='center')
# P2 Score + -
P2ScorePlus = Tkinter.Button(PlayerFrame, text='+', command=score2Plus)
P2ScoreMinus = Tkinter.Button(PlayerFrame, text='-', command=score2Minus)



# Match Info
matchPreVar = Tkinter.StringVar(window)
matchPreVar.set('Winners')
MatchPrefix = Tkinter.OptionMenu(MatchFrame, matchPreVar, '', 'Winners', 'Losers', 'Money Match', 'Friendlies')
matchRVar = Tkinter.StringVar(window)
matchRVar.set('Round')
MatchRound = Tkinter.OptionMenu(MatchFrame, matchRVar, '', 'Round', 'Quarters', 'Semis', 'Finals', 'Grand Finals')
matchNumVar = Tkinter.StringVar(window)
matchNumVar.set('1')
MatchNum = Tkinter.OptionMenu(MatchFrame, matchNumVar, '', '1', '2', '3', '4', '5', '[R]')
# Game Info
GameInfo = Tkinter.Entry(MatchFrame, foreground='#cccccc')
GameInfo.configure(font=('default', 16))
GameInfo.insert(0, "Game")
GameInfo.bind('<FocusIn>', clearEntry)
# Other Info 1 and 2
OtherInfo1 = Tkinter.Entry(MatchFrame, foreground='#cccccc')
OtherInfo1.configure(font=('default', 16))
OtherInfo1.insert(0, "Other Info")
OtherInfo1.bind('<FocusIn>', clearEntry)
OtherInfo2 = Tkinter.Entry(MatchFrame, foreground='#cccccc')
OtherInfo2.configure(font=('default', 16))
OtherInfo2.insert(0, "Other Info")
OtherInfo2.bind('<FocusIn>', clearEntry)



# Creates Buttons for updating and swapping info, also recording toggle
P1Update = Tkinter.Button(PlayerFrame, text="Update", command=updatePlayer1)
P2Update = Tkinter.Button(PlayerFrame, text="Update", command=updatePlayer2)
DoubleUpdate = Tkinter.Button(PlayerFrame, text='Update All', command=updatePlayers)
SwapPlayers = Tkinter.Button(PlayerFrame, text='Swap', command=swapPlayers)
ClearAllPlayer = Tkinter.Button(PlayerFrame, text='Clear All', command=clearAllPlayer)

ClearAllMatch = Tkinter.Button(MatchFrame, text='Clear All', command=clearAllMatch)
MatchUpdate = Tkinter.Button(MatchFrame, text='Update', command=updateMatch)

recordBtn = Tkinter.Button(OtherFrame, text='Start Recording', command=recordingToggle)
openXML = Tkinter.Button(OtherFrame, text='Open XML Folder', command=openXMLFolder)
importPlayer = Tkinter.Button(OtherFrame, text='Player Import', command=openImportPlayers)
options = Tkinter.Button(OtherFrame, text='Options', command=printPlayers)



# Creates Separators to organize widgets
MatchSplit = ttk.Separator(PlayerFrame, orient='horizontal')
PlayerSplit = ttk.Separator(PlayerFrame, orient='vertical')
InfoSplit = ttk.Separator(MatchFrame, orient='horizontal')



# Creates Label with Logo
logoIMG = Tkinter.PhotoImage(file="StreamMasterLogo.gif")
logo = Tkinter.Label(window, image=logoIMG)



# Add Elements to Window in order
logo.place(x=0, y=0, anchor='nw')

# Player Frame
PlayerFrame.place(x=0, y=101, anchor='nw', height=165, width=730)

P1Prefix.place(x=10, y=5, anchor='nw', height=30, width=70)
P1Tag.place(x=95, y=5, anchor='nw', height=30, width=150)
P1Update.place(x=260, y=70, anchor='nw', height=30, width=90)
P1Score.place(x=260, y=5, anchor='nw', height=60, width=60)
P1ScorePlus.place(x=320, y=5, anchor='nw', height=30, width=30)
P1ScoreMinus.place(x=320, y=35, anchor='nw', height=30, width=30)

MatchSplit.place(x=5, y=110, anchor='nw', width=715)
PlayerSplit.place(x=365, y=0, anchor='nw', height=100)

P2Prefix.place(x=375, y=5, anchor='nw', height=30, width=70)
P2Tag.place(x=460, y=5, anchor='nw', height=30, width=150)
P2Update.place(x=625, y=70, anchor='nw', height=30, width=90)
P2Score.place(x=625, y=5, anchor='nw', height=60, width=60)
P2ScorePlus.place(x=685, y=5, anchor='nw', height=30, width=30)
P2ScoreMinus.place(x=685, y=35, anchor='nw', height=30, width=30)

DoubleUpdate.place(x=625, y=115, anchor='nw',height=30, width=90)
SwapPlayers.place(x=320, y=115, anchor='nw', height=30, width=90)
ClearAllPlayer.place(x=10, y=115, anchor='nw', height=30, width=90)

# Match Frame
MatchFrame.place(x=735, y=101, anchor='nw', height=165, width=635)
MatchPrefix.place(x=10, y=5, anchor='nw', height=30, width=130)
MatchRound.place(x=145, y=5, anchor='nw', height=30, width=110)
MatchNum.place(x=260, y=5, anchor='nw', height=30, width=60)
OtherInfo1.place(x=330, y=5, anchor='nw', height=30, width=290)
OtherInfo2.place(x=330, y=45, anchor='nw', height=30, width=190)
GameInfo.place(x=115, y=45, anchor='nw', height=30, width=200)
MatchUpdate.place(x=530, y=45, anchor='nw', height=30, width=90)
ClearAllMatch.place(x=10, y=45, anchor='nw', height=30, width=90)
InfoSplit.place(x=5, y=80, anchor='nw', width=620)

# Other Frame
OtherFrame.place(x=1660, y=101, anchor='nw', height=165, width=235)
recordBtn.place(x=10, y=5, anchor='nw', height=30, width=100)
openXML.place(x=120, y=5, anchor='nw', height=30, width=100)
importPlayer.place(x=10, y=45, anchor='nw', height=30, width=100)
options.place(x=120, y=45, anchor='nw', height=30, width=100)



# Start Window
window.mainloop()
