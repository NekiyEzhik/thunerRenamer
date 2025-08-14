from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint

from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QGroupBox,QFileDialog, QListWidget, QMessageBox
from PyQt5.QtGui import QFont, QColor, QIcon
from darktheme.widget_template import DarkApplication, DarkPalette
import json
import os
defualtSettings = {"Localization": "no", "game-dir": "", "lang": ""}
defualtData = {"Техника уничтожена": "Техника уничтожена", "Самолёт сбит": "Самолёт сбит", "Вертолёт сбит": "Вертолёт сбит", "Помощь в уничтожении противника": "Помощь в уничтожении противника", "Цель разведана": "Цель разведана", "В бой!": "В бой!", "Исследования": "Исследования", "Армия": "Армия", "Авиация": "Авиация", "Вертолёты": "Вертолёты", "Большой флот": "Большой флот", "Малый флот": "Малый флот", "Исследуемая техника": "Исследуемая техника", "Премиумная техника": "Премиумная техника", "Реалистичные бои": "Реалистичные бои", "Инвентарь": "Все неактивные предметы", "Выход": "Выход", "Да": "Да", "Нет": "Нет", "Готов": "Готов", "Попадание": "Попадание", "Критические повреждения": "Критические повреждения", "Фатальные повреждения": "Фатальные повреждения"}
# ЛОКАЛИЗАЦИЯ НА ДРУГИЕ ЯЗЫКИ
appPath = os.path.join(os.path.abspath('data.json').replace('data.json', ''),'thunderRenamer', '_internal')
print(appPath)
iconPath = os.path.join(appPath, 'thunderRenamer.png')
settingsPath = os.path.join(appPath, 'settings.json')
dataPath = os.path.join(appPath, 'data.json')
with open(settingsPath, 'r', encoding='utf-8') as file:
    settings = json.load(file)
with open(dataPath, 'r', encoding='utf-8') as file:
    cnstjson = json.load(file)
cnfgPath = os.path.join(settings['game-dir'], 'config.blk')
langPath = os.path.join(settings['game-dir'], 'lang', 'menu.csv')
defLangPath = os.path.join(appPath, 'menu.csv')
with open(defLangPath, 'r', encoding='utf-8') as file:
    defualtLangFile = file.read()
with open(os.path.join(appPath, 'engLocal.json'), 'r', encoding='utf-8') as file:
    langtitle = json.load(file)

def nextClick1():
    try:
        with open(cnfgPath, 'r', encoding='utf-8') as file:
            cnfgFile = file.read()
        helloWindow.hide()
        customization.show()
    except:
        win1 = QMessageBox()
        win1.setText(langtitle['dataerror'])
        win1.setWindowTitle(langtitle['error'])
        win1.setWindowIcon(QIcon(os.path.abspath('thunderRenamer.png').replace('thunderRenamer.png', '_internal/thunderRenamer.png')))
        win1.show()
        win1.exec_()

def replaceByIndex(string, index, word):
    return string[:index] + word + string[index+len(word):]


def gameFolder():
    global langPath
    global cnfgPath
    global cnfgFile
    gameDir = QFileDialog.getExistingDirectory()
    if gameDir == '':
        pass
    else:
        try:
            cnfgPath = os.path.join(gameDir, 'config.blk')
            with open(cnfgPath, 'r', encoding='utf-8') as file:
                cnfgFile = file.read()
            langPath = os.path.join(gameDir, 'lang')
            langPath = os.path.join(langPath, 'menu.csv')
            settings['game-dir'] = gameDir
            with open(settingsPath, 'w', encoding='utf-8') as file:
                json.dump(settings, file, ensure_ascii=False)
            nextBtn2.setStyleSheet(
                "QPushButton" \
                "{" \
                "background-color: blue;" \
                "}"            
            )
        except: 
            win1 = QMessageBox()
            win1.setText(langtitle['dataerror'])
            win1.setWindowTitle(langtitle['error'])
            win1.setWindowIcon(QIcon(os.path.abspath('thunderRenamer.png').replace('thunderRenamer.png', '_internal/thunderRenamer.png')))
            win1.show()
            win1.exec_()


