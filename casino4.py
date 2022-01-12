import pyautogui,time


def main():
	s = pyautogui.screenshot()
	pyautogui.moveTo(992,590)
	time.sleep(0.3)
	pyautogui.click()
	time.sleep(0.1)
	pyautogui.moveTo(1354,655)
	pyautogui.click()
	while(1):

		
		for i in range(2,0,-1):
			#time.sleep(1)
			print (i)
		time.sleep(30)
		pyautogui.moveTo(1354,655)
		pyautogui.click()
		




if __name__ == "__main__":
    main()


