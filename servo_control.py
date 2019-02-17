import RPi.GPIO as GPIO          
from time import sleep
from threading import Thread
from time import sleep

m_left = 8
m_right = 9
m_cam = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(m_left,GPIO.OUT)
GPIO.setup(m_right,GPIO.OUT)
GPIO.setup(m_cam,GPIO.OUT)

m_left_pwm = GPIO.PWM(m_left,100)
m_right_pwm = GPIO.PWM(m_right,100)
m_cam_pwm = GPIO.PWM(m_cam,100)
m_left_pwm.start(5)
m_right_pwm.start(5)
m_cam_pwm.start(5)

def collision_avoid():
    while True:
        is_collision = GPIO.input(14)
        if is_collision:
            m_left_pwm.ChangeDutyCycle(0)
            m_cam_pwm.ChangeDutyCycle(0)

thread = Thread(target=collision_avoid)
thread.daemon = True
thread.start()


def set_angle(angle):
	duty = angle / 18 + 2
	m_cam_pwm.ChangeDutyCycle(duty)
	sleep(1)
	m_cam_pwm.ChangeDutyCycle(0)

def forward():
	m_left_pwm.ChangeDutyCycle(7.5)
	m_right_pwm.ChangeDutyCycle(7.5)

def backward():
	m_left_pwm.ChangeDutyCycle(2.5)
	m_right_pwm.ChangeDutyCycle(2.5)

def right():
	m_left_pwm.ChangeDutyCycle(7.5)
	m_right_pwm.ChangeDutyCycle(2.5)

def left():
	m_left_pwm.ChangeDutyCycle(2.5)
	m_right_pwm.ChangeDutyCycle(7.5)
