def แขนลง():
    PTKidsBIT.servo_write2(Servo_Write2.S0, 93)
def เลี้ยวซ้าย_90():
    PTKidsBIT.turn_line(Turn_Line.LEFT, 100, 2, 200, 20)
    PTKidsBIT.forward_time(Forward_Direction.FORWARD, 100, 0, 100, 0.06, 0.2)
def วางกระป๋อง():
    PTKidsBIT.servo_write2(Servo_Write2.S0, 93)
    basic.pause(200)
    PTKidsBIT.servo_write2(Servo_Write2.S1, 175)
    basic.pause(200)
    PTKidsBIT.servo_write2(Servo_Write2.S0, 180)
    basic.pause(200)

def on_button_pressed_a():
    PTKidsBIT.motor_go(50, 50)
    basic.pause(500)
    PTKidsBIT.forward_line(Forward_Direction.FORWARD,
        Find_Line.CENTER,
        100,
        100,
        20,
        0.06,
        0.2)
    for index in range(1):
        เซนเซอร์ล้อจอด()
        PTKidsBIT.forward_line(Forward_Direction.FORWARD,
            Find_Line.CENTER,
            50,
            100,
            20,
            0.06,
            0)
        PTKidsBIT.forward_line(Forward_Direction.FORWARD,
            Find_Line.CENTER,
            50,
            100,
            20,
            0.06,
            0)
        เลี้ยวซ้าย_90()
        PTKidsBIT.forward_time(Forward_Direction.FORWARD, 2000, 50, 100, 0.06, 0.2)
        แขนลง()
        PTKidsBIT.forward_line(Forward_Direction.FORWARD,
            Find_Line.CENTER,
            50,
            100,
            40,
            0.04,
            0)
        เซนเซอร์ล้อจอด()
        คีบยก()
        เลี้ยวขวา_90()
        เลี้ยวขวา_90()
        PTKidsBIT.forward_time(Forward_Direction.FORWARD, 2600, 100, 100, 0.06, 0.2)
        PTKidsBIT.forward_line(Forward_Direction.FORWARD,
            Find_Line.CENTER,
            50,
            100,
            20,
            0.04,
            0)
        เซนเซอร์ล้อจอด()
        วางกระป๋อง()
        เลี้ยวซ้าย_90()
        เลี้ยวซ้าย_90()
        PTKidsBIT.forward_time(Forward_Direction.FORWARD, 2000, 50, 100, 0.06, 0.2)
        PTKidsBIT.forward_line(Forward_Direction.FORWARD,
            Find_Line.CENTER,
            50,
            100,
            20,
            0.04,
            0)
        เซนเซอร์ล้อจอด()
        เลี้ยวขวา_90()
        PTKidsBIT.forward_time(Forward_Direction.FORWARD, 1000, 50, 100, 0.06, 0.2)
        PTKidsBIT.forward_line(Forward_Direction.FORWARD,
            Find_Line.CENTER,
            50,
            100,
            20,
            0.04,
            0)
    แขนลง()
    PTKidsBIT.forward_line(Forward_Direction.FORWARD,
        Find_Line.CENTER,
        50,
        100,
        20,
        0.04,
        0)
    เซนเซอร์ล้อจอด()
    คีบยก()
    เลี้ยวซ้าย_90()
    เลี้ยวซ้าย_90()
    PTKidsBIT.forward_time(Forward_Direction.FORWARD, 2000, 100, 100, 0.06, 0.2)
    PTKidsBIT.forward_line(Forward_Direction.FORWARD,
        Find_Line.CENTER,
        100,
        100,
        20,
        0.04,
        0)
    PTKidsBIT.forward_line(Forward_Direction.FORWARD,
        Find_Line.CENTER,
        100,
        100,
        20,
        0.04,
        0)
    เซนเซอร์ล้อจอด()
    แขนลง()
    วางกระป๋อง()
input.on_button_pressed(Button.A, on_button_pressed_a)

def คีบยก():
    PTKidsBIT.servo_write2(Servo_Write2.S1, 117)
    basic.pause(200)
    PTKidsBIT.servo_write2(Servo_Write2.S0, 180)
    basic.pause(200)
def เซนเซอร์หน้าจอด():
    PTKidsBIT.line_sensor_set([0, 1, 2, 3, 4, 5], [0], [5], LED_Pin.DISABLE)
    PTKidsBIT.value_sensor_set([39, 39, 37, 40, 37, 37],
        [18],
        [26],
        [119, 144, 133, 141, 109, 134],
        [67],
        [70])
def เซนเซอร์ล้อจอด():
    PTKidsBIT.line_sensor_set([0, 1, 2, 3, 4, 5], [6], [7], LED_Pin.DISABLE)
    PTKidsBIT.value_sensor_set([39, 39, 37, 40, 37, 37],
        [18],
        [26],
        [119, 144, 133, 141, 109, 134],
        [67],
        [70])

def on_gesture_logo_down():
    basic.show_icon(IconNames.HEART)
    PTKidsBIT.servo_write2(Servo_Write2.S0, 80)
    basic.pause(200)
    PTKidsBIT.servo_write2(Servo_Write2.S1, 110)
    basic.pause(200)
    PTKidsBIT.servo_write2(Servo_Write2.S0, 165)
    basic.pause(200)
    PTKidsBIT.servo_write2(Servo_Write2.S1, 110)
    basic.pause(200)
    for index2 in range(10):
        PTKidsBIT.servo_write2(Servo_Write2.S0, 165)
        basic.pause(150)
        PTKidsBIT.servo_write2(Servo_Write2.S0, 80)
        basic.pause(150)
    PTKidsBIT.servo_write2(Servo_Write2.S0, 165)
    basic.pause(200)
    PTKidsBIT.servo_write2(Servo_Write2.S1, 170)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def เลี้ยวขวา_90():
    PTKidsBIT.turn_line(Turn_Line.RIGHT, 100, 3, 200, 20)
    PTKidsBIT.forward_time(Forward_Direction.FORWARD, 100, 0, 100, 0.06, 0.2)
PTKidsBIT.line_sensor_set([0, 1, 2, 3, 4, 5], [6], [7], LED_Pin.DISABLE)
PTKidsBIT.servo_write2(Servo_Write2.S0, 180)
basic.pause(200)
PTKidsBIT.servo_write2(Servo_Write2.S1, 175)
basic.pause(200)
PTKidsBIT.value_sensor_set([39, 39, 37, 40, 37, 37],
    [18],
    [26],
    [119, 144, 133, 141, 109, 134],
    [67],
    [70])

def on_forever():
    PTKidsBIT.print_sensor_value()
    basic.pause(500)
basic.forever(on_forever)
