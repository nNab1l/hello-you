from microbit import *

import audio

timer = 0
face = Image("00000:"
"09090:"
"00900:"
"09090:"
"00000:")

display.show(face)
audio.play(Sound.HELLO)



while True:
    if button_a.is_pressed():
        timer = 0 
        display.scroll("Hi!")
        sleep(500)
        display.show(face)
    
    
    
    if pin_logo.is_touched():
        timer = 0
        happy = Image("00000:"
                    "09090:"
                    "00000:"
                    "90909:"
                    "09090:")
        display.show(happy)
        audio.play(Sound.HAPPY)
    elif accelerometer.was_gesture('shake'):
        timer = 0
        shake = Image("00000:"
                    "90009:"
                    "09090:"
                    "90009:"
                    "00900:")
        display.show(shake)
        audio.play(Sound.GIGGLE)
    else:
        sleep(500)
        timer += 0.5
        
        
        if timer == 20:
            sad = Image("00000:"
                        "09090:"
                        "09090:"
                        "00900:"
                        "09090:")
            display.show(sad)
            audio.play(Sound.SAD)
        elif timer == 30:
            sleepy = Image("00000:"
                        "00000:"
                        "99099:"
                        "00900:"
                        "00000:")
            display.show(sleepy)
            audio.play(Sound.YAWN)
        elif timer == 36:
              display.scroll("ZZZ..")
        
        
        elif timer == 40:
            audio.play(Sound.MYSTERIOUS)
            display.scroll("Game Over")
            display.scroll("press A to restart")
            