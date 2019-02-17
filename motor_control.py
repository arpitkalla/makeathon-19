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

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
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
  m2_forwards()
  print("left")
  
def move_right():
  # First motor forwards
  m2_forwards()
  print("right")

while(1):

  x=raw_input()
    
  if x=='r':
    print("run")
    # if obstuction detected
    if(GPIO.input(14) == 0):
      move_forwards()
      print("forward")
    else:
      print("bluetooth warning")
      # bluetooth
