#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
"""
20180112找到的範例，雖然有更改，但沒有完成與成功
20180128成功顯示是否連到資料庫與表格，並可以成功整齊的排在一起
20180129加入了可以讀取電力模組的程式碼
20180710繼PythonGUI成功的模組化，也將模組化應用在此程式碼，目前測試都是成功的，希望在
        未來可以將RCR檢查碼可以在輸入時就可以修改。
"""
import serial
import time
import MySQLdb
import datetime
import PowerSocket
import DataBase
from Tkinter import *

class AAA:
    def __init__(self):
        win = Tk()
        win.title("MySQL")

        hostrow, userrow, passwordrow, databaserow, tablerow, connectrow = 1, 2, 3, 4, 5, 6

        #Host:欄位程式碼
        host = Label(win, text = "Host: ")
        self.hostname = StringVar()
        hostentry = Entry(win, textvariable = self.hostname)
        host.grid(row = hostrow, column = 1)
        hostentry.grid(row = hostrow, column = 2)

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
        table = Label(win, text = "Table: ")
        self.tablename = StringVar()
        tableName = Entry(win, textvariable = self.tablename)
        table.grid(row = tablerow, column = 1)
        tableName.grid(row = tablerow, column = 2)

        #連線按鈕的程式碼
        connect = Button(win, text = "Connect",command = self.connectButton)
        connect.grid(row = connectrow, column = 1)

        win.mainloop()

    def connectButton(self):
        CheckTable = self.tablename.get()
        print CheckTable
        db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
        CheckTableName, CheckTableValue = DataBase.CheckTable(CheckTable, db)
        if CheckTableValue == 0:
            print "Not connect"
            create = "Not connect,Are you create name " + CheckTableName + " Table ?"
            win = Tk()
            win.title("連線失敗")
            message = Label(win,text = create)
            message.grid(row = 1, column = 1,sticky = N)
            yes = Button(win, text = "Yes", command = self.yesButton)
            yes.grid(row = 2, column = 1,sticky = N)
            no = Button(win, text = "No", command = self.noButton)
            no.grid(row = 2, column = 2,sticky = N)
            win.mainloop()

        else:
            host = "your connect host: " + self.hostname.get()
            user = "user: " + self.username.get()
            password = "passwd: " + self.passwordname.get()
            database = "database: " + self.databasename.get()
            table = "table: " + self.tablename.get()

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
            #text6 = Label(win, text = quantity)
            #text6.grid(row = 6, column = 1,sticky = W)
            run = Button(win, text = "Run", command = self.runButton)
            run.grid(row = 7, column = 1,sticky = N)

            win.mainloop()

    def runButton(self):
        print "run"
        while(1):
            BootPowerRCR = "\x01\x05\x00\x00\xFF\x00\x8C\x3A"
            REPRCR = "\x01\x03\x00\x48\x00\x06\x45\xDE"
            ShutdownPowerRCR = "\x01\x05\x00\x00\x00\x00\xCD\xCA"
            """
            BootPowerRCR = "\x02\x05\x00\x00\xFF\x00\x8C\x09"
            REPRCR = "\x02\x03\x00\x48\x00\x06\x45\xED"
            ShutdownPowerRCR = "\x02\x05\x00\x00\x00\x00\xCD\xF9"
            """
            db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
            PowerSocket.BootPower(BootPowerRCR, 9600)
            time.sleep(0.5)

            db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
            date, V, I, P, PT, PF = PowerSocket.REP(REPRCR, 9600)                #Read ten characters from serial port to data
            apptableid = self.tablename.get()

            print apptableid
            Select = "select * from " + apptableid + ";"
            Command = "INSERT INTO " + apptableid +"(id, date, v_val, i_val, p_val, pt_val, pf_val) VALUES(NULL, '%s', '%f', '%f', '%f', '%f', '%f')"%(date, V, I, P, PT, PF)
            try:
                db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
                DataBase.Connect(db, Select)
                print "The Table Is Exist"

            except:
                create = "Not connect,Are you create name " + apptableid + " Table ?"
                win = Tk()
                win.title("連線失敗")

                message = Label(win,text = create)
                message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)
                yes = Button(win, text = "Yes", command = self.yesButton)
                yes.grid(row = 2, column = 1)
                no = Button(win, text = "No", command = self.noButton)
                no.grid(row = 2, column = 2)

                win.mainloop()

            else:
                db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
                DataBase.Connect(db, Command)
                time.sleep(0.5)
    def yesButton(self):
        apptableid = self.tablename.get()
        #print apptableid
        CreateTable = "create table " + self.tablename.get() +"(id int(20) auto_increment, app_id int(11), v_val float(255,6), i_val float(255,6), p_val float(255,6), pt_val float(255,6), pf_val float(255,6), date int(20), primary key (id) );"
        db = MySQLdb.connect(host = self.hostname.get(), user = self.username.get(), passwd = self.passwordname.get(), db = self.databasename.get(), charset="utf8")
        DataBase.Connect(db, CreateTable)

    def noButton(self):
        win = Tk()
        win.title("連線失敗")
        message = Label(win,text = "建立失敗")
        message.grid(row = 1, column = 1)
        win.mainloop()
AAA()