def clickedItem():
    name = listTitle.selectedItems()[0].text()
    rename.clear()
    rename.setPlaceholderText(cnstjson[name])
    titleName.setText(f'<b>{name}</b>')
    titleName2.setText(f'{cnstjson[name]}')


def saveBtnFunc():
    try:
        name =listTitle.selectedItems()[0].text()
        text = rename.text()
        cnt = renamecnt.text()
        with open(langPath, 'r', encoding='utf-8') as file:
            lang = file.read()
        newLang = lang.replace(cnstjson[name], text)
        cnstjson[name] = text
        with open(langPath, 'w', encoding='utf-8') as file:
            file.write(newLang)
        with open(dataPath, 'w', encoding='utf-8') as file:
            json.dump(cnstjson, file, ensure_ascii=False)
        rename.clear()
        rename.setPlaceholderText(cnstjson[name])
        titleName2.setText(cnstjson[name])
    except:
        pass

def settPage():
    settingsBox.show()
    if settings['Localization'] == 'yes':
        settLangBtn.setStyleSheet(
            "QPushButton" \
            "{" \
            "background-color: red;" \
            "}"
        )
        settLangBtn.setText(langtitle['disable'])
    else:
        settLangBtn.setStyleSheet(
            "QPushButton" \
            "{" \
            "background-color: green;" \
            "}"
        )
        settLangBtn.setText(langtitle['enable'])

def openPage():
    openWin.show()

def settLang():
    if settLangBtn.text() == langtitle['enable']:
        settLangBtn.setStyleSheet(
            "QPushButton" \
            "{" \
            "background-color: red;" \
            "}"
        )
        settLangBtn.setText(langtitle['disable'])
        settings['Localization'] = 'yes'
        with open(settingsPath, 'w', encoding='utf-8') as file:
            json.dump(settings, file, ensure_ascii=False)
        with open(cnfgPath, 'r', encoding='utf-8') as file:
            cnfgFile = file.read()
        word = 'testLocalization:b='
        index = cnfgFile.find(word)
        if index == -1:
            newCnfgFile = cnfgFile.replace('debug{', 'debug{\n  testLocalization:b=yes')
            with open(cnfgPath, 'w', encoding='utf-8') as file:
                file.write(newCnfgFile)
        else:
            newCnfgFile = cnfgFile.replace('testLocalization:b=no', 'testLocalization:b=yes')
            with open(cnfgPath, 'w', encoding='utf-8') as file:
                file.write(newCnfgFile)
    elif settLangBtn.text() == langtitle['disable']:
        settLangBtn.setStyleSheet(
            "QPushButton" \
            "{" \
            "background-color: green;" \
            "}"
        )
        settLangBtn.setText(langtitle['enable'])
        settings['Localization'] = 'no'
        with open(settingsPath, 'w', encoding='utf-8') as file:
            json.dump(settings, file, ensure_ascii=False)
        with open(cnfgPath, 'r', encoding='utf-8') as file:
            cnfgFile = file.read()
        newCnfgFile = cnfgFile.replace('testLocalization:b=yes', 'testLocalization:b=no')
        with open(cnfgPath, 'w', encoding='utf-8') as file:
            file.write(newCnfgFile)

def openFeedbackSite():
    settingsBox.hide()
    os.system(os.path.join(appPath, 'example.html'))

def openLangFile1():
    openWin.hide()
    os.system(langPath)

def openConfigFile1():
    openWin.hide()
    os.system(cnfgPath)

def openHelpTxt():
    settingsBox.hide()
    if settings['lang'] == 'rus':
        os.system(os.path.join(appPath, 'help_rus.txt'))
    else:
        os.system(os.path.join(appPath, 'help_eng.txt'))


def resetSettings():
    settingsBox.hide()
    warningWindow.show()

def cancelReset():
    warningWindow.hide()

def addItemCancel():
    addItemWindow.hide()
def addItemOk():
    if addItemWindowLineEdit.text() != '':
        cnstjson[addItemWindowLineEdit.text()] = addItemWindowLineEdit.text()
        with open(dataPath, 'w', encoding='utf-8') as file:
            json.dump(cnstjson, file, ensure_ascii=False)
        addItemWindow.hide()
        listTitle.clear()
        for i in cnstjson:
            listTitle.addItem(i)
