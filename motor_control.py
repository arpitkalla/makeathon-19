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



GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def collision_avoid():
    while True:
        is_collision = GPIO.input(14)
        if is_collision:
            m1_p.ChangeDutyCycle(0)
            m2_p.ChangeDutyCycle(0)

thread = Thread(target=collision_avoid)
thread.daemon = True
thread.start()


def m1_forwards():
    GPIO.output(m1_in1,GPIO.HIGH)
    GPIO.output(m1_in2,GPIO.LOW)

def m2_forwards():
    GPIO.output(m2_in1,GPIO.HIGH)
    GPIO.output(m2_in2,GPIO.LOW)

def m1_backwards():
    GPIO.output(m1_in1,GPIO.LOW)
    GPIO.output(m1_in2,GPIO.HIGH)

def m2_backwards():
    GPIO.output(m2_in1,GPIO.LOW)
    GPIO.output(m2_in2,GPIO.HIGH)

def move_forwards():
    m1_forwards()
    m2_forwards()
    print("forwards")

def move_backwards():
    m1_backwards()
    m2_backwards()
    print("backwards")

def move_left():
    # First motor forwards
    m1_backwards()
    m2_forwards()
    print("left")
  
def move_right():
    # First motor forwards
    m1_forwards()
    m2_backwards()
    print("right")

def start():
    m1_p.ChangeDutyCycle(100)
    m2_p.ChangeDutyCycle(100)
    print("started")

def stop():
    m1_p.ChangeDutyCycle(0)
    m2_p.ChangeDutyCycle(0)
    print("started")


