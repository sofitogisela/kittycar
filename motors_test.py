import gpiozero
from time import sleep

motor_left = gpiozero.Motor(forward=5, backward=6)
motor_right = gpiozero.Motor(forward=13, backward=19)

print("Testing left motor forward")
motor_left.forward(0.5)
sleep(2)
motor_left.stop()

print("Testing right motor forward")
motor_right.forward(0.5)
sleep(2)
motor_right.stop()

print("Testing left motor backward")
motor_left.backward(0.5)
sleep(2)
motor_left.stop()

print("Testing right motor backward")
motor_right.backward(0.5)
sleep(2)
motor_right.stop()