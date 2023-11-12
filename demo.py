#!/usr/bin/env python3

import xarm
import enum

class Servo(enum.Enum):
    GRIP_RIGHT=1
    WRIST_ROLL=2
    WRIST_FLEX=3
    ELBOW=4
    SHOULDER_LIFT=5
    SHOULDER_PAN=6


state = {
    Servo.GRIP_RIGHT: -45.0,
    Servo.WRIST_ROLL: 0.0,
    Servo.WRIST_FLEX: 0.0,
    Servo.ELBOW: 0.0,
    Servo.SHOULDER_LIFT: 0.0,
    Servo.SHOULDER_PAN: 0.0
}

arm = xarm.Controller('USB')

arm.setPosition([[servo_id.value, angle] for servo_id, angle in state.items()], wait=True)