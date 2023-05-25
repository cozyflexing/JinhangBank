from time import sleep
import sys
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


def readRFID():
    try:
        id, text = reader.read()
        return text
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise
