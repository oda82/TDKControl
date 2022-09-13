##import tkinter as tk
##from tkinter import ttk

import serial
from serial.tools.list_ports import comports

import time

class TDK_Model:
    def __init__(self, ctrl=None):
        self.ctrl = ctrl #pointer to controler
        self.port = None
#-----port commands
    def scan_port(self):
        '''Просканировать все ком порты'''
        self.ports =  [port.device for port in comports()]

    def open_port(self, port='/dev/ttyUSB0'):
        ''' open port for work'''
        self.port = serial.Serial(port = port, baudrate=9600, timeout=0.1)

    def close_port(self):
        ''' close port '''
        self.port.close()
        self.port = None

    def read_answer(self):
        ''' read data from port'''
        if self.port.is_open():
            read_bytes = bytearray()
            while True:
                read_byte = self.port.read()
                if read_byte == '\r' or len(read_byte) == 0:
                    return read_bytes.decode('utf-8')
                else:
                    read_bytes.append(ord(read_byte))

    def send_command(self, com):
        ''' send command and read answer'''
        if self.port.is_open():
            print(com, str( self.port.write(bytearray(com+'\r', 'utf-8')) ))
            return read_answer()
        
#--------simple TDK commands--------------
#        start command stop
#-----------------------------------------

    def start(self):
        self.send_command('ADR 06') #choose the supply
        self.send_command('OUT 1') #activete out

    def stop(self):
        self.send_command('PC 0.0')#set current
        self.send_command('OUT 0') #activete out
    
    def read_v(self):
        return send_command('MV?')
    
    def read_i(self):
        return send_command('MC?')

#-------compound TDK cmmands----------------------------
    
    def ramp(self, min_i, max_i, t1 = 1, step_time = 0.1):
        assert points > 2
        points = t1 // step_time
        steps = (max_i-min_i) / (points - 1)
        begin_I = ['PC {:0.2f}'.format(min_i + steps * i) for i in range(points)]
        print(begin_I)
        for i in begin_I:
            send_command(i)
            #print(str(i)+'\r')
            time.sleep(step_time)

    def cicle_clear(self, cicle_num, min_i=0.1, max_i=2, t1 = 10, t2 = 100):
        for i in range(cicle_num):
            self.ramp(min_i,max_i)
            time.sleep(t1)
            self.ramp(max_i,min_i)
            time.sleep(t2)

    def last_clear(self, min_i = 0.1, max_i = 2, t1 = 30, t2 = 200):
        ramp(min_i,max_i)
        time.sleep(t1)
        ramp(max_i,min_i, t2)


if __name__ == '__main__':
    pass
    
    
    # print(send_command('PC 5.0'))#set current

    # cicle_clear(5, 0.1, 7.5)
    # last_clear(0.1,8.2)

    # print(send_command('PC 0.1'))#set current
    # ramp(0.1, 6.0, 10)
    # time.sleep(40)
    # ramp(6.0, 0.1, 10)
    # for i in range(60):
    #     print(i)
    #     time.sleep(60)
     
    #tdk.close()

    # print(send_command('IDN?'))
    # print(send_command('REV?'))
    # print(send_command('SN?'))
    # print(send_command('DATE?'))

    # print(send_command('PV?'))
    # print(send_command('MV?'))
    # print(send_command('PC?'))
    # print(send_command('MC?'))
    # 
    # print(send_command('DVC?'))
    # time.sleep(3)
    # print(send_command('OUT 0'))

