import pyautogui, time



def main():
    
    
    colorGris = (60, 60, 60, 255)
    colorRojo = (109, 27, 23, 255)

    contadorApuesta = 0

    



    s = pyautogui.screenshot()
    #print(s.getpixel((1322, 766)))
    pyautogui.moveTo(1061,745)
    time.sleep(0.3) 
    pyautogui.click()
    time.sleep(0.1) 
    pyautogui.click()

    #tiempo de espera del resultado de la ruleta
    print ('tasks done, now sleeping for 10 seconds')
    for i in range(44,0,-1):
        time.sleep(1)
        print (i)
    
    print("time over")


    pyautogui.moveTo((1325,764))
    

    while(1):
        if contadorApuesta < 4 :

            if s.getpixel((1325,764)) == colorRojo:   
                contadorApuesta = 0
                print ("color rojo")
                #mover al boton rojo
                pyautogui.moveTo(1061,745)
                pyautogui.click()
                print("contador de apuesta " + str(contadorApuesta) )
                for i in range(46,0,-1):
                    time.sleep(1)
                    print (i)
                print("time over")

            elif s.getpixel((1325,764)) == colorGris:
                contadorApuesta = contadorApuesta + 1
                print ("color gris")
                #mover al boton de reapostar
                pyautogui.moveTo(1101,794)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                print("contador de apuesta " + str(contadorApuesta) )
                for i in range(46,0,-1):
                    time.sleep(1)
                    print (i)
                print("time over")

            else:
                contadorApuesta = contadorApuesta + 1
                print("no se encontr'o color")
                """ print ("color gris")
                #mover al boton de reapostar
                pyautogui.moveTo(1101,794)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                print("contador de apuesta " + contadorApuesta )
                time.sleep(46) """
        elif contadorApuesta == 4 or contadorApuesta > 4 :
            contadorApuesta = 0



if __name__ == "__main__":
    main()
    
