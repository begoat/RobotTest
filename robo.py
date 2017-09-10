import threading
import DobotDllType as dType
import time

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
}

# #load Dll 
api = dType.load()

#Connect Dobot 
state = dType.ConnectDobot(api,"",115200)[0]
print("Connect status",CON_STR[state])

if(state == dType.DobotConnect.DobotConnect_NoError):
    #Clean Commend Queued
    dType.SetQueuedCmdClear(api)

    #Move Home
    dType.SetHOMEParams(api,200,50,0,50,isQueued = 1)
    dType.SetPTPJointParams(api,200,200,200,200,300,300,200,200,isQueued = 1)
    dType.SetPTPCommonParams(api,100,100,isQueued = 1)

    #Async Home
    dType.SetHOMECmd(api,temp = -20,isQueued = 1)



lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,200,50,-10,50,isQueued = 1)

print(result)

def execute(lastIndex):
    dType.SetQueuedCmdStartExec(api)

#wait
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api):
        dType.dSleep(100)
    
    #Stop
    dType.SetQueuedCmdStopExec(api)
    print("execute!")

def strongPush(x,y):
    #move
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x,y,-10,50,isQueued = 1)
    #push
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x,y,-38,50,isQueued = 1)
    #up
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x,y,-10,50,isQueued = 1)
    print('strong pushed')
    execute(lastIndex)

def lightPush(x,y):
    x += 200
    y += 50
    #move
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x,y,-10,50,isQueued = 1)
    #push
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x,y,-35,50,isQueued = 1)
    #up
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x,y,-10,50,isQueued = 1)
    execute(lastIndex)

def screenUpMove():
    #move
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,250,50,-10,50,isQueued = 1)
    #push
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,250,50,-35,50,isQueued = 1)
    #move on screen
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,278,50,-34,50,isQueued = 1)
    #up
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,278,50,-10,50,isQueued = 1)
    execute(lastIndex)

def screenDownMove():
    #move
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,278,50,-10,50,isQueued = 1)
    #push
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,278,50,-35,50,isQueued = 1)
    #move on screen
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,250,50,-34,50,isQueued = 1)
    #up
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,250,50,-10,50,isQueued = 1)
    execute(lastIndex)
def screenLeftMove():
    #move
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,267,28,-10,50,isQueued = 1)
    #push
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,267,28,-35,50,isQueued = 1)
    #move on screen
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,267,67,-34,50,isQueued = 1)
    #up
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,267,67,-10,50,isQueued = 1)
    execute(lastIndex)

def screenRightMove():
    #move
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,267,67,-10,50,isQueued = 1)
    #push
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,267,67,-35,50,isQueued = 1)
    #move on screen
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,267,28,-34,50,isQueued = 1)
    #up
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,267,28,-10,50,isQueued = 1)
    execute(lastIndex)
def up():
    lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-10,50,isQueued = 1)
    execute(lastIndex)

