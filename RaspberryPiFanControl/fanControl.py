import RPi.GPIO as GPIO
import time
import os

# Return CPU temperature as float
def getCPUtemp():
    cTemp = os.popen('vcgencmd measure_temp').readline()
    return float(cTemp.replace("temp=","").replace("'C\n",""))

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(2,100)

while True:

    CPU_temp = getCPUtemp()
    if CPU_temp > 70.0:
         p.start(100)
    elif CPU_temp > 60.0:
         p.start(60)
    elif CPU_temp > 50.0:
         p.start(40)
    elif CPU_temp > 45.0:
         p.start(30)
    elif CPU_temp > 40.0:
         p.start(20)
    elif CPU_temp > 35.0:
         p.start(15)
    elif CPU_temp > 30.0:
         p.start(10)
    else:
         p.stop()
    time.sleep(15)

GPIO.cleanup()