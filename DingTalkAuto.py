from operator import truediv
import time
from PIL import Image
import pyautogui
import sys
import cv2

pyautogui.FAILSAFE = True #自动防故障

#版本确认
version = "0.0.2" #版本号
line = "b" #产品线
print("当前版本：" + version + line)
print("程序运行中")

LastOnce = False #最后确认

#预加载目标图像
DingLiveIcon = Image.open(r"./source/DingLiveIcon.png")
DingMeetingIcon = Image.open(r"./source/DingMeetingIcon.png")
DingMeetingCallIcon = Image.open(r"./source/DingMeetingCallIcon.png")
DingMicIcon = Image.open(r"./source/DingMicIcon.png")
DingCamIcon = Image.open(r"./source/DingCamIcon.png")
DingEnterIcon = Image.open(r"./source/DingEnterIcon.png")
DingSignIcon = Image.open(r"./source/DingSignIcon.png")

while True:
    time.sleep(1) #延时执行
    #截图直播或会议
    DingLive = pyautogui.locateOnScreen(DingLiveIcon)
    DingMeeting = pyautogui.locateOnScreen(DingMeetingIcon)
    DingMeetingCall = pyautogui.locateOnScreen(DingMeetingCallIcon,confidence=0.9)

    #判断课程类型并执行加入过程

    #直播
    if DingLive:
        x,y,width,height = DingLive
        pyautogui.click(x,y,button="left")
        print("进入直播成功，正在等待签到，或使用ctrl+c退出")
        #等待签到
        while True:
            time.sleep(1)#延时执行
            DingSign = pyautogui.locateOnScreen(DingSignIcon)#截图签到图标

            #签到
            if DingSign:
                x,y,width,height = DingSign
                pyautogui.click(x,y,button="left")
                print("签到完成")

    #被邀请时加入会议
    if DingMeetingCall:
        x,y,width,height = DingMeetingCall
        pyautogui.click(x,y,button="left")

        time.sleep(5)

        #麦克风操作
        while True:
            DingMic = pyautogui.locateOnScreen(DingMicIcon) #截图麦克风图标

            #关闭麦克风
            if DingMic:
                x,y,width,height = DingMic
                pyautogui.click(x,y,button="left")
            else:
                break
        
        #摄像头操作
        while True:
            DingCam = pyautogui.locateOnScreen(DingCamIcon) #截图摄像头图标

            #关闭摄像头
            if DingCam:
                x,y,width,height = DingCam
                pyautogui.click(x,y,button="left")
            else:
                break            

        print("进入会议成功，程序即将退出")
        sys.exit() #进入后退出程序

    #中途加入会议
    if DingMeeting:
        LastOnce = True #开始最后一次循环
        x,y,width,height = DingMeeting
        pyautogui.click(x,y,button="left")

        time.sleep(1)

        #麦克风操作
        while True:
            DingMic = pyautogui.locateOnScreen(DingMicIcon) #截图麦克风图标

            #关闭麦克风
            if DingMic:
                x,y,width,height = DingMic
                pyautogui.click(x,y,button="left")
            else:
                break
        
        #摄像头操作
        while True:
            DingCam = pyautogui.locateOnScreen(DingCamIcon) #截图摄像头图标

            #关闭摄像头
            if DingCam:
                x,y,width,height = DingCam
                pyautogui.click(x,y,button="left")
            else:
                break

        #进入会议
        while True:
            DingEnter = pyautogui.locateOnScreen(DingEnterIcon) #截图进入会议图标

            #进入会议
            if DingEnter:
                x,y,width,height = DingEnter
                pyautogui.click(x,y,button="left")
            else:
                break

    if LastOnce == True:        
        print("进入会议成功，程序即将退出")
        sys.exit() #进入后退出程序

