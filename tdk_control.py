import serial
from serial.tools.list_ports import comports


import time
from time import sleep
from threading import Thread

import tdk_model
import tdk_view

class TDK_Controll:
    def __init__(self, model, view):
        #подключение моделей устройств
        self.model = model
        #подключение отображений
        self.view = view 
        #связать управление в отображении
        self.bind_view()
    
    def bind_view(self):
        pass
        
    
    
if __name__ == '__main__':
    pass
