def reset(a, b):
    regLeft = find("1380292721591.png")
    regRight = find("1380292736191.png")
    newX = regLeft.getX() + regLeft.getW()
    textReg = Region(newX, regLeft.getY(), regRight.getX() - newX, regLeft.getH())
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
    if exists("1380293204363.png",3):
        click("1380293204363.png")
        wait("1380294123754.png")
        click("1380294123754.png")
    else:
        returnTopMenu()
        gotorest()
    
def onlyascii(char):
    if ord(char) < 48 or ord(char) > 127: return ''
    else: return char

def failCondition():
    if exists("1380298064898.png",3) == None:
        returnTopMenu()
        gotoRest()

def judgePeople():
    if exists("1380295688803.png"):
        s="LiHuan"
        print('checking %s' % (s))
        return s
    elif exists("1380295744094.png"):
        s="WanChunGeo"
        print('checking %s' % (s))
        return s
    elif exists("1380295814271.png"):
        s="GenGeoChin"
        print('checking %s' % (s))
        return s
    elif exists("1380295886966.png"):
        s="IKouChen"
        print('checking %s' % (s))
        return s
    elif exists("1380295952501.png"):
        s="TonLau"
        print('checking %s' % (s))
        return s
    elif exists("1380296000327.png"):
        s="IanKou"
        print('checking %s' % (s))
        return s
    elif exists("1380296025439.png"):
        s="WuIChi"
        print('checking %s' % (s))
        return s
    elif exists("1380296113406.png"):
        s="ShiFunBuBai"
        print('checking %s' % (s))
        return s
    elif exists("1380296376446.png"):
        s="LuCuLian"
        print('checking %s' % (s))
        return s
    elif exists("1380296428781.png"):
        s="LinHuChun"
        print('checking %s' % (s))
        return s
    else:
        s="NoMan"
        print('Not a man I want!')
        return s

def gotoRest():
    click("1380297823894.png")
    wait(1)
    click("1380297843385.png")
    wait(3)
    reset(f_left, f_right)
    failCondition()

def returnTopMenu():
    while exists("1380302243814.png") == None:
        print('back to upper menu')
        if exists("1380340686533.png") == None:            
            if clickXToBack():
                wait(3)
                continue
        if exists("1380298499215.png"):
            click("1380298499215.png")
            continue
        elif exists("1380299511425.png"):
            click("1380299511425.png")
            continue
        elif exists("1380298994787.png"):
            click("1380298994787.png")
            continue
        elif exists("1380301410695.png"):
            click("1380301410695.png")
            continue
        elif exists("1380301164310.png"):
            click("1380301201924.png")
            continue
    return

def clickXToBack():
    rValue = False
    while exists("1380341000249.png",5):
        rValue = True
        initList = findAll("1380341000249.png")
        newList = sorted(initList, key=lambda obj: obj.getY(), reverse=True)
        total = len(list(newList))
        print('# of X2: %i' % (total))
        click(newList[0])
        wait(1)
            
    return rValue

def fight():
    click("1380298355974.png")
    wait("1380298396543.png",60)
    return

def ChanAinFight():
    wait("1380298304591.png")
    click("1380298304591.png")
    fight()
    return
def firstStudent():
    click("1380298626344.png")
    wait("1380300452850.png")
    regFirst=find("1380300452850.png")
    
    click(regFirst.find("1380298650993.png"))
    if exists("1380301410695.png"):
        click("1380301410695.png")
    if exists("1380305068556.png"):
        click("1380305068556.png")
    wait(3)
    return

def buildFormat():
    click("1380298820327.png")
    wait("1380298835059.png")
    click("1380298835059.png")
    wait("1380298867375.png")
    click("1380298867375.png")
    returnTopMenu() 
    return
def equip():
    click("1380299051344.png")
    wait("1380299108748.png")
    click("1380299108748.png")
    wait("1380299129006.png")
    click("1380299129006.png")
    wait("1380299152850.png")
    click("1380299152850.png")
    returnTopMenu()
    return

def package():
    wait("1380300948729.png")
    click("1380300948729.png")
    
    wait("1380299226850.png")
    click("1380299226850.png")
    wait("1380299243852.png")
    click("1380299243852.png")
    returnTopMenu()
    return

def pickup100People():
    click("1380299590104.png")
    wait("1380299604350.png")
    click("1380299604350.png")
    wait("1380299636431.png")
    click("1380299636431.png")
    wait(3)
    if exists("1380382370695.png"):
        s = judgePeople()
    else:
        s = "NoMan"
    return s

f_left = "1380292721591.png"
f_right = "1380292736191.png"

s_left = "1380293437259.png"
s_right = "1380293992157.png"
setAutoWaitTimeout(10)
openApp("BlueStacks")
wait(3)
################################################enter Game
def runChoose():
    while 1:
        click("1380298064898.png")
        wait("1380298227453.png",20)
        click("1380298227453.png")
        wait(3)
        click("1380298278558.png")
        ChanAinFight()
        wait("1380337327356.png")
        click("1380337327356.png")
        returnTopMenu()
        firstStudent()
        buildFormat()
        ChanAinFight()
        wait("1380337327356.png")
        click("1380337327356.png")
        wait("1380340309707.png")
        click("1380340309707.png")
        returnTopMenu()
        equip()
        package()
        ChanAinFight()
        returnTopMenu()
        s=pickup100People()
        if s=="NoMan":
            clickXToBack()
            gotoRest()
        else:
            popup("find people:%s" % (s))
runChoose()
