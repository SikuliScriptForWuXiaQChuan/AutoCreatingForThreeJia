def leftRegion():
    return Region(myRegion.getX(), myRegion.getY(), myRegion.getW() / 2, myRegion.getH())

def rightUpRegion():
    return Region(myRegion.getX() + (myRegion.getW() / 2), myRegion.getY(), myRegion.getW() / 2, myRegion.getH()/2)

def reset():
    regLeft = myRegion.find("1380292721591.png")
    regRight = myRegion.find("1380292736191.png")
    newX = regLeft.getX() + regLeft.getW()
    textReg = Region(newX, regLeft.getY(), regRight.getX() - newX, regLeft.getH())
    s = textReg.text()
    print('origin s:%s' % (s))
    s1 = s.replace(".","")
    s2 = s1.replace(" ","")
    s3 = filter(onlyascii, s2)
    print('s:%s, s1:%s, s2:%s, s3:%s' % (s, s1, s2, s3))
    myRegion.click("1380293789145.png")
    myRegion.wait(3)
    myRegion.type(s3)
    myRegion.wait(3)
    if myRegion.exists("1380293204363.png",10):
        myRegion.click("1380293204363.png")
        myRegion.wait("1380294123754.png")
        myRegion.click("1380294123754.png")
    else:
        returnTopMenu()
        gotorest()
    
def onlyascii(char):
    if ord(char) < 48 or ord(char) > 127: return ''
    else: return char

def failCondition():
    if myRegion.exists("1380298064898.png",3) == None:
        returnTopMenu()
        gotoRest()

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

def gotoRest():
    myRegion.click("1380297823894.png")
    myRegion.wait(1)
    myRegion.click("1380297843385.png")
    myRegion.wait(3)
    reset()
    myRegion.wait(3)
    failCondition()

def returnTopMenu():
    while myRegion.exists("1380302243814.png") == None:
        print('back to upper menu')
           
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
            print('1')
        if targetRegion.exists("1380341000249.png"):
            x2 = targetRegion.findAll("1380341000249.png")
            allArray += x2
            print('2')
        if not allArray:
            return rValue
        rValue = True
        newList = sorted(allArray, key=lambda obj: obj.getX())
        print('3')
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
    myRegion.wait(Pattern("1380562324428.png").similar(0.50),30)
    myRegion.click(Pattern("1380562324428.png").similar(0.50))
    fight()
    return
def firstStudent():
    myRegion.wait("1380298626344.png",10)
    myRegion.click("1380298626344.png")
    myRegion.wait("1380300452850.png", 10)
    regFirst=myRegion.find("1380300452850.png")
    
    click(regFirst.find("1380298650993.png"))
    if myRegion.exists("1380301410695.png", 10):
        myRegion.click("1380301410695.png")
    if myRegion.exists("1380305068556.png", 10):
        myRegion.click("1380305068556.png")
    wait(3)
    return

def buildFormat():
    wait("1380298820327.png", 10)
    myRegion.click("1380298820327.png")
    myRegion.wait("1380298835059.png")
    myRegion.click("1380298835059.png")
    myRegion.wait("1380298867375.png")
    myRegion.click("1380298867375.png")
    returnTopMenu() 
    return
def equip():
    myRegion.click("1380299051344.png")
    myRegion.wait("1380299108748.png")
    myRegion.click("1380299108748.png")
    myRegion.wait("1380299129006.png")
    myRegion.click("1380299129006.png")
    myRegion.wait("1380299152850.png")
    myRegion.click("1380299152850.png")
    returnTopMenu()
    return

def package():
    myRegion.wait("1380300948729.png")
    myRegion.click("1380300948729.png")
    
    myRegion.wait("1380299226850.png")
    myRegion.click("1380299226850.png")
    myRegion.wait("1380299243852.png")
    myRegion.click("1380299243852.png")
    returnTopMenu()
    return

def pickup100People():
    myRegion.wait("1380299590104.png", 30)
    myRegion.click("1380299590104.png")
    myRegion.wait("1380299604350.png", 30)
    myRegion.click("1380299604350.png")
    myRegion.wait("1380299636431.png", 30)
    myRegion.click("1380299636431.png")
    myRegion.wait(3)
    if myRegion.exists(Pattern("1380382370695.png").similar(0.95)):
        s = judgePeople()
    else:
        s = "NoMan"
    return s

def runChoose():
    while 1:
        myRegion.wait("1380298064898.png", 10)
        myRegion.click("1380298064898.png")
        
        myRegion.wait("1380298227453.png",20)
        myRegion.click("1380298227453.png")
        myRegion.wait("1380298278558.png", 10)
        myRegion.click("1380298278558.png")
        ChanAinFight()
        myRegion.wait("1380337327356.png", 30)
        myRegion.click("1380337327356.png")
        returnTopMenu()
        firstStudent()
        buildFormat()
        ChanAinFight()
        myRegion.wait("1380337327356.png", 30)
        myRegion.click("1380337327356.png")
        myRegion.wait("1380340309707.png", 10)
        myRegion.click("1380340309707.png")
        returnTopMenu()
        equip()
        package()
        ChanAinFight()
        myRegion.wait("1380337327356.png", 30)

        returnTopMenu()
        s=pickup100People()
        if s=="NoMan":
            clickXToBack(myRegion)
            gotoRest()
        else:
            popup("find people:%s" % (s))
            break

####setting
f_left = "1380292721591.png"
f_right = "1380292736191.png"

s_left = "1380293437259.png"
s_right = "1380293992157.png"

####choose app
myApp = openApp("BlueStacks")
wait(1)
myApp.focus()
wait(3)
myRegion = Region(myApp.focusedWindow())
myRegion.setAutoWaitTimeout(10)

#### run Choosing People
runChoose()
