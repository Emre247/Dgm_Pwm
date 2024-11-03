import RPi.GPIO as GPIO
from time import sleep
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
cikisPin=38
GPIO.setup(cikisPin,GPIO.OUT)
try:
    while True:
        GPIO.output(cikisPin,True)
        sleep(1)
except KeyboardInterrupt:
    print("Program başarılı bir şekilde kapatıldı..")
    GPIO.cleanup()