def addItem():
    addItemWindow.show()

def removeItem():
    name = listTitle.selectedItems()[0].text()
    with open(langPath, 'r', encoding='utf-8') as file:
        lang = file.read()
    
    del cnstjson[name]
    with open(dataPath, 'w', encoding='utf-8') as file:
        json.dump(cnstjson, file, ensure_ascii=False)
    listTitle.clear()
    for i in cnstjson:
        listTitle.addItem(i)
    

def okReset():
    warningWindow.hide()
    settingsBox.hide()
    customization.hide()
    with open(dataPath, 'w', encoding='utf-8') as file:
        json.dump(defualtData, file, ensure_ascii=False)
    with open(settingsPath, 'w', encoding='utf-8') as file:
        json.dump(defualtSettings, file, ensure_ascii=False)
    with open(langPath, 'w', encoding='utf-8') as file:
        file.write(defualtLangFile)
    os._exit(0)

def selectEng():
    global langtitle
    settings['lang'] = 'eng'
    with open(settingsPath, 'w', encoding='utf-8') as file:
        json.dump(settings, file, ensure_ascii=False)
    with open(os.path.join(appPath, 'engLocal.json'), 'r', encoding='utf-8') as file:
        langtitle = json.load(file)
    langWinNextBtn.show()
    langWinNextBtn.setText('Next')

def selectRus():
    global langtitle
    settings['lang'] = 'rus'
    with open(settingsPath, 'w', encoding='utf-8') as file:
        json.dump(settings, file, ensure_ascii=False)
    with open(os.path.join(appPath, 'rusLocal.json'), 'r', encoding='utf-8') as file:
        langtitle = json.load(file)
    langWinNextBtn.show()
    langWinNextBtn.setText('Дальше')


def langnext():
    global langtitle
    with open(settingsPath, 'r', encoding='utf-8') as file:
        settings = json.load(file)
    if settings['lang'] != '':
        if settings['lang'] == 'eng':
            with open(os.path.join(appPath, 'engLocal.json'), 'r', encoding='utf-8') as file:
                langtitle = json.load(file)
        elif settings['lang'] == 'rus':
            with open(os.path.join(appPath, 'rusLocal.json'), 'r', encoding='utf-8') as file:
                langtitle = json.load(file)
        langWin.hide()
        helloWindow.show()
        os._exit(0)
    
def langnback():
    helloWindow.hide()
    langWin.show()

if settings['lang'] == 'eng':
    with open(os.path.join(appPath, 'engLocal.json'), 'r', encoding='utf-8') as file:
        langtitle = json.load(file)
elif settings['lang'] == 'rus':
    with open(os.path.join(appPath, 'rusLocal.json'), 'r', encoding='utf-8') as file:
        langtitle = json.load(file)

def translateBtn():
    global langtitle
    if settings['lang'] == 'rus':    
        settings['lang'] = 'eng'
        with open(settingsPath, 'w', encoding='utf-8') as file:
            json.dump(settings, file, ensure_ascii=False)
        with open(os.path.join(appPath, 'engLocal.json'), 'r', encoding='utf-8') as file:
             langtitle = json.load(file)
    elif settings['lang'] == 'eng': 
        settings['lang'] = 'rus'
        with open(settingsPath, 'w', encoding='utf-8') as file:
            json.dump(settings, file, ensure_ascii=False)
        with open(os.path.join(appPath, 'rusLocal.json'), 'r', encoding='utf-8') as file:
            langtitle = json.load(file)
        
    os._exit(0)
app=QApplication([])
app.setPalette(DarkPalette())
app.setStyle('Fusion')
app.setFont(QFont('FRANKLIN GOTHIC MEDIUM', 12))
win=QWidget()
win.setWindowIcon(QIcon(os.path.abspath('thunderRenamer.png').replace('thunderRenamer.png', '_internal/thunderRenamer.png')))
win.setWindowTitle('Thunder Renamer')
win.resize(600,400)

