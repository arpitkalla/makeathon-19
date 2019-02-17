import RPi.GPIO as GPIO          
from time import sleep
from threading import Thread
from time import sleep

m_left = 12
m_right = 20
m_cam = 16
collision = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(m_left,GPIO.OUT)
GPIO.setup(m_right,GPIO.OUT)
GPIO.setup(m_cam,GPIO.OUT)
GPIO.setup(collision,GPIO.IN)

m_left_pwm = GPIO.PWM(m_left,100)
m_right_pwm = GPIO.PWM(m_right,100)
m_cam_pwm = GPIO.PWM(m_cam,100)
m_left_pwm.start(5)
m_right_pwm.start(5)
m_cam_pwm.start(5)

STEPS=10 # the number of steps either side of nominal while True: 
NOMINAL=7.5 # the 'zero' PWM %age is_collision = GPIO.input(collision)
RANGE=1.0   # the maximum variation %age above/below NOMINAL        if not is_collision:

def collision_avoid():
        m_left_pwm.ChangeDutyCycle(0)
        m_cam_pwm.ChangeDutyCycle(0)

#thread = Thread(target=collision_avoid)
#thread.daemon = True
#thread.start()


def set_angle(angle):
	duty = angle / 18 + 2
	m_cam_pwm.ChangeDutyCycle(duty)
	sleep(1)
	#m_cam_pwm.ChangeDutyCycle(0)

def forward():
	print("forward")
	m_left_pwm.ChangeDutyCycle(2.5)
	m_right_pwm.ChangeDutyCycle(2.5)
	sleep(5)
	m_left_pwm.ChangeDutyCycle(11.5) # may need to be adjusted
	m_right_pwm.ChangeDutyCycle(11.5)
	sleep(5)
	m_left_pwm.ChangeDutyCycle(20.5)
	m_right_pwm.ChangeDutyCycle(20.5)
	sleep(5)
	m_left_pwm.ChangeDutyCycle(11.5) # may need to be adjusted
	m_right_pwm.ChangeDutyCycle(11.5)

def backward():
	print("backward")
	m_left_pwm.ChangeDutyCycle(25)
	m_right_pwm.ChangeDutyCycle(25)
	sleep(1)
def right():
	m_left_pwm.ChangeDutyCycle(2.5)
	m_right_pwm.ChangeDutyCycle(2.5)
	sleep(1)
def left():
	m_left_pwm.ChangeDutyCycle(2.5)
	m_right_pwm.ChangeDutyCycle(7.5)
	sleep(1)
def stop():
	print("Stopping")
	GPIO.cleanup()
