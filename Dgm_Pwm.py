import RPi.GPIO as GPIO
from time import sleep
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
cikisPin=38
GPIO.setup(cikisPin,GPIO.OUT)
GPIO.output(cikisPin,True)
#60 herz üzerinden işlem yapıyorum. İnsan gözü bu değerden sonra
#ki tüm değerleri ayırt edemiyor ya da çok yakın hissediyor.
benimDGM=GPIO.PWM(cikisPin,60)
benimDGM.start(30)
