import legendQLib
from sikuli import * 

# 1. 保護童姥
# 2. 吃雞
# 3. 遇到登出, 半小時後再登入

AppRegion = None
myRegion = legendQLib.loginGame()
legendQLib.returnTopMenu()
legendQLib.protectChildElder(99999)