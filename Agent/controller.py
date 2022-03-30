import pyautogui,string,time,random
pyautogui.FAILSAFE = False
class Controller:
    def __init__(self):
        pass
    def process(self,input):
        alpha = input[:26]
        x_pos = input[27] * pyautogui.size()[0]
        y_pos = input[28] * pyautogui.size()[1]
        if  input[29] > 0:
            self.click(x_pos,y_pos)
        if input[30] > 0:
            self.type(alpha)

    def click(self,x,y):
        pyautogui.moveTo(x, y)
        pyautogui.click()
    
    def type(self,inputs):
        max_value = max(inputs)
        max_index = inputs.index(max_value)
        char = string.ascii_lowercase[max_index]
        print(char)
        time.sleep(1)
        pyautogui.typewrite(char)
    

