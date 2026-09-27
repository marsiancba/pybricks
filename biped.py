from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Direction, Port, Button
from pybricks.tools import wait
from pybricks.iodevices import XboxController

hub = PrimeHub()

print("Connecting to Xbox controller...")
xbox = XboxController()
print("Xbox controller connected!")

# Biped leg motors (using absolute encoder positions)
motor_left = Motor(Port.C, Direction.CLOCKWISE)
motor_right = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# Eyes (ultrasonic sensor lights)
eyes = UltrasonicSensor(Port.A)
eyes.lights.on(100)

# Hands motor (port B) - limited to ±90 degrees
motor_hands = Motor(Port.B, Direction.CLOCKWISE)
HANDS_MIN = -135
HANDS_MAX = 135
HANDS_SPEED = 2  # Degrees per trigger unit per cycle

STEP_ANGLE = 180  # Degrees per step
STEP_SPEED = 300  # Degrees per second

# Initialize legs to opposite phase positions (absolute)
motor_left.run_target(STEP_SPEED, 90, wait=False)
motor_right.run_target(STEP_SPEED, -90)

# Track current target positions
left_target = 90
right_target = -90
hands_target = 0

# Initialize hands to center position
motor_hands.run_target(200, 0, wait=False)

hub.speaker.beep()

def sound_shot():  # Y button
    for f, d in [(4000, 8), (2500, 20), (1000, 40)]:
        hub.speaker.beep(f, d)

def sound_laser():  # A button
    for f in range(800, 3000, 400):
        hub.speaker.beep(f, 10)
    for f in range(3000, 800, -600):
        hub.speaker.beep(f, 10)

def sound_robot():  # B button
    for f, d in [(600, 80), (900, 80), (1200, 80)]:
        hub.speaker.beep(f, d)

def sound_magic():  # X button
    for f, d in [(1000, 50), (1300, 50), (1600, 50), (2000, 100)]:
        hub.speaker.beep(f, d)

last_buttons = set()

while True:
    buttons = xbox.buttons.pressed()
    new_presses = set(buttons) - last_buttons
    triggers = xbox.triggers()
    
    # Hands control with triggers (LT = negative, RT = positive)
    lt, rt = triggers
    hands_delta = (rt - lt) * HANDS_SPEED / 100
    if hands_delta != 0:
        hands_target += hands_delta
        hands_target = max(HANDS_MIN, min(HANDS_MAX, hands_target))
        motor_hands.track_target(hands_target)
    
    # Check if motors are done (ready for next step)
    motors_ready = motor_left.done() and motor_right.done()
    
    # D-pad controls - continuous stepping while held
    if motors_ready:
        if Button.UP in buttons:
            left_target -= STEP_ANGLE
            right_target -= STEP_ANGLE
            motor_left.run_target(STEP_SPEED, left_target, wait=False)
            motor_right.run_target(STEP_SPEED, right_target, wait=False)
        elif Button.DOWN in buttons:
            left_target += STEP_ANGLE
            right_target += STEP_ANGLE
            motor_left.run_target(STEP_SPEED, left_target, wait=False)
            motor_right.run_target(STEP_SPEED, right_target, wait=False)
        elif Button.LEFT in buttons:
            left_target += STEP_ANGLE
            right_target -= STEP_ANGLE
            motor_left.run_target(STEP_SPEED, left_target, wait=False)
            motor_right.run_target(STEP_SPEED, right_target, wait=False)
        elif Button.RIGHT in buttons:
            left_target -= STEP_ANGLE
            right_target += STEP_ANGLE
            motor_left.run_target(STEP_SPEED, left_target, wait=False)
            motor_right.run_target(STEP_SPEED, right_target, wait=False)
    
    # Sound buttons
    if Button.Y in new_presses:
        sound_shot()
    if Button.A in new_presses:
        sound_laser()
    if Button.B in new_presses:
        sound_robot()
    if Button.X in new_presses:
        sound_magic()
    
    last_buttons = set(buttons)
    
    wait(20)
