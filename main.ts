input.onGesture(Gesture.EightG, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onGesture(Gesture.FreeFall, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onGesture(Gesture.LogoUp, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onGesture(Gesture.TiltLeft, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onGesture(Gesture.SixG, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onGesture(Gesture.ScreenUp, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onGesture(Gesture.ScreenDown, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onGesture(Gesture.Shake, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onGesture(Gesture.TiltRight, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onGesture(Gesture.LogoDown, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
input.onGesture(Gesture.ThreeG, function () {
    radio.sendString("INTRUDER!")
    music.playMelody("C5 C C5 C C5 C C5 C ", 120)
})
radio.setGroup(1)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    # . . . #
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    # # . # #
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    `)
basic.showString("CONNECTED")
