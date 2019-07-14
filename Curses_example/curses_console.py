import time
import curses

from maximize_console import maximize_console


def some(n, character):
    stdscr = curses.initscr()
    for x in range(25):
        for y in range(35):
            if not x:
                stdscr.addstr(y, 0, str(y))
            if x == y:
                stdscr.addstr(y, x+n, character)
    stdscr.refresh()
                # time.sleep(0.025)
    return True
    
    
if __name__ == "__main__":
    maximize_console()
    time.sleep(0.1)
    for x in range(35):
        some(x, character='X')
        time.sleep(0.025)
    # stdscr.clear()
    for x in range(35):
        some(x, character='.')
        time.sleep(0.01)
    for x in range(35):
        some(x, character=' ')
        time.sleep(0.01)
        
    # curses.reset_shell_mode()       # return to shell mode
    # print(42)
