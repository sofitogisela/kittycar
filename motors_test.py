from gpiozero import Motor
from time import sleep

# Initialize motors with PWM-compatible GPIO pins
motor_left = Motor(forward=12, backward=6)
motor_right = Motor(forward=13, backward=19)

# Set speed (0 to 1 scale, where 1 is 100% duty cycle)
speed = 0.5  # 50% speed

# Function to test the left motor forward
def test_left_motor_forward():
    print("Running left motor forward...")
    motor_left.forward(speed)
    sleep(2)
    motor_left.stop()

# Function to test the left motor backward
def test_left_motor_backward():
    print("Running left motor backward...")
    motor_left.backward(speed)
    sleep(2)
    motor_left.stop()

# Function to test the right motor forward
def test_right_motor_forward():
    print("Running right motor forward...")
    motor_right.forward(speed)
    sleep(2)
    motor_right.stop()

# Function to test the right motor backward
def test_right_motor_backward():
    print("Running right motor backward...")
    motor_right.backward(speed)
    sleep(2)
    motor_right.stop()

# Run each motor test
try:
    test_left_motor_forward()
    test_left_motor_backward()
    test_right_motor_forward()
    test_right_motor_backward()
finally:
    # Ensure motors are stopped
    motor_left.stop()
    motor_right.stop()