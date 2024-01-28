import RPi.GPIO as GPIO
import time
LEDR = 18
LEDG = 15
LEDB = 14
 
SW = 22
count = 0
 
import RPi.GPIO as GPIO
import time
 
LED_color = [LEDR, LEDG, LEDB]
state_color = [0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111]
current_state = 0
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
for pin in LED_color:
   GPIO.setup(pin, GPIO.OUT)
 
def changeClr(State):
   for i in range(2,-1,-1):
      if State & 0x01:
         GPIO.output(LED_color[i],1)
      else:
         GPIO.output(LED_color[i],0)
      State >>= 1
 
try:
   for pin in LED_color:
     GPIO.output(pin, 0)
   while True:
      if GPIO.wait_for_edge(SW, GPIO.FALLING):
         current_state = (current_state + 1) % len(state_color)
         changeClr(state_color[current_state])
         time.sleep(0.2)
 
except KeyboardInterrupt:
    GPIO.cleanup()
 
print("\nBye..........")
