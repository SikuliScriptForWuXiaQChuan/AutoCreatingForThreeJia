def leftRegion():
    return Region(myRegion.getX(), myRegion.getY(), myRegion.getW() / 2, myRegion.getH())

def rightUpRegion():
    return Region(myRegion.getX() + (myRegion.getW() / 2), myRegion.getY(), myRegion.getW() / 2, myRegion.getH()/2)

def ActionMethodWithRegion(region, pattern):
    region.wait(pattern, 30)
    region.click(pattern)
    return

def Log(s):
    wait(1)
    myText.focus()
    wait(1)
    type(s)
    wait(1)
    myApp.focus()
    wait(1)
    return
def ActionMethod(pattern):
    ActionMethodWithRegion(myRegion, pattern)
    return

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
    print('s:%s, s1:%s, s2:%s, s3:%s' % (s, s1, s2, s3))

    return s3

def reset(leftOfOCR, rightOfOCR):
    s = OCR(leftOfOCR, rightOfOCR) 
    fillRegCode(s)
    failCondition()

def fillRegCode(s):
    myRegion.click("1380293789145.png")
    myRegion.wait(3)
    myRegion.type(s)
    myRegion.wait(3)
    type("\n")
    ActionMethod("1380294123754.png")
    return 

def judgementDetailRegCode(event):
    print "judgementDetail"
    
    s = OCR("1380732254499.png","1380732611879.png")
    fillRegCode(s)
    event.region.stopObserver()
    myRegion.wait(3)
    return

def onlyascii(char):
    if ord(char) < 48 or ord(char) > 127: return ''
    else: return char

def failCondition():
    if myRegion.exists("1380298064898.png",10) == None:
        returnTopMenu()
        gotoReset()

def judgePeople():
    myLeftRegion = leftRegion()
    if myLeftRegion.exists(Pattern("1380295688803.png").similar(0.95)):
        s="LiHuan"
        print('checking %s' % (s))
        return s
    elif myLeftRegion.exists(Pattern("1380295744094.png").similar(0.95)):
        s="WanChunGeo"
        print('checking %s' % (s))
        return s
    elif myLeftRegion.exists(Pattern("1380295814271.png").similar(0.95)):
        s="GenGeoChin"
        print('checking %s' % (s))
        return s
    elif myLeftRegion.exists(Pattern("1380295886966.png").similar(0.95)):
        s="IKouChen"
        print('checking %s' % (s))
        return s
    elif myLeftRegion.exists(Pattern("1380295952501.png").similar(0.95)):
        s="TonLau"
        print('checking %s' % (s))
        return s
    elif myLeftRegion.exists(Pattern("1380296000327.png").similar(0.95)):
        s="IanKou"
        print('checking %s' % (s))
        return s
    elif myLeftRegion.exists(Pattern("1380296025439.png").similar(0.95)):
        s="WuIChi"
        print('checking %s' % (s))
        return s
    elif myLeftRegion.exists(Pattern("1380296113406.png").similar(0.95)):
        s="ShiFunBuBai"
        print('checking %s' % (s))
        return s
    elif myLeftRegion.exists(Pattern("1380296376446.png").similar(0.95)):
        s="LuCuLian"
        print('checking %s' % (s))
        return s
    elif myLeftRegion.exists(Pattern("1380296428781.png").similar(0.95)):
        s="LinHuChun"
        print('checking %s' % (s))
        return s
    elif myLeftRegion.exists(Pattern("1380555446088.png").similar(0.95)):
        s="MoonPrincess"
        print('checking %s' % (s))
        return s
    else:
        s="NoMan"
        print('Not a man I want!')
        return s

def gotoReset():
    ActionMethod("1380297823894.png")
    ActionMethod("1380297843385.png")
    myRegion.wait(3)
    reset("1380292721591.png", "1380292736191.png")
    myRegion.wait(3)
    failCondition()

def returnTopMenu():
    while myRegion.exists("1380302243814.png") == None:
           
        if clickXToBack(myRegion):
            myRegion.wait(3)
            continue
        else:
            break
    myRegion.wait(1)
    return

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

def fight():
    if myRegion.exists("1380298355974.png", 10):
        
        myRegion.click("1380298355974.png")
        myRegion.wait("1380298396543.png",60)
    return

def ChanAinFight():
    ActionMethod(Pattern("1380562324428.png").similar(0.50))
    fight()
    return
def firstStudent():
    ActionMethod("1380298626344.png")
    myRegion.wait("1380300452850.png", 30)
    regFirst=myRegion.find("1380300452850.png")
    
    click(regFirst.find("1380298650993.png"))
    if myRegion.exists("1380301410695.png", 10):
        myRegion.click("1380301410695.png")
    if myRegion.exists("1380305068556.png", 30):
        myRegion.click("1380305068556.png")
    wait(3)
    return

def buildFormat():
    ActionMethod("1380298820327.png")
    ActionMethod("1380298835059.png")
    ActionMethod("1380298867375.png")
    returnTopMenu() 
    return
def equip():
    ActionMethod("1380299051344.png")
    ActionMethod("1380299108748.png")
    ActionMethod("1380299129006.png")
    ActionMethod("1380299152850.png")
    returnTopMenu()
    return

def package():
    ActionMethod("1380300948729.png")
    ActionMethod("1380299226850.png")
    ActionMethod("1380299243852.png")
    returnTopMenu()
    return

def pickup100People():
    ActionMethod("1380299590104.png")
    ActionMethod("1380299604350.png")
    if myRegion.exists("1380299636431.png", 30):
        myRegion.click("1380299636431.png")
        myRegion.wait(3)
        if myRegion.exists(Pattern("1380382370695.png").similar(0.95)):
            s = judgePeople()
        else:
            s = "NoMan"
    else:
        returnTopMenu()
        s = "NoMan"
    return s

def runChoose():
    count = 1
    while 1:
        Log('starting process %i time' % (count))
        ActionMethod("1380298064898.png")
        ActionMethod("1380298227453.png")
        ActionMethod("1380298278558.png")
        ChanAinFight()
        ActionMethod("1380337327356.png")
        returnTopMenu()
        firstStudent()
        buildFormat()
        ChanAinFight()
        ActionMethod("1380337327356.png")
        ActionMethod("1380340309707.png")
        returnTopMenu()
        equip()
        package()
        ChanAinFight()
        ActionMethod("1380337327356.png")
        returnTopMenu()
        s=pickup100People()
        if s=="NoMan":
            Log('pick up people in %i time failure!' % (count))
            count += 1
            clickXToBack(myRegion)
            gotoReset()
        else:
            popup("find people:%s" % (s))
            break

####setting

####choose app
myText = openApp("TextEdit")
myApp = openApp("BlueStacks")
wait(1)
myApp.focus()
wait(3)
myRegion = Region(myApp.focusedWindow())
myRegion.setAutoWaitTimeout(10)
#### run Choosing People
runChoose()
