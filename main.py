def on_up_pressed():
    mySprite: Sprite = None
    controller.move_sprite(mySprite)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_button_pressed():
    info.change_score_by(1)
    music.play_melody("E B C5 A B G A F ", 120)
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_a_pressed():
    pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
