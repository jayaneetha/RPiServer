from platform import platform

import RPi.GPIO as GPIO

in1 = 18
in2 = 12
in3 = 13
in4 = 19
en = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
platform.p = GPIO.PWM(en, 1000)
platform.p.start(25)


def initialize_platform():
    stop()


def forward():
    _set_gpio(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)


def backward():
    _set_gpio(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)


def left():
    _set_gpio(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)


def right():
    _set_gpio(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW)


def stop():
    _set_gpio(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW)


def _set_gpio(g1, g2, g3, g4):
    GPIO.output(in1, g1)
    GPIO.output(in2, g2)
    GPIO.output(in3, g3)
    GPIO.output(in4, g4)


def change_speed(dutyCycle):
    print(f'Changing Speed {dutyCycle}')
    platform.p.ChangeDutyCycle(dutyCycle)


def shutdown_platform():
    stop()
    GPIO.cleanup()
