from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()

import random


def generate_random_number():
    min_value = 10**8  # this is the smallest 9-digit number
    max_value = 10**9 - 1  # this is the largest 9-digit number
    return str(random.randint(min_value, max_value))


def writeRFID():
    try:
        text = f"CHJNHB987654321"
        print("Now place your tag to write")
        reader.write(text=text)
        return [id, text]
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise


writeRFID()
