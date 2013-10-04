
import legendQLib

from sikuli import * 

def checkClick(obj):
    if exists(obj):
        click(obj)

def waitAndClick(obj, sec):
    wait(obj, sec)
    click(obj)

def createGame(firstStudent):
    print('create game...')
    checkClick("1380695415869.png")
    
    print('select first student...')
    wait("1380695482077.png", 30)
    checkClick(firstStudent)
    checkClick("1380695515823.png")


def runTutorial(firstAce):
    wait("1380695640309-2.png", 10)
    click("1380724384033.png")
    click("1380695762060-2.png")
    wait("1380695815218-2.png", 30)
    click("1380695830359-2.png")
    click("1380695864981-2.png")
    wait(2)

    stud = pickStudent(0, firstAce)
    print("stud: %s" % stud)
    b = 0
    if stud >= 4:
        b = 1
    click("1380696105210-2.png")
    click("1380696128810-2.png")
    click("1380696149010-2.png")
    click("1380695864981-2.png")
    click("1380724384033-1.png")
    click("1380695762060-2.png")
    wait("1380696450966-2.png", 20)
    click("1380695830359-2.png")
    click("1380696510493-2.png")
    wait(1)
    click("1380695864981-2.png")    
    waitAndClick("1380696677065-2.png", 10)
    click("1380696735878-2.png")
    click("1380696829107-2.png")
    click("1380696853984-2.png")
    click("1380695864981-2.png")
    click("1380696903585-2.png")
    click("1380696921992-2.png")
    wait(2)
    wait("1380696939217-2.png")
    click("1380696939217-2.png")
    wait(2)
    click("1380695864981-2.png")
    click("1380724384033-2.png")
    click("1380697007266-2.png")
    wait("1380695830359-2.png", 30)
    click("1380695830359-2.png")
    # level up
    print("level up...")
    wait("1380702038600.png", 5)
    click("1380702038600.png")

    print("check drop item...")
    if exists("1380695515823-3.png"):
        click("1380695515823-3.png")
    print("close")   
    if exists("1380696510493-2.png"):
        click("1380696510493-2.png")

    closeSuprise()
            
    click("1380695864981-2.png")
    return b


def gotoreset():
    click("1380697566803.png")
    wait(2)
    click("1380697586833.png")
    reset(0, 0)
    #click("1380697620865.png")
    #

def leftRegion():
    return Region(myRegion.getX(), myRegion.getY(), myRegion.getW() / 2, myRegion.getH())

def rightUpRegion():
    return Region(myRegion.getX() + (myRegion.getW() / 2), myRegion.getY(), myRegion.getW() / 2, myRegion.getH()/2)    

def reset(a, b):   
    tread = Settings.OcrTextRead
    Settings.OcrTextRead = True
    
    regLeft = find("1380292721591.png")
    regRight = find("1380292736191.png")
    newX = regLeft.getX() + regLeft.getW()
    textReg = Region(newX, regLeft.getY(), regRight.getX() - newX, regLeft.getH())
    print("%s, %s, %s, %s " % (textReg.getX(), textReg.getY(), textReg.getW(), textReg.getH()) )
    s = textReg.text()
    print('origin s:%s' % (s))
    s1 = s.replace(".","")
    s2 = s1.replace(" ","")
    s3 = filter(onlyascii, s2)
    print('s:%s, s1:%s, s2:%s, s3:%s' % (s, s1, s2, s3))
    click("1380293789145.png")
    wait(3)
    type(s3)
    wait(3)
    type("\r")

    Settings.OcrTextRead = tread
    
    wait("1380294123754.png")
    click("1380294123754.png")

    wait(5)
    if exists("1380294123754.png"):
        returnTopMenu()
        gotoreset()


def onlyascii(char):
    if ord(char) < 48 or ord(char) > 127: return ''
    else: return char

def pickStudent(flag, obj):
    click("1380720199487.png")
    if flag == 0:
        wait(Pattern("1380745557536.png").similar(0.95), 10)
        click(Pattern("1380745557536.png").similar(0.95))
    elif flag == 1:
        wait(Pattern("1380745523721.png").similar(0.95), 10)
        click(Pattern("1380745523721.png").similar(0.95))
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
    wait("1380695974966-2.png", 20)
    click("1380695974966-2.png")
    returnTopMenu()
    return ret

def pickFromTenThoundard(obj):
    click("1380720199487.png")
    print("Ace student")
    wait("1380710775636.png", 10)
    click("1380710775636.png")
    wait(5)
    # check first ace student
    if exists(firstAce):
        b = 1
    else: 
        b = 0
        
    wait("1380695974966-2.png", 20)
    click("1380695974966-2.png")

def returnTopMenu():
    while exists("1380725442905.png"):
        click("1380725442905.png")
        wait(1)
    if exists("1380695864981-2.png"):
        click("1380695864981-2.png")
        wait(1)
        returnTopMenu()

def closeSuprise():
     wait(1)
     while exists("1380743092036.png", 2):
        click("1380743092036.png")
        wait(1)


def skipBattle():
    print("skipBattle not implement yet...")
        
        
def upToLv5AndGetGold():
    click("1380724384033-2.png")
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
    
    
 
def main():
    openApp("BlueStacks")
    while 1:
        print("call lib create game...")
        #legendQLib.createGame("1380695538575.png")
        legendQLib.createGame("1380782192220.png")
        b =  runTutorial("1380724013725.png")
        if b == 0 :
            gotoreset()
        else:
            stud = pickStudent(1, 0)
            print("stud: %s" % stud )

            upToLv5AndGetGold()
            stud = pickStudent(0, 0)
            print("stud: %s" % stud )

            if stud < 4:
                gotoreset()
            else:                           
                break

def test():
    openApp("BlueStacks")
    #pickStudent(1, 0)
    #upToLv5AndGetGold()
    legendQLib.gotoreset()

#main()
test()