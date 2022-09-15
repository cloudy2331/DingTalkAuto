from email.mime import image
import sys
import time
from turtle import width
from PIL import Image
import pyautogui
import cv2

pyautogui.FAILSAFE = True #自动防故障

#版本确认
version = "0.1.0" #版本号
line = "a" #产品线
print("当前版本：" + version + line)
print("程序运行中，请保持需要进行签到的群组聊天界面完整显示")

#接龙输入内容
SolitaireInput = "."

#预加载目标图像
DingSolitaireIcon = Image.open(r"./source/DingSolitaireIcon.png")
DingSolitaireInputIcon = Image.open(r"./source/DingSolitaireInputIcon.png")
DingSolitaireSendIcon = Image.open(r"./source/DingSolitaireSendIcon.png")

while True:
    time.sleep(1) #延时执行

    #截图群内签到或接龙等
    try:
        DingSolitaire = pyautogui.locateOnScreen(DingSolitaireIcon)
    except:
        DingSolitaire = None

    #接龙
    if DingSolitaire:
        x,y,width,height = DingSolitaire
        pyautogui.click(x,y,button="left")
        time.sleep(1) #延时执行
        
        #输入接龙内容
        while True:
            try:
                DingSolitaireInput = pyautogui.locateOnScreen(DingSolitaireInputIcon)
            except:
                DingSolitaireInput = None
            
            if DingSolitaireInput:
                x,y,width,height = DingSolitaireInput
                pyautogui.click(x,y,button="left")
                time.sleep(1) #延时执行
                pyautogui.typewrite(SolitaireInput)
                time.sleep(1) #延时执行
                while True:
                    try:
                        pyautogui.scroll(-20)
                        DingSolitaireSend = pyautogui.locateOnScreen(DingSolitaireSendIcon)
                    except:
                        DingSolitaireSend = None
                    
                    if DingSolitaireSend:
                        x,y,width,height = DingSolitaireSend
                        pyautogui.click(x,y,button="left")
                        print("接龙完成，程序即将退出")
                        sys.exit()
