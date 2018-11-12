#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
"""
20180702可以讀取、開啟、關閉電力插座的函式
201807021753解決讀取錯誤的狀況，將開機指令與讀取另的時間格0.5秒，並將原本的data的最小由零改為17
"""
import serial
import datetime
import time

def REP(seand1, Bd):#Modbus RTU CRC:"\x08\x03\x00\x48\x00\x06\x45\x47",Baud:9600
    data=[100.00]
    ser = serial.Serial ("/dev/ttyAMA0")    #Open named port
    ser.flushInput()
    ser.baudrate = Bd
    ser.write(seand1)
    ser.timeout = 0.5
    ser.writeTimeout = 0.5
    data = ser.read(17)
    if len(data) < 17:
        ser.write(seand1)
    else:
        try:
            print '%x' % ord(data[0]),'%x' % ord(data[1]),'%x' % ord(data[2]),'%x' % ord(data[3]),'%x' % ord(data[4]),'%x' % ord(data[5]),'%x' % ord(data[6]),'%x' % ord(data[7]),'%x' % ord(data[8]),'%x' % ord(data[9]),'%x' % ord(data[10]),'%x' % ord(data[11]),'%x' % ord(data[12]),'%x' % ord(data[13]),'%x' % ord(data[14]),'%x' % ord(data[15]),'%x' % ord(data[16])
        except:
            print "讀取錯誤"

        else:
            V = ((ord(data[3])*256)+(ord(data[4]))*1.0)/100
            I = ((ord(data[5])*256)+(ord(data[6]))*1.0)/1000
            P = ((ord(data[7])*256)+(ord(data[8]))*1.0)
            aaa = V * I
            PT = ((ord(data[9])*20.48)+(ord(data[10])*1.28)+(ord(data[11])*0.08)+(ord(data[12])*0.0003125))/3200
            PF = ((ord(data[13])*256)+(ord(data[14]))*1.0)/1000
            date =  time.strftime("%Y/%m/%d %H:%M:%S")
            d = datetime.datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
            date1 = time.mktime(d.timetuple()) + 1e-6 * d.microsecond
            print date
            print "V=" ' %f' % V
            print "I =" ' %f' % I
            print "P=" ' %f' % P
            print aaa
            print "PT =" ' %f' % PT
            print "PF =" ' %f' % PF
            listREP = [date1, V, I, P, PT, PF]
            ser.close()
            return listREP

def ShutdownPower(seand1, Bd):
    data=[100.00]
    ser = serial.Serial ("/dev/ttyAMA0")
    ser.flushInput()
    ser.baudrate = Bd                      #Set baud rate to 9600
    ser.write(seand1)
    ser.close()
    print "Power Shutdonw"

def BootPower(seand1, Bd):
    data=[100.00]
    ser = serial.Serial ("/dev/ttyAMA0")
    ser.flushInput()
    ser.baudrate = Bd                      #Set baud rate to 9600
    ser.write(seand1)
    ser.close()
    print "Power Boot"
