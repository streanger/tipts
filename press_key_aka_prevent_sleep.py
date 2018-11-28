# press F15 key, what prevents sleep
# contains also 'move_mouse' function
import win32api
from time import sleep
import re
from sys import argv

def move_mouse(direction=True):
    try:
        pos = win32api.GetCursorPos()   #actual position
    except:
        return False
    if direction:
        new_pos = (pos[0]+1, pos[1]+1)
    else:
        new_pos = (pos[0]-1, pos[1]-1)
    win32api.SetCursorPos(new_pos)
    return new_pos

def press_key(key="F15"):
    #keys = https://gist.github.com/chriskiehl/2906125
    keys = {"F15":0x7E,
            'F1':0x70,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87}
    val = keys[key]
    win32api.keybd_event(val, 0, 0, 0)

def main():
    minutes = re.findall(r'\d+', argv[0])
    if minutes:
        minutes = int(minutes[0])
    else:
        minutes = 5
    interval = 60*minutes      #60*5
    direction = True
    while True:
        press_key("F15")
        #currentPos = move_mouse(direction)
        #direction = not direction
        sleep(interval)
        
if __name__ == "__main__":
    main()

