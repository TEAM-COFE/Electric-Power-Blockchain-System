#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
import serial
import time
import MySQLdb
import datetime
import PowerSocket
import DataBase
from Tkinter import *

class AAA:
    def __init__(self):

        win = Tk()#使用Tk()
        win.title("MySQL")

        hostrow, userrow, passwordrow, databaserow, tablerow, crcrow, connectrow = 1, 2, 3, 4, 5, 6, 7#設定列

        #Host:欄位程式碼
        host = Label(win, text = "Host: ")#在win建立(標籤)Label，輸出文字為"Host:"
        self.hostname = StringVar()
        hostentry = Entry(win, textvariable = self.hostname)#在win建立項目(Entry)並將字串存入self.hostname
        host.grid(row = hostrow, column = 1)#設定標籤(Label)位置在第一列第一欄
        hostentry.grid(row = hostrow, column = 2)#設定項目(Entry)位置在第一列第二欄

        #User:欄位程式碼
        user = Label(win, text = "User: ")
        self.username = StringVar()
        userentryName = Entry(win, textvariable = self.username)
        user.grid(row = userrow, column = 1)
        userentryName.grid(row = userrow, column = 2)

        #Password:欄位程式碼
        password = Label(win, text = "Password: ")
        self.passwordname = StringVar()
        userentryName = Entry(win, textvariable = self.passwordname)
        password.grid(row = passwordrow, column = 1)
        userentryName.grid(row = passwordrow, column = 2)

        #DataBase:欄位程式碼
        database = Label(win, text = "DataBase: ")
        self.databasename = StringVar()
        databaseentryName = Entry(win, textvariable = self.databasename)
        database.grid(row = databaserow, column = 1)
        databaseentryName.grid(row = databaserow, column = 2)

        #Table:欄位程式碼
        """table = Label(win, text = "Table: ")
        self.tablename = StringVar()
        tableName = Entry(win, textvariable = self.tablename)
        table.grid(row = tablerow, column = 1)
        tableName.grid(row = tablerow, column = 2)"""

        #Table:欄位程式碼
        crc = Label(win, text = "CRC: ")
        self.crcname = StringVar()
        crcName = Entry(win, textvariable = self.crcname)
        crc.grid(row = crcrow, column = 1)
        crcName.grid(row = crcrow, column = 2)

        #連線按鈕的程式碼
        connect = Button(win, text = "連線",command = self.CheckButton)#在win建立按鈕，並在上顯示"連線"，當如果動作呼叫AAA()類別的CheckButton()物件
        connect.grid(row = connectrow, column = 1)

        win.mainloop()

    def CheckButton(self):
        CheckTable1, CheckTable2, CheckTable3, host, user, passwd, datebase = "auto", "MachineLearning", "status", self.hostname.get(), self.username.get(), self.passwordname.get(), self.databasename.get()
        db = MySQLdb.connect(host, user, passwd, datebase, charset="utf8")
        CheckTableName1, CheckTableValue1 = DataBase.CheckTable(CheckTable1, db)
        CheckTableName2, CheckTableValue2 = DataBase.CheckTable(CheckTable2, db)
        CheckTableName3, CheckTableValue3 = DataBase.CheckTable(CheckTable3, db)
        if CheckTableValue1 == 1 and CheckTableValue2 == 1 and CheckTableValue3 == 1:
            host = "your connect host: " + host
            user = "user: " + user
            password = "passwd: " + passwd
            database = "database: " + datebase
            table = "table: " + CheckTable1 + "," + CheckTable2 + "," + CheckTable3
            win = Tk()
            win.title("連線成功")
            text = Label(win, text = host)
            text.grid(row = 1, column = 1,sticky = W)
            text2 = Label(win, text = user)
            text2.grid(row = 2, column = 1,sticky = W)
            text3 = Label(win, text = password)
            text3.grid(row = 3, column = 1,sticky = W)
            text4 = Label(win, text = database)
            text4.grid(row = 4, column = 1,sticky = W)
            text5 = Label(win, text = table)
            text5.grid(row = 5, column = 1,sticky = W)
            run = Button(win, text = "執行", command = self.autoButton)
            run.grid(row = 6, column = 1,sticky = N)
            win.mainloop()
        else:
            win = Tk()
            win.title("連線失敗")
            create = "是否要建立" + CheckTable1 + "," + CheckTable2 + "," + CheckTable3 + "表格?"
            message = Label(win,text = create)
            message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)
            yes = Button(win, text = "Yes", command = self.YesAllButton)
            yes.grid(row = 2, column = 1)
            no = Button(win, text = "No", command = self.noButton)
            no.grid(row = 2, column = 2)
            win.mainloop()

    def autoButton(self):
        win = Tk()
        win.title("選擇模式")
        text = Label(win, text = "請選擇使用的模式。")
        text.grid(row = 1, column = 1,sticky = W)
        run = Button(win, text = "自動", command = self.runButton)
        run.grid(row = 2, column = 1,sticky = N)
        run = Button(win, text = "手動", command = self.Manual)
        run.grid(row = 2, column = 2,sticky = N)
        win.mainloop()

    def Manual(self):
        win = Tk()
        win.title("電源開關")
        run = Button(win, text = "Boot Power", command = self.Boot)
        run.grid(row = 1, column = 1,sticky = N)
        run = Button(win, text = "Shutdown Power", command = self.Shutdown)
        run.grid(row = 1, column = 2,sticky = N)
        win.mainloop()

    def runButton(self):
        while(1):
            CRCName = self.crcname.get()
            SocketCodeList = CRCName.split(',')
            for SocketCode in SocketCodeList:
                SocketCode = '%s' % SocketCode
                if SocketCode == "x01":
                    Stop = 0
                    BootPowerRCR = "\x01\x05\x00\x00\xFF\x00\x8C\x3A"
                    REPRCR = "\x01\x03\x00\x48\x00\x06\x45\xDE"
                    ShutdownPowerRCR = "\x01\x05\x00\x00\x00\x00\xCD\xCA"
                if SocketCode == "x02":
                    Stop = 0
                    BootPowerRCR = "\x02\x05\x00\x00\xFF\x00\x8C\x09"
                    REPRCR = "\x02\x03\x00\x48\x00\x06\x45\xED"
                    ShutdownPowerRCR = "\x02\x05\x00\x00\x00\x00\xCD\xF9"
                self.ReadPower(Stop, SocketCode, BootPowerRCR, REPRCR, ShutdownPowerRCR)
                time.sleep(1)
            pass

    def YesAllButton(self):
        tableauto = "auto"
        tableMachineLearning = "MachineLearning"
        tbalestatus = "status"
        print tableauto, tableMachineLearning, tbalestatus
        db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
        DataBase.CreateTable(tableauto, tableMachineLearning, tbalestatus, db)
    def noButton(self):
        win = Tk()
        win.title("連線失敗")
        message = Label(win,text = "建立失敗")
        message.grid(row = 1, column = 1)
        win.mainloop()

    def Boot(self):
        db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
        DataBase.Status(db, "status", self.crcname.get(), 1, 2, 2, 2)
        BootPowerRCR = "\x01\x05\x00\x00\xFF\x00\x8C\x3A"
        #REPRCR = "\x01\x03\x00\x48\x00\x06\x45\xDE"
        #ShutdownPowerRCR = "\x01\x05\x00\x00\x00\x00\xCD\xCA"
        PowerSocket.BootPower(BootPowerRCR, 9600)
        BootPowerRCR = "\x02\x05\x00\x00\xFF\x00\x8C\x09"
        #REPRCR = "\x02\x03\x00\x48\x00\x06\x45\xED"
        #ShutdownPowerRCR = "\x02\x05\x00\x00\x00\x00\xCD\xF9"
        PowerSocket.BootPower(BootPowerRCR, 9600)

    def Shutdown(self):
        db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
        DataBase.Status(db, "status", self.crcname.get(), 0, 2, 2, 2)
        #BootPowerRCR = "\x01\x05\x00\x00\xFF\x00\x8C\x3A"
        #REPRCR = "\x01\x03\x00\x48\x00\x06\x45\xDE"
        ShutdownPowerRCR = "\x01\x05\x00\x00\x00\x00\xCD\xCA"
        PowerSocket.ShutdownPower(ShutdownPowerRCR, 9600)
        #BootPowerRCR = "\x02\x05\x00\x00\xFF\x00\x8C\x09"
        #REPRCR = "\x02\x03\x00\x48\x00\x06\x45\xED"
        ShutdownPowerRCR = "\x02\x05\x00\x00\x00\x00\xCD\xF9"
        PowerSocket.ShutdownPower(ShutdownPowerRCR, 9600)

    def YesCreateAutoTableButton(self):
        apptableid = "auto"
        db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
        CreateTable = "create table " + apptableid +"(id int(20) auto_increment, app_id int(11), app_table_id int(11), socket_code float(3,0), v_val float(255,6), i_val float(255,6), p_val float(255,6), pt_val float(255,6), pf_val float(255,6), date int(20), primary key (id) );"
        DataBase.Connect(db, CreateTable)

    def ReadPower(self, Stop, socket_code, BootPowerRCR, REPRCR, ShutdownPowerRCR):
        if Stop == "":
            Stop = 0
        else:
            if Stop < 1:
                db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
                PowerSocket.BootPower(BootPowerRCR, 9600)
                time.sleep(0.5)
                date, V, I, P, PT, PF = PowerSocket.REP(REPRCR, 9600)
                if I <= 0:#更新"狀態"資料表"負載"欄位
                    noload = 0
                else:
                    noload = 1
                    DataBase.Status(db, "status", self.crcname.get(), 1, 0, noload, 0)
                if I >= 9:
                    db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
                    PowerSocket.ShutdownPower(ShutdownPowerRCR, 9600)
                    DataBase.Status(db, "status", self.crcname.get(), 0, 1, 1, 0)
                    Stop = 2
                else:
                    apptableid = "auto"
                    print apptableid
                    Select = "select * from " + apptableid + ";"
                    Command = "INSERT INTO " + apptableid +"(id, socket_code, date, v_val, i_val, p_val, pt_val, pf_val) VALUES(NULL, '%s', '%s', '%f', '%f', '%f', '%f', '%f')"%(socket_code, date, V, I, P, PT, PF)
                    try:
                        db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
                        DataBase.Connect(db, Select)
                        print "The Table Is Exist"
                    except:
                        win = Tk()
                        win.title("連線失敗")
                        create = "是否要建立" + apptableid + "表格?"
                        message = Label(win,text = create)
                        message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)
                        yes = Button(win, text = "Yes", command = self.YesCreateAutoTableButton)
                        yes.grid(row = 2, column = 1)
                        no = Button(win, text = "No", command = self.noButton)
                        no.grid(row = 2, column = 2)
                        win.mainloop()
                    else:
                        db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
                        DataBase.Connect(db, Command)
                        time.sleep(0.5)

AAA()
