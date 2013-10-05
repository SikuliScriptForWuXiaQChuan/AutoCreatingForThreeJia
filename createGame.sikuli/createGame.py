
import legendQLib

from sikuli import * 
    
 
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
    #openApp("BlueStacks")
    #pickStudent(1, 0)
    #upToLv5AndGetGold()
    legendQLib.loginGame()
    

#main()
test()