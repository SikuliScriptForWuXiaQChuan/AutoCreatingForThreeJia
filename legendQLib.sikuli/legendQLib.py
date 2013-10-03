from sikuli import * 
# ActionMethodWithRegion
# param region: In this given region, find and click the pattern in 30 sec.
# param pattern: The target you want to click, which could be a string, pic or something else.
# return: null
def ActionMethodWithRegion(region, pattern):
    region.wait(pattern, 30)
    region.click(pattern)
    return

# ActionMethod
# If myRegion exists, invoke ActionMethodWithRegion(myRegion, pattern)
# param pattern: The target you want to click, which could be a string, pic or something else.
# return: null
def ActionMethod(pattern):
    ActionMethodWithRegion(myRegion, pattern)
    return

# Log
# For any textEditor you assign, type the log into.
# param s: 
# return: null
def Log(s):
    if myText:
        wait(1)
        myText.focus()
        wait(1)
        type(s)
        wait(1)
        myApp.focus()
        wait(1)
    return

# check region image is exists and click
def checkClick(obj):
    if exists(obj):
        click(obj)

# wait region image and click
def waitAndClick(obj, sec):
    wait(obj, sec)
    click(obj)

# create game for first B studenet
def createGame(firstStudent):
    print('create game...')
    checkClick("1380695415869-1.png")
    
    print('select first student...')
    wait("1380695482077-1.png", 30)
    checkClick(firstStudent)
    checkClick("1380695515823-1.png")

# run tutorial and expect Ace student
def runTutorial(firstAce):
    wait("1380695640309-3.png", 10)
    click("1380724384033.png")
    click("1380695762060-3.png")
    wait("1380695815218-3.png", 30)
    click("1380695830359-3.png")
    click("1380695864981-3.png")
    wait(2)

    stud = pickStudent(0, firstAce)
    print("stud: %s" % stud)
    b = 0
    if stud >= 4:
        b = 1
    click("1380696105210-3.png")
    click("1380696128810-3.png")
    click("1380696149010-3.png")
    click("1380695864981-3.png")
    click("1380724384033-1.png")
    click("1380695762060-3.png")
    wait("1380696450966-3.png", 20)
    click("1380695830359-3.png")
    click("1380696510493-3.png")
    click("1380695864981-3.png")    
    waitAndClick("1380696677065-3.png", 10)
    click("1380696735878-3.png")
    click("1380696829107-3.png")
    click("1380696853984-3.png")
    click("1380695864981-3.png")
    click("1380696903585-3.png")
    click("1380696921992-3.png")
    wait(2)
    wait("1380696939217-3.png")
    click("1380696939217-3.png")
    wait(2)
    click("1380695864981-3.png")
    click("1380724384033-2.png")
    click("1380697007266-3.png")
    wait("1380695830359-3.png", 30)
    click("1380695830359-3.png")
    # level up
    print("level up...")
    wait("1380702038600-1.png", 5)
    click("1380702038600-1.png")

    print("check drop item...")
    if exists("1380695515823-3.png"):
        click("1380695515823-3.png")
    print("close")   
    if exists("1380696510493-2.png"):
        click("1380696510493-2.png")
    closeSuprise()
    click("1380695864981-3.png")
    return b

# gotoreset
# reset the account. Note, you have to invoke returnTopMenu before this method, for be suring that we could go from setting options.
# return: null
def gotoreset():
    ActionMethod("1380297823894.png")
    ActionMethod("1380297843385.png")
    myRegion.wait(3)
    reset("1380292721591.png", "1380292736191.png")
    myRegion.wait(3)
    resetFailCondition()
    return

# leftRegion
# The left screen of myRegion. To decrease the searching area for finding patterns.
# return: null
def leftRegion():
    return Region(myRegion.getX(), myRegion.getY(), myRegion.getW() / 2, myRegion.getH())

# rightUpRegion
# one-fouth of myRegion in RightUp side. For decreasing the searching area.
# return: null
def rightUpRegion():
    return Region(myRegion.getX() + (myRegion.getW() / 2), myRegion.getY(), myRegion.getW() / 2, myRegion.getH()/2)    

#OCR method
#param leftOfOCR: the picture which is left from OCR.
#param rightOfOCR: the picture which is right from OCR
#return: the OCR string in ASCII
def OCR(leftOfOCR, rightOfOCR):
    regLeft = myRegion.find(leftOfOCR)
    regRight = myRegion.find(rightOfOCR)
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
    myRegion.click("1380293789145-1.png")
    myRegion.wait(3)
    myRegion.type(s)
    myRegion.wait(3)
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
    if myRegion.exists("1380298064898.png",10) == None:
        returnTopMenu()
        gotoReset()
    return

# returnTopMenu
# disable all window until the main screen is visible
# param char: Any string you want to process
# return: A string excluding non-ASCII char
def returnTopMenu():
    while myRegion.exists("1380302243814.png") == None:
           
        if clickXToBack(myRegion):
            myRegion.wait(3)
            continue
        else:
            break
    myRegion.wait(1)
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

# pick student
# param flag: student type | 0 Ace, 1 B, 2 C,D
# param obj: expect role
# return: expect result bitmask: 0-note expected, 4-expected ; student type bitmask 0-A, 1-B, 2-C, 3-D 
def pickStudent(flag, obj):
    click("1380720199487.png")
    if flag == 0:
        wait("1380710775636-1.png", 10)
        click("1380710775636-1.png")
    elif flag == 1:
        wait("1380720222877.png", 10)
        click("1380720222877.png")
    #else:
        
    wait(3);

    lv = 0
    if exists("1380721537747.png"):
        lv = 0
    elif exists("1380721548302.png"):
        lv = 1
    else:
        lv = 2 

    foundObj = 0
    if obj != 0 and exists(obj):
        foundObj = 4
    ret = lv + foundObj    
    print("pick ret: %s " % ret) 
    wait("1380695974966-3.png", 20)
    click("1380695974966-3.png")
    returnTopMenu()
    return ret

# back to top menu
def skipBattle():
    print("skipBattle not implement yet...")


def upToLv5AndGetGold():
    click("1380724384033-3.png")
    waitAndClick("1380740029234.png", 10)
    wait(1)
    lv = 4
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
