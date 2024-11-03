import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
# PWM frekansını 60 Hz olarak ayarlıyoruz
benimDGM = GPIO.PWM(38, 60)
benimDGM.start(1)  # %30 "duty cycle" ile düşük parlaklıkta başlat
try:
    while True:
        sleep(1)  # Sonsuz döngüde bekletiyoruz
except KeyboardInterrupt:
    pass  # Çıkmak için Ctrl+C tuşlayabilirsiniz
    print("Herşey yolunda..")
    benimDGM.stop()
finally:
    GPIO.cleanup()