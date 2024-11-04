import gpiozero
import time
# Initialize GPIO components
stop_button = gpiozero.Button(17)       # Emergency stop button (GPIO 17)
stop_led = gpiozero.LED(27)             # Emergency LED (GPIO 27)
motor_left = gpiozero.Motor(forward=5, backward=6)  # Motors for left and right wheels
motor_right = gpiozero.Motor(forward=13, backward=19)
speed = 0.5                             # Set initial speed (0 to 1 scale)

motor_left.forward(speed)
motor_right.forward(speed)

time.sleep(2)

motor_left.stop()
motor_right.stop()