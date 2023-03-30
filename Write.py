from time import sleep
import sys
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


def writeRFID():
    try:
        text = input("What pin code would you like? ")
        print("Now place your tag to write")
        reader.write(text=text)
        return [id, text]
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise
