controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    let mySprite: Sprite = null
    controller.moveSprite(mySprite)
})
controller.anyButton.onEvent(ControllerButtonEvent.Pressed, function () {
    info.changeScoreBy(1)
    music.playMelody("E B C5 A B G A F ", 120)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
	
})
