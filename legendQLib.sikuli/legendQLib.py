# -*- coding: utf-8 -*-

from sikuli import *
import time

# ActionMethodWithRegion
# param region: In this given region, find and click the pattern in 30 sec.
# param pattern: The target you want to click, which could be a string, pic or something else.
# return: null
def ActionMethodWithRegion(region, pattern):
    if region.exists(pattern, 30):
        region.click(pattern)
        return True
    else:
        return False

# ActionMethod
# If myRegion exists, invoke ActionMethodWithRegion(myRegion, pattern)
# param pattern: The target you want to click, which could be a string, pic or something else.
# return: null
def ActionMethod(pattern):
    ActionMethodWithRegion(SCREEN, pattern)
    return

# Log
# For any textEditor you assign, type the log into.
# param s: 
# return: null
def Log(s):
    if globalLogger:
        wait(1)
        globalLogger.focus()
        wait(1)
        type(s)
        wait(1)
        globalLogger.focus()
        wait(1)
    else:
        print(s)
    return

def closeSuprise():
    while exists("1380553164626.png"):
        click("1380553164626.png")
        wait(1)

# check region image is exists and click
def checkClick(obj):
    if exists(obj):
        click(obj)

# wait region image and click
def waitAndClick(obj, sec):
    wait(obj, sec)
    click(obj)
    return

def protectTonLauResult():
    print("nextStep")
    returnValue = true
    if exists("1379785615163.png"):
        click("1379785615163.png")
    elif exists("1379785915692.png"):
        click("1379785915692.png")
    elif exists("1379785955990.png"):
        click("1379785955990.png")
    elif exists("1379810380156.png"):
        click("1379810380156.png")
    elif exists("1379784900486.png"):
        click("1379784900486.png")
    elif exists("1379960592944.png"):
       click("1379960611444.png")
    else:
        returnValue = false
    wait(1)
    return returnValue

# create game for first B studenet
def createGame(firstStudent):
    print('create game...')
    checkClick("1380695415869-1.png")
    
    print('select first student...')
    wait("1380695482077-1.png", 30)
    checkClick(firstStudent)
    checkClick("1380695515823-1.png")

def ChanAnFight():
    ActionMethod(Pattern("1380562324428.png").similar(0.50))
    fight()
    return

# run tutorial and expect Ace student
def runTutorial(firstAce):
    count = 1
    while 1:
        Log('starting pickup process %i time' % (count))
        ActionMethod("1380298064898-1.png")
        ActionMethod("1380298227453.png")
        ActionMethod("1380298278558.png")
        ChanAnFight()
        ActionMethod("1380337327356.png")
        returnTopMenu()
        firstStudent()
        buildFormat()
        ChanAnFight()
        ActionMethod("1380337327356.png")
        ActionMethod("1380340309707.png")
        returnTopMenu()
        equip()
        package()
        ChanAnFight()
        ActionMethod("1380337327356.png")
        returnTopMenu()
        pickupReturn=pickStudent(1,["FanYao", "InWan", "ShenFaiFai", "GenYeoShen"]) 
        if pickupReturn[1] == "NoMan" and pickupReturn[0] >= 2:
            Log('pick up people in %i time failure!' % (count))
            count += 1
            clickXToBack(SCREEN)
            gotoReset()
        else:
            popup("find people:%s" % (s))
            return

#    stud = pickStudent(0, firstAce)
#    print("stud: %s" % stud)
#    b = 0
#    if stud >= 4:
#        b = 1

    return b

# gotoreset
# reset the account. Note, you have to invoke returnTopMenu before this method, for be suring that we could go from setting options.
# return: null
def gotoreset():
    ActionMethod("1380297823894.png")
    ActionMethod("1380297843385.png")
    wait(3)
    reset("1380292721591.png", "1380292736191.png")
    wait(3)
    resetFailCondition()
    return


# leftRegion
# The left screen of myRegion. To decrease the searching area for finding patterns.
# return: null
def leftRegion():
    myRegion = SCREEN
    return Region(myRegion.getX(), myRegion.getY(), myRegion.getW() / 2, myRegion.getH())

# rightUpRegion
# one-fouth of myRegion in RightUp side. For decreasing the searching area.
# return: null
def rightUpRegion():
    myRegion = SCREEN
    return Region(myRegion.getX() + (myRegion.getW() / 2), myRegion.getY(), myRegion.getW() / 2, myRegion.getH()/2)    

#OCR method
#param leftOfOCR: the picture which is left from OCR.
#param rightOfOCR: the picture which is right from OCR
#return: the OCR string in ASCII
def OCR(leftOfOCR, rightOfOCR):
    regLeft = find(leftOfOCR)
    regRight = find(rightOfOCR)
    newX = regLeft.getX() + regLeft.getW()
    textReg = Region(newX, regLeft.getY(), regRight.getX() - newX, regLeft.getH())
    s = textReg.text()
    print('origin s:%s' % (s))
    s1 = s.replace(".","")
    s2 = s1.replace(" ","")
    s3 = filter(onlyascii, s2)
    print ('after proofread: %s' % s3)

    return s3

# fillRegCode
# filling the regCode while reset the account.
# param s: OCR string
# return: null
def fillRegCode(s):
    click("1380293789145-1.png")
    wait(3)
    type(s)
    wait(3)
    type("\n")
    ActionMethod("1380294123754-1.png")
    return 

# reset
# reset this account in typing regCode screen.
# param leftOfOCR: the left picture of OCR
# param leftOfOCR: The right picture of OCR
# return: null
def reset(leftOfOCR, rightOfOCR):   
    tread = Settings.OcrTextRead
    Settings.OcrTextRead = True
    s = OCR(leftOfOCR, rightOfOCR) 
    fillRegCode(s)
    resetFailCondition()
    return

# onlyascii
# trim the string to exclude any non-ASCII char.
# param char: Any string you want to process
# return: A string excluding non-ASCII char
def onlyascii(char):
    if ord(char) < 48 or ord(char) > 127: return ''
    else: return char

# resetFailCondition
# In the failure condition of reseting account, you should invoke this method to try again.
# return: null
def resetFailCondition():
    if exists("1380298064898.png",10) == None:
        returnTopMenu()
        gotoReset()
    return

# returnTopMenu
# disable all window until the main screen is visible
# param char: Any string you want to process
# return: A string excluding non-ASCII char
def returnTopMenu():
    while exists("1380302243814.png") == None:   
        if clickXToBack(SCREEN):
            wait(3)
            continue
        else:
            break
    wait(1)
    return

# clickXToBack
# click the X button. If the number of X button is bigger then 1, this methomd would click the x-button whose x position is the minimum of them.
# param appRegion: searching region
# return: null
def clickXToBack(appRegion):
    while True:
        rValue = False
        x1 = []
        x2 = []
        allArray = []
        targetRegion =  rightUpRegion()
        if targetRegion.exists("1380553164626.png"):
            x1 = targetRegion.findAll("1380553164626.png")
            allArray += x1
        if targetRegion.exists("1380341000249.png"):
            x2 = targetRegion.findAll("1380341000249.png")
            allArray += x2
        if not allArray:
            return rValue
        rValue = True
        newList = sorted(allArray, key=lambda obj: obj.getX())
        total = len(list(newList))
        targetRegion.click(newList[0])
        targetRegion.wait(3)
    return rValue

def mappingAClassPeople(s):
    r = "None"

    if s=="LiHuan":
        r = Pattern("1380295688803.png").similar(0.95)
    elif s=="WanChunGeo":
        r = Pattern("1380295744094.png").similar(0.95)        
    elif s=="IKouChen":
        r = Pattern("1380295886966.png").similar(0.95)
    elif s=="TonLau":
        r=Pattern("1380295952501.png").similar(0.95)
    elif s=="IanKou":
        r=Pattern("1380296000327.png").similar(0.95)
    elif s=="WuIChi":
        r=Pattern("1380296025439.png").similar(0.95)
    elif s=="ShiFunBuBai":
        r=Pattern("1380296113406.png").similar(0.95)
    elif s=="LuCuLian":
        r=Pattern("1380296376446.png").similar(0.95)
    elif s=="LinHuChun":
        r=Pattern("1380296428781.png").similar(0.95)
    elif s=="MoonPrincess":
        r=Pattern("1380555446088.png").similar(0.95)
    else:
        pass

    return r

