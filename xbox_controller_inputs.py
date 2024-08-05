import pygame
import sys

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check if there's a joystick connected
if pygame.joystick.get_count() == 0:
    print("No joystick connected!")
    sys.exit()

# Use the first joystick found
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick name: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")
print(f"Number of buttons: {joystick.get_numbuttons()}")
print(f"Number of hats: {joystick.get_numhats()}")

# Initialize previous state storage
prev_axes = [0.0] * joystick.get_numaxes()
prev_buttons = [0] * joystick.get_numbuttons()
prev_hats = [(0, 0)] * joystick.get_numhats()

# Main loop to read inputs
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.JOYAXISMOTION:
                for i in range(joystick.get_numaxes()):
                    axis_value = joystick.get_axis(i)
                    if axis_value != prev_axes[i]:
                        print(f"Axis {i} value: {axis_value}")
                        prev_axes[i] = axis_value
            elif event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
                for i in range(joystick.get_numbuttons()):
                    button_value = joystick.get_button(i)
                    if button_value != prev_buttons[i]:
                        state = "pressed" if button_value else "released"
                        print(f"Button {i} {state}")
                        prev_buttons[i] = button_value
            elif event.type == pygame.JOYHATMOTION:
                for i in range(joystick.get_numhats()):
                    hat_value = joystick.get_hat(i)
                    if hat_value != prev_hats[i]:
                        print(f"Hat {i} value: {hat_value}")
                        prev_hats[i] = hat_value

except KeyboardInterrupt:
    print("\nExiting...")
    pygame.quit()
    sys.exit()
