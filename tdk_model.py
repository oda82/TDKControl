##import tkinter as tk
##from tkinter import ttk

import serial
import time

tdk = serial.Serial(port = '/dev/ttyUSB0', baudrate=9600, timeout=0.1)

def read_answer():
    read_bytes = bytearray()
    while True:
        read_byte = tdk.read()
        if read_byte == '\r' or len(read_byte) ==0:
            return read_bytes.decode('utf-8')
        else:
            read_bytes.append(ord(read_byte))

def send_command(com):
    print(com, str( tdk.write(bytearray(com+'\r', 'utf-8')) ))
    #time.sleep(0.1)
    #return tdk.readline()
    return read_answer()

def ramp(min_i, max_i, points, sleep_time=0.1):
    assert points>2
    steps = (max_i-min_i)/(points-1)
    begin_I = ['PC {:0.2f}'.format(min_i + steps*i) for i in range(points)]
    print(begin_I)
    for i in begin_I:
        send_command(i)
        #print(str(i)+'\r')
        time.sleep(sleep_time)

def cicle_clear(cicle_num, min_i=0.1, max_i=8.3):
    for i in range(cicle_num):
        ramp(min_i,max_i, 10)
        time.sleep(30)
        ramp(max_i,min_i, 10)
        time.sleep(120)
    pass

def last_clear(min_i=0.1, max_i=8.3):
    ramp(min_i,max_i, 10)
    time.sleep(20)
    ramp(max_i,min_i, 200)
    pass

if __name__ == '__main__':
    
    print(send_command('ADR 06')) #choose the supply
    print(send_command('OUT 1')) #activete out

    print(send_command('PC 0.11'))#set current
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
    # 
    print(send_command('PC 0.0'))#set current
    print(send_command('OUT 0')) #activete out

    tdk.close()

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

