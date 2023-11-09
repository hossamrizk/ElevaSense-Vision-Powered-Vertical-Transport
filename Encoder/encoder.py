# Set GPIO pin numbers
import RPi.GPIO as GPIO
import time
IN1 = 16
IN2 = 18
EN = 32
sp_forward= 1.743
sp_backward= 1.494

#Set GPIO mode and pin direction
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

# Create PWM object
pwm = GPIO.PWM(EN, 10)  # 1 kHz frequency

# Start PWM at 0% duty cycle
pwm.start(0)

# Function to drive motor forward
def motor_forward(num_floors):
    GPIO.output(IN1,True)
    GPIO.output(IN2, False)
    pwm.ChangeDutyCycle(100)  # 50% duty cycle
    time.sleep(sp_forward * num_floors)
    motor_stop()    

# Function to drive motor backward
def motor_backward(num_floors):
    time.sleep(1)
    GPIO.output(IN2, True)
    GPIO.output(IN1, False)
    pwm.ChangeDutyCycle(100)  # 50% duty cycle
    time.sleep(sp_backward * num_floors)
    motor_stop()  

# Function to stop motor
def motor_stop():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    pwm.ChangeDutyCycle(0)  # 0% duty cycle

motor_forward(1)
time.sleep(1)
motor_backward(1)
