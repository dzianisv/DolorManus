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


arm = xarm.Controller('USB', debug=True)
arm.actionGroupRun(0)

def move(states):
    for state in states:
        print(state)
        arm.setPosition([[servo_id.value, angle] for servo_id, angle in state.items()], wait=True)

def push_enter():
    cmds = [
        {
            Servo.ELBOW: 2100
        },{
            Servo.ELBOW: 2600,
        }
    ]
    move(cmds)

def push_power_button():
    cmds = [
        {
            Servo.SHOULDER_PAN: 700,
        },{
            Servo.ELBOW: 2100
        },{
            Servo.ELBOW: 2600
        },{
            Servo.SHOULDER_PAN: 1100
        }
    ]

    move(cmds)

def shoulder_test():
    cmds = [
        {
            Servo.SHOULDER_LIFT: 700,
        },         {
            Servo.SHOULDER_LIFT: 1500,
        },         {
            Servo.SHOULDER_LIFT: 2500,
        }, 
    ]

    move(cmds)


shoulder_test()