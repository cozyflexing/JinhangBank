from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()


def readRFID():
    try:
        id, text = reader.read()
        return text
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise


readRFID()
