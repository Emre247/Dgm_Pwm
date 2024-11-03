import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
GPIO.output(38,True)
GPIO.output(38,False)