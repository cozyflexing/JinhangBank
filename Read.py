from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()


def readRFID():
    try:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id, text))
        return [id, text]
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise


readRFID()
