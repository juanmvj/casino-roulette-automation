import pyautogui, time



def main():
    while(1):
        s = pyautogui.screenshot()
        print(s.getpixel((1166,397)))
        



if __name__ == "__main__":
    main()


   