def mappingBClassPeople(s):
    r="None"
    if s == "InWan":
        r = Pattern("1380812256013.png").similar(0.95)
    elif  s == "GenYeoShen":
        r = Pattern("1380812634032.png").similar(0.95)
    elif s == "GenYeoShen": 
        r = Pattern("1380812733459.png").similar(0.95)
    elif s == "FanYao": 
        r = Pattern("1380812785030.png").similar(0.95)
    else:
        pass
    return r

# LoginGame
# 1.open BlueStacks
# 2.get focus
# 3.click the game's icon for entering game
# return: return the app's region
def loginGame():
    myApp = openApp("BlueStacks")
    wait(3)
    myApp.focus()
    wait(3)
    AppRegion = Region(myApp.focusedWindow())
    AppRegion.setAutoWaitTimeout(10) 
    if exists("1379952280943.png"):
        click("1379952290815.png")
        wait("1379952311495-1.png", 180)
        click("1379952319422.png")
        wait(1)

    return Region(myApp.focusedWindow())

# unlockProtection
# Maybe the protection mission is locked, you should unlock it.
def unlockProtection():
    if exists("1379865937421-1.png"):
        click("1379865950512.png")
        wait(3)
    return

# protection
# protect the TonLau, you should call this method after invoking enterAdventure()
def protection():
    if exists("1379784828302.png", 30):
        click("1379784828302.png")
        wait(2)
        unlockProtection()
        if exists("1379784985998.png"):
            wait(1)
        else:
            if exists("1381243077632.png"):
                click("1381243077632.png")
            elif exists("1379785496704.png"):
                click("1379785496704.png")
            else:
                pass
        wait(60)
    

def enterAdventureMenu():
    if exists("1382398755443.png"):
        click("1382398755443.png")
        wait(1)
    return

def checkPeopleExist(names, classLevel):
    if classLevel == 1:
        for name in enumerate(names):
            pattern = mappingAClassPeople(name)
            if exists(pattern, 1):
                return name
    elif classLevel == 2:
        for name in enumerate(names):
            pattern = mappingBClassPeople(name)
            if exists(pattern, 1):
                return name
    return "None"

# pickStudent
# 挑弟子. 請確定在主畫面才呼叫此method
# param pickupType: 0 代表萬裡選一, 1代表百里選中
# param names: 型態是list, 把你想要抽中的名字放list裡
# return list[lv, name]: 表示抽中的結果, lv 代表是抽中等級, 1是甲級, 2是乙級, 3是丙丁級
#                                      name是代表抽中的結果, 若名字為None, 表示不在程式清單之中
def pickStudent(pickupType, names):
    ActionMethod("1380720199487.png")
    if pickupType == 0:
        ActionMedthod(Pattern("1380710775636-1.png").similar(0.95))
    elif pickupType == 1:
        ActionMedthod(Pattern("1380720222877.png").similar(0.95))

    lv = "0"
    name = "None"
    if exists("1380299636431-1.png", 30):
        click("1380299636431-1.png")
        wait(3)
        if exists(Pattern("1380721537747.png").similar(0.95)):
            name = checkPeopleExist(names, 1)  
            lv = "1"
        elif exists(Pattern("1380721548302.png").similar(0.95)):
            name = checkPeopleExist(names, 2)
            lv = "2"          
        else: #TODO: you have to implement C, D class level here
            lv = "3"            
    returnTopMenu()
    ret = [lv, name]
    return ret


def closeSuprise():
     while exists("1380553164626.png", 2):
        click("1380553164626.png")
        wait(1)

def skipBattle():
    print("skipBattle...")
    if exists("1380782430341.png", 20):
        click("1380782430341.png")
        if exists("1380782771931.png", 20):
            click("1380782771931.png")
            
def relogin():
    if exists("1381338723630.png"):      
        wait(1500)
        ActionMethod("1381338749717.png")
        ActionMethod("1379952311495-1.png")
    return

