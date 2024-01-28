import RPi.GPIO as GPIO
import time
LED = 18
SW = 22
count = 0
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
             count = count + 1
             if count%2 != 0:
               GPIO.output(LED,True)
               print(f"LED ON!!!")
             else:
               GPIO.output(LED,False)
               print(f"LED OFF!!!")
        #print(f"Button pressed {count}")
except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nBye…")
