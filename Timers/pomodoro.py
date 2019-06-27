import time, subprocess
timeLeft = 25
secLeft = 0
while timeLeft > 0:
    time.sleep(1)
    if secLeft==0:
        print(timeLeft)
        secLeft=60
        timeLeft-=1
    secLeft -= 1
subprocess.Popen(['start', "C:/Users/Adam/Music/alarm.mp3"], shell=True)