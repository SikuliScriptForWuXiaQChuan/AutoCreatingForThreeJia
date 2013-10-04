
import legendQLib



def gotorest():
    click("1380697566803.png")
    click("1380697586833.png")
    click("1380697620865.png")
    # 文字辨試輸入

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
    type("\r")
    

"""
    if exists("1380293204363.png",3):
        click("1380293204363.png")
        wait("1380294123754.png")
        click("1380294123754.png")
    else:
        returnTopMenu()
        gotorest()
"""


def onlyascii(char):
    if ord(char) < 48 or ord(char) > 127: return ''
    else: return char

 
def main():
    while 1:
        print("call lib create game...")
        #legendQLib.createGame("1380695538575.png")
        b =  legendQLib.runTutorial(0)
        if b == 0 :
            gotorest()
          

main()
