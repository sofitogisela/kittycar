import gpiozero
from time import sleep

# Updated motor configuration
motor_left = gpiozero.Motor(forward=12, backward=6)
motor_right = gpiozero.Motor(forward=13, backward=19)
speed = 0.5  # Set speed (0 to 1 scale)

print("Testing left motor forward")
motor_left.forward(speed)
sleep(2)
motor_left.stop()

print("Testing right motor forward")
motor_right.forward(speed)
sleep(2)
motor_right.stop()