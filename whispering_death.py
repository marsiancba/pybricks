from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Direction, Port
from pybricks.tools import wait
from pybricks.iodevices import XboxController

hub = PrimeHub()

print("Whispering Death - connecting to Xbox controller...")
xbox = XboxController()
print("Xbox controller connected!")

motor_right_leg = Motor(Port.A, Direction.CLOCKWISE)
motor_left_leg = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_tail = Motor(Port.D, Direction.CLOCKWISE)

LEG_ANGLE = 90
TAIL_MAX_ANGLE = 60
MOVE_SPEED = 300
STICK_DEADZONE = 10

motor_right_leg.run_target(MOVE_SPEED, 0, wait=False)
motor_left_leg.run_target(MOVE_SPEED, 0, wait=False)
motor_tail.run_target(MOVE_SPEED, 0, wait=False)

hub.speaker.beep()

def sound_roar():  # Y button
    for f, d in [(180, 60), (250, 50), (350, 40), (500, 80), (650, 100), (400, 60), (200, 80)]:
        hub.speaker.beep(f, d)

def sound_fire():  # A button
    for f in range(400, 2200, 180):
        hub.speaker.beep(f, 12)
    for f, d in [(900, 30), (600, 40), (450, 50), (300, 60), (200, 80)]:
        hub.speaker.beep(f, d)

def sound_hiss():  # B button
    for _ in range(6):
        for f in (2800, 3200, 3600):
            hub.speaker.beep(f, 15)
    hub.speaker.beep(2400, 40)

def sound_growl():  # X button
    for f, d in [(220, 70), (180, 50), (260, 70), (200, 50), (240, 90), (160, 100)]:
        hub.speaker.beep(f, d)

last_buttons = set()

while True:
    lt, rt = xbox.triggers()

    right_leg_target = (rt / 100) * LEG_ANGLE
    left_leg_target = (lt / 100) * LEG_ANGLE

    motor_right_leg.track_target(right_leg_target)
    motor_left_leg.track_target(left_leg_target)

    stick_x = xbox.joystick_right()[0]
    if abs(stick_x) < STICK_DEADZONE:
        stick_x = 0
    tail_target = -(stick_x / 100) * TAIL_MAX_ANGLE
    motor_tail.track_target(tail_target)

    pressed = xbox.buttons.pressed()
    new_presses = set(pressed) - last_buttons

    if Button.Y in new_presses:
        sound_roar()
    if Button.A in new_presses:
        sound_fire()
    if Button.B in new_presses:
        sound_hiss()
    if Button.X in new_presses:
        sound_growl()

    last_buttons = set(pressed)

    wait(20)
