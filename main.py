def on_gesture_eight_g():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_button_pressed_a():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_free_fall():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_gesture_logo_up():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_six_g():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

def on_gesture_screen_up():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_screen_down():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_ab():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_gesture_three_g():
    radio.send_string("INTRUDER!")
    music.play_melody("C5 C C5 C C5 C C5 C ", 120)
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

radio.set_group(1)
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        # . . . #
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        # # . # #
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
""")
basic.show_string("CONNECTED")