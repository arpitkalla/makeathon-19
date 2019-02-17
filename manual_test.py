import RPi.GPIO as GPIO          
from time import sleep
from threading import Thread
m1_in1 = 24
m1_in2 = 23
m1_en = 25
temp1=1

m2_in1 = 10
m2_in2 = 9
m2_en = 11
temp2=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(m1_in1,GPIO.OUT)
GPIO.setup(m1_in2,GPIO.OUT)
GPIO.setup(m1_en,GPIO.OUT)
GPIO.output(m1_in1,GPIO.LOW)
GPIO.output(m1_in2,GPIO.LOW)
m1_p=GPIO.PWM(m1_en,100)
m1_p.start(100)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(m2_in1,GPIO.OUT)
GPIO.setup(m2_in2,GPIO.OUT)
GPIO.setup(m2_en,GPIO.OUT)
GPIO.output(m2_in1,GPIO.LOW)
GPIO.output(m2_in2,GPIO.LOW)
m2_p=GPIO.PWM(m2_en,100)
m2_p.start(100)


while True:
  GPIO.output(m1_in1,GPIO.HIGH)
  GPIO.output(m1_in2,GPIO.LOW)

  GPIO.output(m2_in1,GPIO.HIGH)
  GPIO.output(m2_in2,GPIO.LOW)
  
  raw_input()