langWin = QGroupBox()
langWin.setTitle('Select your language / Выберите свой язык')
langWinHline1 = QHBoxLayout()
langWinHline2 = QHBoxLayout()
langWinHline3 = QHBoxLayout()
langWinVline = QVBoxLayout()
langWinTitle = QLabel('Select your language to continue\nВыберите ваш язык, чтобы продолжить')
engBtn = QPushButton('English')
rusBtn = QPushButton('Русский')
langWinNextBtn = QPushButton('')
langWinNextBtn.hide()
langWinHline1.addWidget(langWinTitle, alignment=Qt.AlignCenter)
langWinHline2.addWidget(engBtn, alignment=Qt.AlignCenter)
langWinHline2.addWidget(rusBtn, alignment=Qt.AlignCenter)
langWinHline2.addWidget(langWinNextBtn, alignment=Qt.AlignCenter)
langWinVline.addLayout(langWinHline1)
langWinVline.addLayout(langWinHline2)
# langWinVline.addLayout(langWinHline3)
langWin.setLayout(langWinVline)
engBtn.clicked.connect(selectEng)
rusBtn.clicked.connect(selectRus)
langWinNextBtn.clicked.connect(langnext)

helloWindow = QGroupBox(langtitle['helloWinTitle'])
title2 = langtitle['HelloTitle']
titlelbl2 = QLabel(title2)
hbox2line1 = QHBoxLayout()
hbox2line2 = QHBoxLayout()
vbox2line = QVBoxLayout()
hbox2line1.addWidget(titlelbl2, alignment=Qt.AlignCenter)
hellobackBtn = QPushButton(langtitle['back'])
folderBtn2 = QPushButton(langtitle['browseBtn'])
nextBtn2 = QPushButton(langtitle['nextBtn'])

nextBtn2.setStyleSheet(
    "QPushButton:hover" \
    "{" \
    " background-color: red;" \
    "}"
)

hbox2line2.addWidget(hellobackBtn, alignment=Qt.AlignCenter)
hbox2line2.addWidget(folderBtn2, alignment=Qt.AlignCenter)
hbox2line2.addWidget(nextBtn2, alignment=Qt.AlignCenter)
vbox2line.addLayout(hbox2line1)
vbox2line.addLayout(hbox2line2)
helloWindow.setLayout(vbox2line)
nextBtn2.clicked.connect(nextClick1)
hellobackBtn.clicked.connect(langnback)
folderBtn2.clicked.connect(gameFolder)

customization = QGroupBox(langtitle['customizationWinTitle'])
customVline1 = QVBoxLayout()
customVline2 = QVBoxLayout()
customHline1 = QHBoxLayout()
customHline2 = QHBoxLayout()
customHline3 = QHBoxLayout()
listTitle = QListWidget()
addItemBtn = QPushButton(langtitle['addtitle'])
removeItemBtn = QPushButton(langtitle['removetitle'])
rename = QLineEdit()
renamecnt = QLineEdit()
titleName = QLabel(langtitle['chosetitle'])
titleName2 = QLabel('')
saveBtn = QPushButton(langtitle['save'])
settingsBtn = QPushButton(langtitle['settings'])

customVline1.addWidget(listTitle)
customHline3.addWidget(addItemBtn, alignment=Qt.AlignVCenter)
customHline3.addWidget(removeItemBtn, alignment=Qt.AlignVCenter)
customVline1.addLayout(customHline3)
customHline4 = QHBoxLayout()
customVline2.addWidget(titleName,alignment=Qt.AlignVCenter)
customVline2.addWidget(titleName2,alignment=Qt.AlignVCenter)
customHline4.addWidget(rename, alignment=Qt.AlignVCenter)
customHline4.addWidget(renamecnt, alignment=Qt.AlignVCenter)
renamecnt.setPlaceholderText(langtitle['cnt'])
customVline2.addLayout(customHline4)
customHline2.addWidget(saveBtn, alignment=Qt.AlignVCenter)
customHline2.addWidget(settingsBtn, alignment=Qt.AlignVCenter)
customVline2.addLayout(customHline2)
rename.setStyleSheet(
    "QLineEdit" \
    "{" \
    "width: 250px;"
    "}"
)
renamecnt.setStyleSheet(
    "QLineEdit" \
    "{" \
    "width: 50px;"
    "}"
)
saveBtn.setStyleSheet(
    "QPushButton" \
    "{" \
    "width: 100px;" \
    "background-color: green;" \
    "}"
    "QPushButton:hover" \
    "{" \
    "background-color: #006221;" \
    "}"
)

