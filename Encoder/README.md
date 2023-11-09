# Raspberry Pi Motor Control

This Python script allows you to control a motor using a Raspberry Pi. It provides basic motor control functions, allowing you to move the motor forward and backward.

## Prerequisites

Before using this code, make sure you have the following components and libraries installed:

- Raspberry Pi
- Motor driver (to which the motor is connected)
- RPi.GPIO library
- Python 3

## Usage

1. Connect your motor driver to the Raspberry Pi GPIO pins as specified in the code.
2. Run the script on your Raspberry Pi.

### Code Explanation

- `IN1`, `IN2`, and `EN` are GPIO pin numbers, and `sp_forward` and `sp_backward` are speed constants.
- The code initializes GPIO pins, sets up PWM for motor speed control, and defines functions for motor control.
- `motor_forward(num_floors)` drives the motor forward for a specified number of floors.
- `motor_backward(num_floors)` drives the motor backward for a specified number of floors.
- `motor_stop()` stops the motor.

## Example

```python
motor_forward(1)
time.sleep(1)
motor_backward(1)

