AutoCreatingForThreeJia
=======================
##前言
![image](https://raw.github.com/SikuliScriptForWuXiaQChuan/AutoCreatingForThreeJia/master/ScreenShot/screenShot.png)<br/>

這是武俠Q傳的自動化framework. 這個framework只提供tool, 想要使用的人必須依這些tool去打造功能. 這個framework目前可以做到的重要功能計有:

1. 保護童姥
2. 打魔教
3. 自動開局, 升級, 抽三甲; 抽完三甲後, 判斷所有弟子是不是你要的(把弟子名稱當參數丟進程式, 包含強乙弟子), 若不是就重置再開局一次.
4. 其他(懶得想了).

目前作者有在使用的是1, 2兩項, 通常是半夜睡覺時在跑的. 至於第3個功能, 一個晚上大概能跑個5x次, 但能抽到作者心中理想弟子開局的機率, 實在太低; 還不如跑童姥賺點銀倆實在. 當然, 你也可以把這些method湊一湊, 寫一個script既可以保護童姥, 又能打魔教, 還能去開局抽三甲. It depends on you! 

##Requirement
1. You play 武俠Q傳(台) recently on BlueStack in your PC/Mac
2. Sikuli IDE(http://www.sikuli.org/)
3. 熟悉python語法

##Why Sikuli?
Sikuli是很方便的自動化程式script, 以圖形比對為基礎, 有下面優點:

1. 跨平台: 由於圖形比對相似度預設為0.75, 可避免掉跨平台不同導致的圖形失真問題. 相似度亦可在程式裡調整
2. python語言, 易學易懂
3. 以圖片觀點寫code, 省去計算一堆複雜position問題
4. 內建OCR功能, 能判斷重置碼

##Installation
1. clone this repository on your PC/Mac
2. 下載sikuli IDE from http://www.sikuli.org/
3. 新建一個新的sikuli檔案, 需與repository裡的legendQLib.sikuli 同一個目錄
4. 於你的sikuli 腳本裡import 本library, `import legendQLib`
5. 測試是否可以使用, 先來個簡單的腳本, 如下圖
   ![image](https://raw.github.com/SikuliScriptForWuXiaQChuan/AutoCreatingForThreeJia/master/ScreenShot/test.png)<br/>
   如果可以看到訊息欄有出現 `running testFun`, 就代表lib 有import成功
6. Read All APIs in this lib and write your own automation script. Enjot! :-)

##TODO
1. 創立帳號, 自動註冊
2. 登入不同server 
3. 每日翻牌與簽到
4. 刷四甲
5. 定時打不敗

##Sample Code
###打魔教
```
attackPagan(3, 8, 999999, 0)
```
參數意義:</br>
從主畫面出發, 血戰打到第3關, 力戰打到第8關, 奮戰打到第999999關(等於無窮盡打下去), buff策略為 `0`, buff 策略目前僅提供兩策略:

* 0: 分別於30%以及15%找氣血, 武力. 有的話就加, 要不然就加3%</br>
* 1: 永遠選擇3%</br>

執行過程訊息輸出如下: (奮戰打到68關就死了, 汗...)<br/>
![image](https://raw.github.com/SikuliScriptForWuXiaQChuan/AutoCreatingForThreeJia/master/ScreenShot/lose.png
)<br/>

###保護童姥
基本構成的method如下:
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
也可以使用`protectChildElder(times)`, times是指要保護童姥幾次.
