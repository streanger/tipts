''' example from Al Sweigart book '''
import traceback

try:
    raise Exception("this is very error")
except:
    file = open("info.txt", "w")
    file.write(traceback.format_exc())
    file.close()
    print("info was saved to file")
