import pyautogui, time



def main():
    colorGris = (60, 60, 60, 255)
    colorRojo = (109, 27, 23, 255)
    colorVerde = (0, 210, 0, 255)
    colorVerdeCero = (0, 144, 0, 255)
    contadorApuesta = 0

    
    s = pyautogui.screenshot()
    pyautogui.moveTo(1061,745)
    time.sleep(0.3) 
    pyautogui.click()
    time.sleep(0.1) 
    pyautogui.click()
    

    while(1):
        s = pyautogui.screenshot()
        if(s.getpixel((1103,438)) != colorVerde):
            for i in range(2,0,-1):
                time.sleep(1)
                print (i)
        elif (s.getpixel((1103,438)) == colorVerde):
            print("color verde detectado")
            #para el color rojo
            if s.getpixel((1325,764)) == colorRojo:
                print("color rojo detectado")
                contadorApuesta = 0
                #mover al boton rojo
                pyautogui.moveTo(1061,745)
                pyautogui.click()
                for i in range(15,0,-1):
                    time.sleep(1)
                    print (i)
                print("contador de apuesta " + str(contadorApuesta) )
                #para los grises
            elif s.getpixel((1325,764)) == colorGris and contadorApuesta < 6:
                print("color gris detectado")
                contadorApuesta = contadorApuesta + 1
                #mover al boton de reapostar
                pyautogui.moveTo(1101,794)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                for i in range(15,0,-1):
                    time.sleep(1)
                    print (i)
                print("contador de apuesta " + str(contadorApuesta) )
            elif s.getpixel((1325,764)) == colorGris and contadorApuesta >= 6:
                print("color gris detectado")
                contadorApuesta = 0
                #mover al boton de reapostar
                pyautogui.moveTo(1061,745)
                time.sleep(0.1)
                pyautogui.click()
                for i in range(15,0,-1):
                    time.sleep(1)
                    print (i)
                print("contador de apuesta " + str(contadorApuesta) )
                #para los ceros
            elif s.getpixel((1325,764)) == colorVerdeCero and contadorApuesta < 6:
                print("CERO detectado")
                contadorApuesta = contadorApuesta + 1
                #mover al boton de reapostar
                pyautogui.moveTo(1101,794)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                for i in range(15,0,-1):
                    time.sleep(1)
                    print (i)
                print("contador de apuesta " + str(contadorApuesta) )
            elif s.getpixel((1325,764)) == colorVerdeCero and contadorApuesta >= 6:
                print("CERO detectado")
                contadorApuesta = 0
                #mover al boton de reapostar
                pyautogui.moveTo(1061,745)
                time.sleep(0.1)
                pyautogui.click()
                for i in range(15,0,-1):
                    time.sleep(1)
                    print (i)
                print("contador de apuesta " + str(contadorApuesta))

                


""" s = pyautogui.screenshot()
    pyautogui.moveTo(1061,745)
    time.sleep(0.3) 
    pyautogui.click()
    time.sleep(0.1) 
    pyautogui.click()

    while(s.getpixel((1103,438)) != colorRojo):
        for i in range(3,0,-1):
            time.sleep(1)
            print (i) """






if __name__ == "__main__":
    main()
