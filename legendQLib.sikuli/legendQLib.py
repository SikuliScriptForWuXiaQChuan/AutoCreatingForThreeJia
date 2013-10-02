from sikuli import * 

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
    if exists("1380695515823-4.png"):
        click("1380695515823-4.png")
    print("close")   
    if exists("1380696510493-3.png"):
        click("1380696510493-3.png")
            
    click("1380695864981-3.png")
    return b

# go to reset account
def gotoreset():
    click("1380697566803.png")
    wait(2)
    click("1380697586833.png")
    reset(0, 0)
    #click("1380697620865.png")
    # 文字辨試輸入

def leftRegion():
    return Region(myRegion.getX(), myRegion.getY(), myRegion.getW() / 2, myRegion.getH())

def rightUpRegion():
    return Region(myRegion.getX() + (myRegion.getW() / 2), myRegion.getY(), myRegion.getW() / 2, myRegion.getH()/2)    

# reset account
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
def returnTopMenu():
    while exists("1380725442905.png"):
        click("1380725442905.png")
        wait(1)
    if exists("1380695864981-3.png"):
        click("1380695864981-3.png")
        wait(1)
        returnTopMenu()
        