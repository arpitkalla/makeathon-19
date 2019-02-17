import RPi.GPIO as GPIO          
from time import sleep

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

GPIO.setup(m2_in1,GPIO.OUT)
GPIO.setup(m2_in2,GPIO.OUT)
GPIO.setup(m2_en,GPIO.OUT)
GPIO.output(m2_in1,GPIO.LOW)
GPIO.output(m2_in2,GPIO.LOW)
m2_p=GPIO.PWM(m2_en,100)
m2_p.start(100)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=raw_input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         # First motor forwards
         GPIO.output(m1_in1,GPIO.HIGH)
         GPIO.output(m1_in2,GPIO.LOW)

         # Second motor forwards
         GPIO.output(m2_in1,GPIO.HIGH)
         GPIO.output(m2_in2,GPIO.LOW)
         print("forward")
        else:
         # First motor backwards
         GPIO.output(m1_in1,GPIO.LOW)
         GPIO.output(m1_in2,GPIO.HIGH)

         # Second motor backwards 
         GPIO.output(m2_in1,GPIO.LOW)
         GPIO.output(m2_in2,GPIO.HIGH)
         print("backward")
