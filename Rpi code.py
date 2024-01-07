import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)                   

trigPIN = 23
GPIO.setup(trigPIN, GPIO.OUT, initial=GPIO.LOW)

echoPIN = 24
GPIO.setup(echoPIN, GPIO.IN)

switch1 = 4
switch2 = 27
switch3 = 22
switch4 = 5


def main():
    sleep(2)
    while GPIO.input(switch1):
        print("Working1")
    while GPIO.input(switch2):
        print("Working2")
    while GPIO.input(switch3):
        print("Working3")
    while GPIO.input(switch4):
        print("Working4")
        


if __name__ == "__main__":
    while True:
        main()

while t:
    time.sleep(1)
    t -= 1
    print(t)
