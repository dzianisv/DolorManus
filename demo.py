#!/usr/bin/env python3


# https://www.youtube.com/watch?v=Qh7lPC_Qf74&list=PLFbzd0m6AcmIRtTkAc3stBz77wRqlpMFD&index=11
import xarm
import enum

limit=1600

class Servo(enum.Enum):
    GRIP=1
    WRIST_ROLL=2
    WRIST_FLEX=3
    ELBOW=4
    SHOULDER_LIFT=5
    SHOULDER_PAN=6





state_1 = {
    # Servo.GRIP: 0.0,
    Servo.WRIST_ROLL: 100,
    Servo.WRIST_FLEX: 100,
    Servo.ELBOW: 100,
    Servo.SHOULDER_LIFT: 100,
    Servo.SHOULDER_PAN: 100
}

state_2 = {
    # Servo.GRIP: 0.0,
    Servo.WRIST_ROLL: 0,
    Servo.WRIST_FLEX: 0,
    Servo.ELBOW: 2500,
    Servo.SHOULDER_LIFT: 0,
    Servo.SHOULDER_PAN: 0
}

state_3 = {
    Servo.GRIP: -125.0,
    Servo.WRIST_ROLL: 125.0,
    Servo.WRIST_FLEX: 125.0,
    Servo.ELBOW: 1.0,
    Servo.SHOULDER_LIFT: 100.0,
    Servo.SHOULDER_PAN: 125.0
}


arm = xarm.Controller('USB', debug=True)
arm.actionGroupRun(0)

# for servo_id in Servo:
#     arm.servoOff(servo_id.value)


# for state in [state_1, state_2]:
#     arm.setPosition([[servo_id.value, angle] for servo_id, angle in state.items()], wait=True)

# arm.setPosition([[Servo.SHOULDER_PAN.value, 125.0]], wait=True)
# arm.setPosition([[Servo.SHOULDER_LIFT.value, 125.0]], wait=True)