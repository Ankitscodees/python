import RPi.GPIO as GPIO
import time

# Pin configuration
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# PWM setup
red_pwm = GPIO.PWM(RED_PIN, 100)
green_pwm = GPIO.PWM(GREEN_PIN, 100)
blue_pwm = GPIO.PWM(BLUE_PIN, 100)
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

def set_color(r, g, b):
    red_pwm.ChangeDutyCycle(r)
    green_pwm.ChangeDutyCycle(g)
    blue_pwm.ChangeDutyCycle(b)

try:
    while True:
        set_color(100, 0, 0)  # Red
        time.sleep(1)
        set_color(0, 100, 0)  # Green
        time.sleep(1)
        set_color(0, 0, 100)  # Blue
        time.sleep(1)
        set_color(100, 100, 0)  # Yellow
        time.sleep(1)
        set_color(100, 0, 100)  # Purple
        time.sleep(1)
        set_color(0, 100, 100)  # Cyan
        time.sleep(1)
except KeyboardInterrupt:
    pass
