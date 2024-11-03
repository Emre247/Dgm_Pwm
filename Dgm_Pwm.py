import RPi.GPIO as GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
cikisPin=38
GPIO.setup(cikisPin,GPIO.OUT)
benimDGM=GPIO.PWM(cikisPin,100)
#60 herz üzerinden işlem yapıyorum. İnsan gözü bu değerden sonra
#ki tüm değerleri ayırt edemiyor ya da çok yakın hissediyor.
benimDGM.start(50)