def unlock(a1,a2,a3,a4,a5,a6):
    #1
    if a1=="1":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-35,50,isQueued = 1)
    #2
    elif a1=="2":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-35,50,isQueued = 1)
    #3
    elif a1=="3":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-35,50,isQueued = 1)
    #4
    elif a1=="4":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-35,50,isQueued = 1)
    #5
    elif a1=="5":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-35,50,isQueued = 1)
    #6
    elif a1=="6":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-35,50,isQueued = 1)
    #7
    elif a1=="7":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-35,50,isQueued = 1)
    #8
    elif a1=="8":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-35,50,isQueued = 1)
    #9
    elif a1=="9":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-35,50,isQueued = 1)
    #0
    else:
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-35,50,isQueued = 1)
    up()
    ########################################################################################
    #1
    if a2=="1":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-35,50,isQueued = 1)
    #2
    elif a2=="2":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-35,50,isQueued = 1)
    #3
    elif a2=="3":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-35,50,isQueued = 1)
    #4
    elif a2=="4":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-35,50,isQueued = 1)
    #5
    elif a2=="5":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-35,50,isQueued = 1)
    #6
    elif a2=="6":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-35,50,isQueued = 1)
    #7
    elif a2=="7":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-35,50,isQueued = 1)
    #8
    elif a2=="8":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-35,50,isQueued = 1)
    #9
    elif a2=="9":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-35,50,isQueued = 1)
    #0
    else:
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-35,50,isQueued = 1)
    up()
    ############
    if a3=="1":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-35,50,isQueued = 1)
    #2
    elif a3=="2":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-35,50,isQueued = 1)
    #3
    elif a3=="3":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-35,50,isQueued = 1)
    #4
    elif a3=="4":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-35,50,isQueued = 1)
    #5
    elif a3=="5":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-35,50,isQueued = 1)
    #6
    elif a3=="6":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-35,50,isQueued = 1)
    #7
    elif a3=="7":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-35,50,isQueued = 1)
    #8
    elif a3=="8":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-35,50,isQueued = 1)
    #9
    elif a3=="9":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-35,50,isQueued = 1)
    #0
    else:
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-35,50,isQueued = 1)
    up()
    #########
    if a4=="1":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-35,50,isQueued = 1)
    #2
    elif a4=="2":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-35,50,isQueued = 1)
    #3
    elif a4=="3":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-35,50,isQueued = 1)
    #4
    elif a4=="4":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-35,50,isQueued = 1)
    #5
    elif a4=="5":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-35,50,isQueued = 1)
    #6
    elif a4=="6":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-35,50,isQueued = 1)
    #7
    elif a4=="7":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-35,50,isQueued = 1)
    #8
    elif a4=="8":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-35,50,isQueued = 1)
    #9
    elif a4=="9":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-35,50,isQueued = 1)
    #0
    else:
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-35,50,isQueued = 1)
    up()
    ##################################################################    
    if a5=="1":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-35,50,isQueued = 1)
    #2
    elif a5=="2":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-35,50,isQueued = 1)
    #3
    elif a5=="3":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-35,50,isQueued = 1)
    #4
    elif a5=="4":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-35,50,isQueued = 1)
    #5
    elif a5=="5":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-35,50,isQueued = 1)
    #6
    elif a5=="6":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-35,50,isQueued = 1)
    #7
    elif a5=="7":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-35,50,isQueued = 1)
    #8
    elif a5=="8":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-35,50,isQueued = 1)
    #9
    elif a5=="9":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-35,50,isQueued = 1)
    #0
    else:
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-35,50,isQueued = 1)
    up()
    ######
    if a6=="1":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,65,-35,50,isQueued = 1)
    #2
    elif a6=="2":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,50,-35,50,isQueued = 1)
    #3
    elif a6=="3":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,270,35,-35,50,isQueued = 1)
    #4
    elif a6=="4":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,65,-35,50,isQueued = 1)
    #5
    elif a6=="5":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,50,-35,50,isQueued = 1)
    #6
    elif a6=="6":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,256,35,-35,50,isQueued = 1)
    #7
    elif a6=="7":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,65,-35,50,isQueued = 1)
    #8
    elif a6=="8":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,50,-35,50,isQueued = 1)
    #9
    elif a6=="9":
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,245,35,-35,50,isQueued = 1)
    #0
    else:
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-10,50,isQueued = 1)
        lastIndex, result = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,228,50,-35,50,isQueued = 1)
    up()
    #########
    #DobotConnect_Occupied

    print('unlocked')
    execute(lastIndex)

# My_x=0
# My_y=0
# num=0
#My_x,My_y=input("输入home坐标：").split(' ')

if __name__ == '__main__':

    strongPush(200,50)
    strongPush(200,50)
    num1,num2,num3,num4,num5,num6=input("输入开机密码：").split(' ')
    print(num1,num2,num3,num4,num5,num6)
    unlock(num1,num2,num3,num4,num5,num6)
    screenLeftMove()
    screenRightMove()

