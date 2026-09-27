from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Stop
from pybricks.tools import wait
from pybricks.iodevices import XboxController

hub = PrimeHub()

print("Connecting to Xbox controller...")
xbox = XboxController()
print("Xbox controller connected!")

# Drive motor on port C
motor_drive = Motor(Port.C, Direction.CLOCKWISE)

# Steering motor on port F - angle directly controls wheel angle
motor_steering = Motor(Port.F, Direction.CLOCKWISE)

# Reset steering to center position
motor_steering.reset_angle(0)

hub.speaker.beep()

DRIVE_SPEED = 100  # Max drive power percentage
MAX_STEERING_ANGLE = 45  # Max steering angle in degrees - adjust as needed

while True:
    # Left stick Y for throttle (negated)
    throttle = -xbox.joystick_left()[1]
    
    # Right stick X for steering angle (negated)
    steer_input = -xbox.joystick_right()[0]
    
    # Map joystick (-100 to 100) to steering angle
    target_angle = (steer_input / 100) * MAX_STEERING_ANGLE
    
    # Apply deadzone to throttle
    if abs(throttle) < 10:
        throttle = 0
    
    # Drive motor
    motor_drive.dc(throttle)
    
    # Steering - move to target angle
    motor_steering.track_target(target_angle)
    
    wait(20)
