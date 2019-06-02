import pyautogui
print(pyautogui.position())
pyautogui.click(80, 113)
pyautogui.dragTo(122, 116, button='left')
pyautogui.hotkey("ctrl", "c")
pyautogui.click(755, 103)
for i in range(0,10000):
	pyautogui.hotkey("ctrl", "v")
	pyautogui.press("space")
