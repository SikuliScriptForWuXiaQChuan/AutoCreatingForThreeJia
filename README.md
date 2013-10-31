AutoCreatingForThreeJia
=======================
##前言
這是武俠Q傳的自動化framework. 目前可以做到很多功能, 但我們只提供tool, 你需要自己依這些tool打造功能. 這個framework目前重要的功能計有:

1. 保護童姥
2. 打魔教
3. 自動開局, 升級, 抽三甲; 抽完三甲後, 判斷所有弟子是不是你要的(把弟子名稱當參數丟進程式, 包含強乙弟子), 若不是就重置再開局一次.
4. 其他...(懶得想了)

目前作者有在使用的是1, 2兩項, 通常是半夜睡覺時在跑的. 至於第3個功能, 一個晚上大概能跑個5x次, 但能抽到作者心中理想弟子開局的機率, 實在太低;還不如跑童姥賺點銀倆實在.

##Requirement
1. You are playing 武俠Q傳 on BlueStack in your PC/Mac
2. Sikuli IDE(http://www.sikuli.org/)
3. 熟悉python語法

##Installation
1. clone this repository on your PC/Mac
2. `Import legendQLib` in your Sikuli programs
3. Read the API and write your own automation script.

##Sample Code
###打魔教
```
attackPagan(3, 8, 999999, 0)
```
參數意義:</br>
從主畫面出發, 血戰打3關, 力戰打8關, 奮戰999999(等於無窮盡打下去), buff策略為0
buff 策略目前僅提供兩策略:</br>

* 0: 分別於30%以及15%找氣血, 武力. 有的話就加, 要不然就加3%</br>
* 1: 永遠選擇3%</br>

###保護童姥
```
enterAdventureMenu()
unlockProtection()  
protection()
```
意義分別說明如下:

1. 進入奇遇
2. 選擇保護童姥(並解鎖)
3. 驅趕小賊

以上範例只能保護一次, 如需要無窮盡保護下去, 可以使用下面這個範例:

```
while True:
    r = True
    while r:
        relogin()
        r=tunLauNextStep()
    enterAdventureMenu()
    unlockProtection()  
    protection()  
```
