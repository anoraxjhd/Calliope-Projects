def on_button_a():
    global x2
    PlayerUpdatePixels(x2, y2)
    x2 += -1
    PlayerUpdatePixels(x2, y2)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    global x2
    PlayerUpdatePixels(x2, y2)
    x2 += 1
    PlayerUpdatePixels(x2, y2)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def PlayerUpdatePixels(x: number, y: number):
    led.toggle(x, y)
def ChangeEnemyPosition(xpos: number, ypos: number):
    global Enemy_1_Y, Score, Enemy_1_X, GameTime
    led.unplot(Enemy_1_X, Enemy_1_Y)
    Enemy_1_Y += 1
    if not (Enemy_1_X == x2 and Enemy_1_Y == y2):
        led.toggle(Enemy_1_X, Enemy_1_Y)
    else:
        Score += 1
        Enemy_1_X = randint(0, 4)
        Enemy_1_Y = -1
        if GameTime > 0.2:
            GameTime = GameTime - 0.1
Score = 0
Enemy_1_Y = 0
Enemy_1_X = 0
y2 = 0
x2 = 0
GameTime = 0
led.toggle(2, 4)
GameTime = 1
x2 = 2
y2 = 4
Enemy_1_X = randint(0, 4)
Enemy_1_Y = -1

def on_forever():
    global Score
    if Enemy_1_Y >= 5:
        Score += 1
    if Score == 10:
        basic.set_led_color(basic.rgb(0, 255, 0))
        basic.show_string("Gewonnen!")
        control.reset()
    if Enemy_1_Y >= 5:
        basic.set_led_color(basic.rgb(255, 0, 0))
        basic.show_string("Verloren!")
        control.reset()
basic.forever(on_forever)

def on_forever2():
    basic.pause(GameTime * 1000)
    ChangeEnemyPosition(Enemy_1_X, Enemy_1_Y)
basic.forever(on_forever2)
