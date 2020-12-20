import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def Shutdown(channel):
    print("Shutting Down")
    os.system("echo Shutting Down | wall")
    time.sleep(5)
    os.system("sudo shutdown -P now")

GPIO.add_event_detect(21, GPIO.RISING, callback=Shutdown, bouncetime=2000)

while True:
    time.sleep(1)



