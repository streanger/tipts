import sys
import os
import sounddevice as sd
from scipy.io.wavfile import write


def script_path():
    '''change dir, to current script path'''
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def record_external_sound(seconds=10, out='external_sound.wav'):
    '''record sound from microphone
        -seconds    - Duration of recording
        -out        - file to write
    doc:
        https://python-sounddevice.readthedocs.io/en/0.4.0/usage.html#recording
    info:
        sd.query_devices():
            shows list of devices
        sd.default.device:
            depends on system and physicall devices
        sd.wait:
            If the recording was already finished, this returns immediately
            if not, it waits and returns as soon as the recording is finished
    '''
    print('in progress... ')
    sd.default.device = [1, 3]      # (1) microphone; (3) glosniki
    fs = 44100      # Sample rate
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()       # Wait until recording is finished
    write(out, fs, myrecording)     # Save as WAV file 
    return None
    
    
def record_system_sound(seconds=10, out='system_sound.wav'):
    '''record sound from system
        -seconds    - Duration of recording
        -out        - file to write
    doc:
        https://python-sounddevice.readthedocs.io/en/0.4.0/usage.html#recording
    info:
        sd.query_devices():
            shows list of devices
        sd.default.device:
            depends on system and physicall devices
        sd.wait:
            If the recording was already finished, this returns immediately
            if not, it waits and returns as soon as the recording is finished
    '''
    print('in progress... ')
    sd.default.device = [12, 3]      # (12) Miks stereo; (3) speakers
    
    fs = 44100      # Sample rate
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()       # Wait until recording is finished
    write(out, fs, myrecording)     # Save as WAV file 
    return None
    
    
if __name__ == "__main__":
    script_path()
    record_external_sound(seconds=5, out='external_sound.wav')
    record_system_sound(seconds=15, out='system_sound.wav')
    
    
'''
devices info:
>>> sd.query_devices()
       0 Mapowanie dźwięku Microsoft - Input, MME (2 in, 0 out)
    >  1 Mikrofon (Conexant SmartAudio H, MME (2 in, 0 out)
       2 Mapowanie dźwięku Microsoft - Output, MME (0 in, 2 out)
    <  3 Głośniki (Conexant SmartAudio H, MME (0 in, 2 out)
       4 Podstawowy sterownik przechwytywania dźwięku, Windows DirectSound (2 in, 0 out)
       5 Mikrofon (Conexant SmartAudio HD), Windows DirectSound (2 in, 0 out)
       6 Podstawowy sterownik dźwięku, Windows DirectSound (0 in, 2 out)
       7 Głośniki (Conexant SmartAudio HD), Windows DirectSound (0 in, 2 out)
       8 Głośniki (Conexant SmartAudio HD), Windows WASAPI (0 in, 2 out)
       9 Mikrofon (Conexant SmartAudio HD), Windows WASAPI (2 in, 0 out)
      10 Mikrofon (Conexant HD Audio capture), Windows WDM-KS (2 in, 0 out)
      11 Speakers (Conexant HD Audio output), Windows WDM-KS (0 in, 2 out)
      12 Miks stereo (Conexant HD Stereo Mix), Windows WDM-KS (2 in, 0 out)
      13 Output (Audio dla wyświetlaczy Intel(R) 1), Windows WDM-KS (0 in, 2 out)
      
sd.default.device -> [1, 3]

'''