customHline1.addLayout(customVline1)
customHline1.addLayout(customVline2)
customization.setLayout(customHline1)


settingsBox = QGroupBox()
settingsBox.setWindowTitle(langtitle['settings'])
settingsBox.setWindowIcon(QIcon(os.path.abspath('thunderRenamer.png').replace('thunderRenamer.png', '_internal/thunderRenamer.png')))
settingsBox.resize(400,300)
settVline1 = QVBoxLayout()
settHline1 = QHBoxLayout()
settHline2 = QHBoxLayout()
settHline3 = QHBoxLayout()
settHline4 = QHBoxLayout()
settHlineLast = QHBoxLayout()
settTitle = QLabel(langtitle['switchuserlocal'])
settLangBtn = QPushButton(langtitle['enable'])
settOpenBtn = QPushButton(langtitle['open...'])
settTitle2 = QLabel(langtitle["pathtowt"])
settResetBtn = QPushButton(langtitle['resetSettings'])
settHelpBtn = QPushButton(langtitle['help'])
settDirectoryBtn = QPushButton(langtitle['browseBtn'])
spacing = QLabel('<hr>')
settTitle3 = QLabel(langtitle['translate'])
settTransBtn = QPushButton(langtitle['transbtn'])
settHline1.addWidget(settTitle, alignment=Qt.AlignCenter)
settHline1.addWidget(settLangBtn, alignment=Qt.AlignCenter)
settHline2.addWidget(settTitle2, alignment=Qt.AlignCenter)
settHline2.addWidget(settDirectoryBtn, alignment=Qt.AlignCenter)
settHline3.addWidget(settTitle3, alignment=Qt.AlignCenter)
settHline3.addWidget(settTransBtn, alignment=Qt.AlignCenter)
settHline4.addWidget(spacing)
settHlineLast.addWidget(settResetBtn, alignment=Qt.AlignLeft)
settHlineLast.addWidget(settHelpBtn, alignment=Qt.AlignRight)
settHlineLast.addWidget(settOpenBtn,alignment=Qt.AlignRight)
settVline1.addLayout(settHline1)
settVline1.addLayout(settHline2)
settVline1.addLayout(settHline3)
settVline1.addLayout(settHline4)
settVline1.addLayout(settHlineLast)
settingsBox.setLayout(settVline1)
settLangBtn.setStyleSheet(
    "QPushButton" \
    "{" \
    "background-color: green;" \
    "width: 75px;" \
    "}"
)
settTitle.setStyleSheet(
    "QLabel" \
    "{" \
    "text-align: center;" \
    "width: 100px;" \
    "}"
)
settTitle.setStyleSheet(
    "QLabel" \
    "{" \
    "text-align: center;" \
    "width: 100px;" \
    "}"
)
settOpenBtn.setStyleSheet(
    "QPushButton" \
    "{" \
    "width: 75px;" \
    "padding: 3px;" \
    "}"
)
settHelpBtn.setStyleSheet(
    "QPushButton" \
    "{" \
    "width: 75px;" \
    "padding: 3px;" \
    "}"
)
openWin = QGroupBox(langtitle['open...'])
openWin.resize(200,180)
openWin.setWindowTitle(langtitle['open'])
openWin.setWindowIcon(QIcon(os.path.abspath('thunderRenamer.png').replace('thunderRenamer.png', '_internal/thunderRenamer.png')))
openWinVLine = QVBoxLayout()
openConfigFile = QPushButton(langtitle['openconfigfile'])
openLangFile = QPushButton(langtitle['openlangfile'])
openWinVLine.addWidget(openConfigFile, alignment=Qt.AlignCenter)
openWinVLine.addWidget(openLangFile, alignment=Qt.AlignCenter)
openWin.setLayout(openWinVLine)
openWin.hide()

