import pyautogui, time



def main():
	colorRojo = (154, 34, 28, 255)
	colorNegro = (37, 36, 37, 255)
	colorVerde = (0,161,107,255)
	colorVerdeTapete = (62,80,71,255)
	contadorApuesta = 0


	s = pyautogui.screenshot()
	pyautogui.moveTo(992,590)
	time.sleep(0.3)
	pyautogui.click()
	time.sleep(0.1)
	pyautogui.click()
	pyautogui.moveTo(1357,673)
	time.sleep(0.3)
	pyautogui.click()




	while(1):
		s = pyautogui.screenshot()
		if((s.getpixel((1166,397)) != colorVerde) and (s.getpixel((1166,397)) != colorNegro) and (s.getpixel((1166,397)) != colorRojo) ):
			for i in range(2,0,-1):
				#time.sleep(1)
				print (i)
		elif((s.getpixel((1166,397)) == colorVerde) or (s.getpixel((1166,397)) == colorNegro) or (s.getpixel((1166,397)) == colorRojo) ):
			print("color detectado")
			#para el color rojo
			if s.getpixel((1166,397)) == colorRojo:
				print("color rojo detectado")
				contadorApuesta = 0
				#aqui se mueve a borrar y apostar de nuevo
				time.sleep(6)
				pyautogui.moveTo(1200,659)
				time.sleep(0.3)
				pyautogui.click()
				time.sleep(0.3)
				pyautogui.moveTo(992,590)
				time.sleep(0.3)
				pyautogui.click()
				pyautogui.moveTo(1355,661)
				time.sleep(0.3)
				pyautogui.click()
				print("contador de apuesta " + str(contadorApuesta) )
				#para el color negro
			elif s.getpixel((1166,397)) == colorNegro and contadorApuesta < 9:
				print("color negro detectado")
				contadorApuesta = contadorApuesta + 1
				#para seguir apostando
				time.sleep(6)
				pyautogui.moveTo(961,658)
				time.sleep(0.3)
				pyautogui.click()
				pyautogui.moveTo(1355,661)
				time.sleep(0.3)
				pyautogui.click()
				print("contador de apuesta " + str(contadorApuesta) )
			elif s.getpixel((1166,397)) == colorNegro and contadorApuesta >= 9:
				print("color negro detectado")
				contadorApuesta = 0
				time.sleep(6)
				pyautogui.moveTo(1200,659)
				time.sleep(0.3)
				pyautogui.click()
				time.sleep(0.3)
				pyautogui.moveTo(992,590)
				time.sleep(0.3)
				pyautogui.click()
				pyautogui.moveTo(1355,661)
				time.sleep(0.3)
				pyautogui.click()
				print("contador de apuesta " + str(contadorApuesta) )
			elif s.getpixel((1166,397)) == colorVerde and contadorApuesta < 9:
				print("color verde detectado")
				contadorApuesta = contadorApuesta + 1
				#para seguir apostando
				time.sleep(6)
				pyautogui.moveTo(961,658)
				time.sleep(0.3)
				pyautogui.click()
				pyautogui.moveTo(1355,661)
				time.sleep(0.3)
				pyautogui.click()
				print("contador de apuesta " + str(contadorApuesta) )
			elif s.getpixel((1166,397)) == colorVerde and contadorApuesta >= 9:
				print("color verde detectado")
				contadorApuesta = 0
				time.sleep(6)
				pyautogui.moveTo(1200,659)
				time.sleep(0.3)
				pyautogui.click()
				time.sleep(0.3)
				pyautogui.moveTo(992,590)
				time.sleep(0.3)
				pyautogui.click()
				pyautogui.moveTo(1355,661)
				time.sleep(0.3)
				pyautogui.click()
				print("contador de apuesta " + str(contadorApuesta) )







if __name__ == "__main__":
    main()





