import RPi.GPIO as GPIO 
from time import sleep 
from threading import Thread 
from time import sleep 
m_left = 8 
m_right = 9 
m_cam = 7 
collision = 14 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(m_left,GPIO.OUT) GPIO.setup(m_right,GPIO.OUT) GPIO.setup(m_cam,GPIO.OUT) 
GPIO.setup(collision,GPIO.IN) m_left_pwm = GPIO.PWM(m_left,100) m_right_pwm = 
GPIO.PWM(m_right,100) m_cam_pwm = GPIO.PWM(m_cam,100) m_left_pwm.start(5) 
m_right_pwm.start(5)
m_cam_pwm.start(5)