openConfigFile.setStyleSheet(
    "QPushButton" \
    "{" \
    "width: 140px;" \
    "}"
)
openLangFile.setStyleSheet(
    "QPushButton" \
    "{" \
    "width: 140px;" \
    "}"
)

warningWindow = QGroupBox()
warningWindow.setWindowTitle(langtitle['resetSettings'])
warningWindow.setWindowIcon(QIcon(os.path.abspath('thunderRenamer.png').replace('thunderRenamer.png', '_internal/thunderRenamer.png')))
warningWindowHline1 = QHBoxLayout()
warningWindowHline2 = QHBoxLayout()
warningWindowVline = QVBoxLayout()
warningWindowTitle = QLabel(langtitle['resetsettingswintitle'])
warningWindowHline1.addWidget(warningWindowTitle, alignment=Qt.AlignCenter)
warningWindowOkBtn = QPushButton(langtitle['reset'])
warningWindowCancelBtn = QPushButton(langtitle['cancel'])
warningWindowHline2.addWidget(warningWindowCancelBtn, alignment=Qt.AlignCenter)
warningWindowHline2.addWidget(warningWindowOkBtn, alignment=Qt.AlignCenter)
warningWindowVline.addLayout(warningWindowHline1)
warningWindowVline.addLayout(warningWindowHline2)
warningWindow.setLayout(warningWindowVline)
warningWindowOkBtn.setStyleSheet(
    "QPushButton" \
    "{" \
    "background-color: red;" \
    "}"
)

warningWindowCancelBtn.clicked.connect(cancelReset)
warningWindowOkBtn.clicked.connect(okReset)

addItemWindow = QGroupBox()
addItemWindow.setWindowTitle(langtitle['addtitle'])
addItemWindow.setWindowIcon(QIcon(os.path.abspath('thunderRenamer.png').replace('thunderRenamer.png', '_internal/thunderRenamer.png')))
addItemWindowHline1 = QHBoxLayout()
addItemWindowHline2 = QHBoxLayout()
addItemWindowVline = QVBoxLayout()
addItemWindowLineEdit = QLineEdit()
addItemWindowLineEdit.setPlaceholderText(langtitle['ingametitle'])
addItemWindowOkBtn = QPushButton(langtitle["add"])
addItemWindowCancelBtn = QPushButton(langtitle['cancel'])
addItemWindowHline1.addWidget(addItemWindowLineEdit)
addItemWindowHline2.addWidget(addItemWindowOkBtn)
addItemWindowHline2.addWidget(addItemWindowCancelBtn)
addItemWindowVline.addLayout(addItemWindowHline1)
addItemWindowVline.addLayout(addItemWindowHline2)
addItemWindow.setLayout(addItemWindowVline)


listTitle.itemClicked.connect(clickedItem)


Vline = QVBoxLayout()
Vline.addWidget(langWin)
Vline.addWidget(helloWindow)
Vline.addWidget(customization)
langWin.hide()
helloWindow.hide()
settingsBox.hide()
customization.hide()
for i in cnstjson:
    listTitle.addItem(i)
if settings['game-dir'] != '':
    customization.show()
else:
    if settings['lang'] == '':
        langWin.show()
    else:
        helloWindow.show()
addItemWindowOkBtn.clicked.connect(addItemOk)
addItemWindowCancelBtn.clicked.connect(addItemCancel)
addItemBtn.clicked.connect(addItem)
removeItemBtn.clicked.connect(removeItem)
saveBtn.clicked.connect(saveBtnFunc)
openLangFile.clicked.connect(openLangFile1)
openConfigFile.clicked.connect(openConfigFile1)
settResetBtn.clicked.connect(resetSettings)
settHelpBtn.clicked.connect(openHelpTxt)
settingsBtn.clicked.connect(settPage)
settOpenBtn.clicked.connect(openPage)
settLangBtn.clicked.connect(settLang)
settDirectoryBtn.clicked.connect(gameFolder)
settTransBtn.clicked.connect(translateBtn)
listofholder = [addItemWindowLineEdit]
listoftitleswin = [addItemWindow,warningWindow,openWin,openWin]
win.setLayout(Vline)
win.show()
app.exec_()
print('h' \
'e' \
'l' \
'l' \
'o' \
'w')