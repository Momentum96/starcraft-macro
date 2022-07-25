import keyboard
import mouse
import time
import winsound as sd

key_list = ["q", "w", "e", "a", "s", "d", "z", "x", "c"]
num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def start_beep():
    sd.Beep(1000, 400)
    sd.Beep(1250, 400)
    sd.Beep(1500, 400)

    time.sleep(1)

    sd.Beep(1500, 200)
    sd.Beep(1350, 200)
    sd.Beep(1250, 200)
    sd.Beep(1150, 200)
    sd.Beep(1000, 200)


def unit_produce():
    unit_choice = ""
    while True:
        key = keyboard.read_hotkey(suppress=False)
        if key in key_list:
            time.sleep(0.1)
            unit_choice = key
            break

    for i in num_list:
        keyboard.press_and_release(i)
        time.sleep(0.05)
        keyboard.press_and_release("q")
        time.sleep(0.05)
        keyboard.press_and_release(unit_choice)
        time.sleep(0.05)


def unit_produce_other():
    unit_choice = ""
    while True:
        key = keyboard.read_hotkey(suppress=False)
        if key in key_list:
            time.sleep(0.1)
            unit_choice = key
            break

    for i in num_list:
        keyboard.press_and_release(i)
        time.sleep(0.05)
        keyboard.press_and_release(unit_choice)
        time.sleep(0.05)


def ralley():
    for i in num_list:
        time.sleep(0.05)
        keyboard.press_and_release(i)
        time.sleep(0.05)
        mouse.click("right")


def auto_mouse():
    while True:
        if keyboard.is_pressed("esc"):
            break
        mouse.click("right")
        time.sleep(0.1)


def diss():
    while True:
        if keyboard.is_pressed("esc"):
            break
        mouse.click("left")


def main():
    start_beep()
    print("=" * 20)
    print("생컨버전")
    print("1번 단축키 : 생산(저그)")
    print("2번 단축키 : 생산(다른 종족)")
    print("3번 단축키 : 랠리")
    print("4번 단축키 : 오토마우스")
    print("0번 단축키 : 디스")
    print("=" * 20)

    while True:
        if keyboard.is_pressed("ctrl+shift+1"):
            print("1번 단축키 : 생산(저그)")
            unit_produce()
        elif keyboard.is_pressed("ctrl+shift+2"):
            print("2번 단축키 : 생산(다른 종족)")
            unit_produce_other()
        elif keyboard.is_pressed("ctrl+shift+3"):
            print("3번 단축키 : 랠리")
            ralley()
        elif keyboard.is_pressed("ctrl+shift+4"):
            print("4번 단축키 : 오토마우스")
            auto_mouse()
        elif keyboard.is_pressed("ctrl+shift+0"):
            print("0번 단축키 : 디스")
            time.sleep(0.2)
            diss()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
