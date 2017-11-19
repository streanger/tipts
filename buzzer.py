
#!/bin/python
#run with python3

from gpiozero import Buzzer
from time import sleep
from sys import argv

class buzz:
    def __init__(self, buzzPin):
        self.pin = buzzPin
        self.buzz = Buzzer(buzzPin)
    
    def buzz_init(self, buzzPin):
        self.buzz = Buzzer(buzzPin)    

    def set_pin(self, newPin):
        self.pin = newPin
        self.buzz = Buzzer(newPin)
   
    def sound(self, note, duration):
        #notes etc
        notePairs = [['cL', 129], ['cLS', 139],
                     ['dL', 146], ['dLS', 156],
                     ['eL', 163], ['fL', 173],
                     ['fLS', 185], ['gL', 194],
                     ['gLS', 207], ['aL', 219],
                     ['aLS', 228], ['bL', 232],
                     ['c', 261], ['cS', 277],
                     ['d', 294], ['dS', 311],
                     ['e', 329], ['f', 349],
                     ['fS', 370], ['g', 391], 
                     ['gS', 415], ['a', 440],
                     ['aS', 455], ['b', 466],
                     ['cH', 523], ['cHS', 554],
                     ['dH', 587], ['dHS', 622],
                     ['eH', 659], ['fH', 698],
                     ['fHS', 740], ['gH', 784],
                     ['gHS', 830], ['aH', 880],
                     ['aHS', 910], ['bH', 933]]
        notes = dict(notePairs)
        beepDelay = round((1000000/notes[note]))  #in miliseconds
        times = round((duration*1000)/(beepDelay*2))
        beepDelay = round(beepDelay/1000000,5)
        print("note:", notes[note])
        print("times:", times)
        print("beepDelay:", beepDelay)
        for x in range(times):
            self.buzz.on()
            sleep(beepDelay)
            self.buzz.off()
            sleep(beepDelay)            
        #some delay between notes
        self.buzz.off()
        sleep(0.020)

    def play_buzzer(self):
        print("beep!")
        self.buzz.toggle()
        duration = 1/12
        sleep(duration)
        print(duration)
        self.buzz.toggle()
def songs(title="starwars"):
    if title == "starwars":
        print("starwars")
        song = [("a", 500),
                ("a", 500),
                ("f", 350),
                ("cH", 150),

                ("a", 500),
                ("f", 350),
                ("cH", 150),
                ("a", 1000),
                ("eH", 500),                

                ("eH", 500),
                ("eH", 500),
                ("fH", 350),
                ("cH", 150),
                ("gS", 500),

                ("f", 350),
                ("cH", 150),
                ("a", 1000),
                ("aH", 500),
                ("a", 350),

                ("a", 150),
                ("aH", 500),
                ("gHS", 250),
                ("gH", 250),
                ("fHS", 125),
                ("fH", 125),
                ("fHS", 250)]

    else:
        print("only one song for now :(")

    return song

def play_melody(buzz, song):
    #buzz is buzzer object
    #song is just a two dimension list
    print("start a song")
    for note in song:
        buzz.sound(note[0], note[1])
    print("song finished")        
    
#args = argv[1:]
#print(args)

buzz = buzz(12)
play_melody(buzz, songs())

