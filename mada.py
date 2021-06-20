import RPi.GPIO as GPIO
import time

delay = 2  # delay 2ms

pin_4 = 4
pin_17 = 17
pin_23 = 23
pin_24 = 24

GPIO.setmode(GPIO.BCM)  # 设置引脚的编码方式


def init():
    GPIO.setwarnings(False)
    GPIO.setup(pin_4, GPIO.OUT)
    GPIO.setup(pin_17, GPIO.OUT)
    GPIO.setup(pin_23, GPIO.OUT)
    GPIO.setup(pin_24, GPIO.OUT)


def forward(delay):
    setStep(1, 0, 0, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 0)
    time.sleep(delay)
    setStep(0, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 0, 0, 1)
    time.sleep(delay)


def setStep(w1, w2, w3, w4):
    GPIO.output(pin_4, w1)
    GPIO.output(pin_17, w2)
    GPIO.output(pin_23, w3)
    GPIO.output(pin_24, w4)


def main():
    init()
    while True:
        forward(int(delay) / 1000.0)


main()  # 调用main
