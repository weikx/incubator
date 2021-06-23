import RPi.GPIO as GPIO
import Adafruit_DHT
import time

DHT22Port = 4
relayPort = 17
sensor = Adafruit_DHT.DHT22
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPort, GPIO.OUT)


def getTemp():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT22Port)
        heating(temperature)
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        time.sleep(2)


def heating(temp):
    if (temp >= 37.5):
        GPIO.output(relayPort, GPIO.HIGH)
        print('stop heating{0:0.1f}*C'.format(temp))
    else:
        GPIO.output(relayPort, GPIO.LOW)
        print('heating{0:0.1f}*C'.format(temp))
