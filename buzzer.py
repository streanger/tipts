#!/usr/bin/python3

from gpiozero import Buzzer
from time import sleep
from sys import argv

class buzz:
    def __init__(self, buzzPin, quietMode=False):
        self.pin = buzzPin
        self.buzz = Buzzer(buzzPin)
        self.quietMode = quietMode
    
    def buzz_init(self, buzzPin):
        self.buzz = Buzzer(buzzPin)    

    def quiet(self, mode):
        self.quietMode = mode

    def set_pin(self, newPin):
        self.pin = newPin
        self.buzz = Buzzer(newPin)
   
    def notes_range(self, up=True, duration=250):
        for x in range(1,1000):
            if up:
                beepDelay=x
            else:
                beepDelay=1000-x
            times = int(round(duration/beepDelay))
            beepDelay = round((beepDelay)/1000, 6)
            for y in range(times):
                self.buzz.on()
                sleep(beepDelay)
                self.buzz.off()
                sleep(beepDelay)
            self.buzz.off()
            sleep(0.01) #some delay between notes
    
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
        times = int(round((duration*1000)/(beepDelay*2)))
        beepDelay = round(beepDelay/1000000,6)
        if not self.quietMode:
            print("note:%d| times: %d| beepDelay[ms]:%f" % (notes[note], times, beepDelay))
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
        print("--< title: starwars")
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
                ("fHS", 250),
                
                ("delay", 0.250),

                ("aS", 250),
                ("dHS", 500),
                ("dH", 250),
                ("cHS", 250),
                ("cH", 125),
                ("b", 125),
                ("cH", 250),
                
                ("delay", 0.250),

                ("f", 125),
                ("gS", 500),
                ("f", 375),
                ("a", 125),
                ("cH", 500),

                ("a", 375),
                ("cH", 125),
                ("eH", 1000),
                ("aH", 500),
                ("a", 350),

                ("a", 150),
                ("aH", 500),
                ("gHS", 250),
                ("gH", 250),
                ("fHS", 125),
                ("fH", 125),
                ("fHS", 250),
                
                ("delay", 0.250),

                ("aS", 250),
                ("dHS", 500),
                ("dH", 250),
                ("cHS", 250),
                ("cH", 125),
                ("b", 125),
                ("cH", 250),

                ("delay", 0.250),
                
                ("f", 250),
                ("gS", 500),
                ("f", 375),
                ("cH", 125),
                ("a", 500),
                ("f", 375),
                ("c", 125),
                ("a", 1000)]
    else:
        print("only one song for now :(")

    return song

def play_melody(buzz, song):
    #buzz is buzzer object
    #song is just a two dimension list
    print("--< start a song")
    for note in song:
        if (note[0] == "delay"):
            sleep(note[1])
            continue
        buzz.sound(note[0], note[1])
    print("--< song finished")


if __name__=="__main__":
    args = argv[1:]
    buzz = buzz(12)
    buzz.quiet(False)
    play_melody(buzz, songs())