def upToLv5AndGetGold():
    click("1380724384033-3.png")
    waitAndClick("1380740029234.png", 10)
    wait(1)
    lv = 2
    # loop to lv 5
    while 1:        
        click("1380740063563.png")
        skipBattle()
        waitAndClick("1380695830359-2.png", 30)  
        wait(1)
        if exists("1380740401525.png"):
            lv += 1     
            closeSuprise()
            if exists("1380745900232.png"):
                click("1380745900232.png")
            
        print("lv: %s" % lv)    
        
        closeSuprise()
        
        if lv == 5:
            break
    
    returnTopMenu()
    # get Gold
    waitAndClick("1380741089704.png", 10)
    waitAndClick("1380741161878.png", 10)
    waitAndClick("1380741198664.png", 3)
    waitAndClick("1380741260901.png", 5)
    click("1380741221220.png")
    returnTopMenu()
    waitAndClick("1380741338550.png", 5)
    waitAndClick("1380741380684.png", 5)
    waitAndClick("1380741413769.png", 5)
    returnTopMenu()


def protectChildElder(times):
    # loop
    for i in range(times):
        enterAdventureMenu()
        protection()   
        returnTopMenu()

def tunLauNextStep():
    returnValue = True
    relogin()
    if exists("1379785615163-1.png"):
        click("1379785615163-1.png")
    elif exists("1379785915692-1.png"):
        click("1379785915692-1.png")
    elif exists("1379785955990-1.png"):
        click("1379785955990-1.png")
    elif exists("1379810380156-1.png"):
        click("1379810380156-1.png")
    elif exists("1379784900486-1.png"):
        click("1379784900486-1.png")
    elif exists("1379960592944-1.png"):
        click("1379960611444-1.png")
    else:
        returnValue = False
    wait(2)
    return returnValue

#Please run this script at main menu
#strategy:
# 0: minumus. Choosing this strategy for saving the amount of stars.
# 1: consuming the stars for walking the travel as farest as possible. I mean, to add HP, power and speed by the algorithm in this strategy.

def attackPagan(bloodLevel, powerLevel, fightLevel, strategy):
    ActionMethod("1382972092381.png")
    wait(1)
    #maybe you should drag the scroll bar before clicking this button.
    #not sure if there is a todo item here.
    ActionMethod("1382972134747.png")
    wait(1)
    
           
    if not ActionMethod("1382972416613.png"):
        ActionMethod("1383229332592.png")
        
    count = 0
    while True:
        #choosing the buf
        wait(1)
        if exists("1383152590100.png", 3):
            click("1383152602260.png")
        wait(1)
            
        if exists("1383229635258.png", 3):
            chooseBuffer(strategy)
        wait(3)
        if count < bloodLevel:
            click("1383147528544.png")
            print "attack blood %d level" % (count)
        elif count < powerLevel:
            click("1383147591861.png")
            print "attack power %d level" % (count)
        else:
            click("1383147608270.png")
            print "attack normal %d level" % (count)
        wait(1)
        if exists("1383147754936.png", 300):
            if exists("1383148524918.png"): #win
                ActionMethod("1383148543550.png")
                count = count + 1
                continue
            elif exists("1383155317544.png"): #lose
                print "lose in %d level" % (count)
                break;            
    returnTopMenu()

    #return the level you are lost.
    #You may adjust your policy to next attacking pagans.
    return count

#choose buffer in attacking pagans.
#0: always choose the minimuns
#1: choose 
def chooseBuffer(strategy):
    if strategy == 0:
        if exists("1383147100622.png"):
            
            star30 = find("1383147100622.png")
            star30Above = star30.above()
            star15 = find("1383147158032.png")
            star15Above = star15.above()
    
            if star30Above.exists("1383147323931.png") or star30Above.exists("1383152924777.png"):
                ActionMethod("1383149127633.png")
            elif star15Above.exists("1383147323931.png") or star15Above.exists("1383152924777.png"):
                ActionMethod("1383149194205.png")
            else:
                ActionMethod("1383152966293.png") 
    else:
        ActionMethod("1383152966293.png")
    wait(1)
    return

def allProtectAction():
    while True:
        loginGame()
        r = True
        while r:
            relogin()
            r=tunLauNextStep()
        enterAdventureMenu()
    #eatChiken()
        unlockProtection()  
        protection()    
    return

def testFun():
    print "running testFun"
    return

