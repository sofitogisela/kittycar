import cv2
import gpiozero

# Initialize GPIO components
stop_button = gpiozero.Button(17)       # Emergency stop button (GPIO 17)
stop_led = gpiozero.LED(27)             # Emergency LED (GPIO 27)
motor_left = gpiozero.Motor(forward=5, backward=6)  # Motors for left and right wheels
motor_right = gpiozero.Motor(forward=13, backward=19)
speed = 0.5                             # Set initial speed (0 to 1 scale)

# Camera initialization
cap = cv2.VideoCapture(0)  # 0 is usually the default camera

# Flag variables
running = True
obstacle_detected = False

def emergency_stop():
    """Handle emergency stop."""
    global running
    print("Emergency stop activated!")
    stop_led.on()
    motor_left.stop()
    motor_right.stop()
    running = False

# Attach emergency stop to button
stop_button.when_pressed = emergency_stop

def detect_obstacle(frame):
    """Detect obstacles in the frame using color detection."""
    global obstacle_detected
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Define color range for obstacles (e.g., orange)
    lower_orange = (10, 100, 100)
    upper_orange = (25, 255, 255)
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    
    mask_val = cv2.countNonZero(mask)

    print(f"Mask value: {mask_val}")
    obstacle = mask_val > 20000  # Threshold for obstacle detection
    if obstacle:
        obstacle_detected = True
        motor_left.stop()
        motor_right.stop()
        print("Obstacle detected!")
    else:
        obstacle_detected = False

def track_follow(frame):
    """Follow the track based on detected lines."""
    # Convert to grayscale and detect edges for line tracking
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    # Track the line using edges and simple control
    # (Add more logic for real-time track following based on contours)
    if not obstacle_detected:
        print("Following the track")
        motor_left.forward(speed)
        motor_right.forward(speed)
    else:
        motor_left.stop()
        motor_right.stop()

def main():
    global running
    while running:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break

        # Process the video
        detect_obstacle(frame)
        track_follow(frame)
        
        # Display processed video
        cv2.imshow("Processed Video", frame)

        # End the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    motor_left.stop()
    motor_right.stop()
    stop_led.off()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        emergency_stop()
        print("Program terminated.")