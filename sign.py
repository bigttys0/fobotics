import servo_controller

# Define functions for each letter of the alphabet 
def sign_A():
    servo_controller.rotate_servo(0, 90)  # Thumb up

def sign_B():
    servo_controller.rotate_servo(1, 90)  # Index finger up
    
def sign_C():
    servo_controller.rotate_servo(2, 180)  # Curly fingers 

# Execute each letter of the alphabet 
sign_A()
sign_B()
sign_C()
...
# Execute sign for 'Z'
