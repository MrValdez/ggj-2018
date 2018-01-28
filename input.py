# Joystick module is inefficient but works

import pygame

class Input:
    def __init__(self):
        self.left = self.right = self.up = self.down = False
        self.left_hold = self.right_hold = self.up_hold = self.down_hold = False
        self.button1 = self.button2 = False
        self.prev_keys = pygame.key.get_pressed()
        self.deadzone = 0.2
        
        self.button1_bindings = pygame.K_q
        self.button2_bindings = pygame.K_w
        self.button3_bindings = pygame.K_SPACE
        self.button4_bindings = pygame.K_RETURN
        
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0) if pygame.joystick.get_count() else None

        if self.joystick:
            self.joystick.init()
            self.prev_buttons = [self.joystick.get_button(0), self.joystick.get_button(1)]

    def update(self):
        keys = pygame.key.get_pressed()

        def check_stick_move(key, key_to_check, deadzone):
            if key != key_to_check:
                return False

            hat = self.joystick.get_hat(0)
            axis = self.joystick.get_axis(0)
            move = False

            if key_to_check == pygame.K_LEFT:
                move = hat[0] < 0 or self.joystick.get_axis(0) < -deadzone
            if key_to_check == pygame.K_RIGHT:
                move = hat[0] > 0 or self.joystick.get_axis(0) > deadzone
            if key_to_check == pygame.K_UP:
                move = hat[1] > 0 or self.joystick.get_axis(1) < -deadzone
            if key_to_check == pygame.K_DOWN:
                move = hat[1] < 0 or self.joystick.get_axis(1) > deadzone

            return move

        def check_stick_move_press(key, key_to_check, deadzone):
            if key != key_to_check:
                return False

            hat = self.joystick.get_hat(0)
            axis = self.joystick.get_axis(0)
            move = False

            if key_to_check == pygame.K_LEFT:
                move = (hat[0] < 0 or self.joystick.get_axis(0) < -deadzone) 
            if key_to_check == pygame.K_RIGHT:
                move = (hat[0] > 0 or self.joystick.get_axis(0) > deadzone)
            if key_to_check == pygame.K_UP:
                move = (hat[1] > 0 or self.joystick.get_axis(1) < -deadzone)
            if key_to_check == pygame.K_DOWN:
                move = (hat[1] < 0 or self.joystick.get_axis(1) > deadzone)

            move = move and not self.prev_keys[key_to_check]

            return move

        def check_stick_button_press(key):
            if key == self.button1_bindings:
                return self.joystick.get_button(0) and not self.prev_buttons[0]
            elif key == self.button2_bindings:
                return self.joystick.get_button(1) and not self.prev_buttons[1]
            elif key == self.button3_bindings:
                return self.joystick.get_button(2) and not self.prev_buttons[2]
            elif key == self.button4_bindings:
                return self.joystick.get_button(3) and not self.prev_buttons[3]
            
            return False

        def check_stick_button_hold(key):
            if key == self.button1_bindings:
                return self.joystick.get_button(0)
            elif key == self.button2_bindings:
                return self.joystick.get_button(1)
            elif key == self.button3_bindings:
                return self.joystick.get_button(2)
            elif key == self.button4_bindings:
                return self.joystick.get_button(3)
            
            return False

        def check_key(key):
            result_joy = False
            result_key = keys[key] and not self.prev_keys[key]

            if self.joystick:
                result_joy = (check_stick_move_press(key, pygame.K_LEFT, self.deadzone) or
                              check_stick_move_press(key, pygame.K_RIGHT, self.deadzone) or
                              check_stick_move_press(key, pygame.K_UP, self.deadzone) or
                              check_stick_move_press(key, pygame.K_DOWN, self.deadzone) or
                              check_stick_button_press(key)
                              )
                
            return result_key or result_joy

        def check_keyhold(key):
            result_joy = False
            result_key = keys[key]

            if self.joystick:
                result_joy = (check_stick_move(key, pygame.K_LEFT, self.deadzone) or
                              check_stick_move(key, pygame.K_RIGHT, self.deadzone) or
                              check_stick_move(key, pygame.K_UP, self.deadzone) or
                              check_stick_move(key, pygame.K_DOWN, self.deadzone) or
                              check_stick_button_hold(key)
                              )

            return result_key or result_joy

        self.left = check_key(pygame.K_LEFT)
        self.right = check_key(pygame.K_RIGHT)
        self.up = check_key(pygame.K_UP)
        self.down = check_key(pygame.K_DOWN)
        self.button1 = check_key(self.button1_bindings)
        self.button2 = check_key(self.button2_bindings)
        self.button3 = check_key(self.button3_bindings)
        self.button4 = check_key(self.button4_bindings)

        self.left_hold = check_keyhold(pygame.K_LEFT)
        self.right_hold = check_keyhold(pygame.K_RIGHT)
        self.up_hold = check_keyhold(pygame.K_UP)
        self.down_hold = check_keyhold(pygame.K_DOWN)
        self.button1_hold = check_keyhold(self.button1_bindings)
        self.button2_hold = check_keyhold(self.button2_bindings)
        self.button3_hold = check_keyhold(self.button3_bindings)
        self.button4_hold = check_keyhold(self.button4_bindings)

        # any button is pushed
        self.button = self.button1 or self.button2 or self.button3 or self.button4
        self.button_hold = self.button1_hold or self.button2_hold or self.button3_hold or self.button4_hold

        self.prev_keys = keys
        if self.joystick:
            self.prev_buttons = [self.joystick.get_button(0), self.joystick.get_button(1)]

            #hack
            self.prev_keys = list(self.prev_keys)
            self.prev_keys[pygame.K_LEFT] = self.left or self.left_hold
            self.prev_keys[pygame.K_RIGHT] = self.right or self.right_hold
            self.prev_keys[pygame.K_UP] = self.up or self.up_hold
            self.prev_keys[pygame.K_DOWN] = self.down or self.down_hold