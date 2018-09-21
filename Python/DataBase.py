#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
"""
20180702可以檢查資料表、更新狀態、創建新資料表、顯示連線資料庫的函式
201807021751可成功將狀態上傳至資料庫
"""
from Tkinter import *
import MySQLdb

def ConnectMySQLServer(Host, User, Passwd, DataBase, Charset):
    db = MySQLdb.connect(Host, User, Passwd, DataBase, Charset)
    return db

def CheckTable(Checktablename,db):#檢查指定資料表是否存在
    print Checktablename
    select = "select * from " + Checktablename + ";"
    db.cursor()
    cursor = db.cursor()
    try:
        data = cursor.execute(select)
        print data
        ListCheckTable = [Checktablename, 1]
        return ListCheckTable#連線成功回傳1
    except:
        print "Not connect"
        ListCheckTable = [Checktablename, 0]
        return ListCheckTable#連線失敗回傳0
    db.commit()
    db.close()

def InsertIntoStatus(db, Table, socket_code, Appliances, Status, Overload, Noload, Ageing):#輸入"Status"資料表
    select = "INSERT INTO " + Table +"(socket_code, appliance, status, overload, noload, ageing) VALUES('%s', '%s', '%f', '%f', '%f', '%f')"%(socket_code, Appliances, Status, Overload, Noload, Ageing)
    print select
    print Appliances
    cursor = db.cursor()
    cursor.execute(select)
    db.commit()
    db.close()
    return 1

def UpdataStatus(db, Table, socket_code, Appliances, Status, Overload, Noload, Ageing):#更新"Status"資料表
    #select = "UPDATE " + apptableid + " SET status = " + str(a) + ",overload = " + str(b) + ",noload = " + str(c) + ",ageing = " + str(d) + " WHERE socket_code = 1;"
    select = 'UPDATE ' + Table + ' SET appliance = "' + '%s'%Appliances + '",status=' + str(Status) + ',overload = ' + str(Overload) + ',noload = ' + str(Noload) + ',ageing = ' + str(Ageing) + ' WHERE socket_code = "' + '%s'%socket_code + '";'
    print select
    print Appliances
    cursor = db.cursor()
    cursor.execute(select)
    db.commit()
    db.close()
    return 1

def Status(db, Table, socket_code, Status, Overload, Noload, Ageing):#更新"Status"資料表
    select = 'UPDATE ' + Table + ' SET status=' + str(Status) + ',overload = ' + str(Overload) + ',noload = ' + str(Noload) + ',ageing = ' + str(Ageing) + ' WHERE socket_code = "' + '%s'%socket_code + '";'
    cursor = db.cursor()
    cursor.execute(select)
    db.commit()
    db.close()
    return 1

def UpdataStatusAppliances(db, Table, socket_code, Appliances):#更新"Status"資料表
    #select = "UPDATE " + apptableid + " SET status = " + str(a) + ",overload = " + str(b) + ",noload = " + str(c) + ",ageing = " + str(d) + " WHERE socket_code = 1;"
    select = 'UPDATE ' + Table + ' SET appliance = "' + '%s'%Appliances + '" WHERE socket_code = "' + '%s'%socket_code + '";'
    print select
    print Appliances
    cursor = db.cursor()
    cursor.execute(select)
    db.commit()
    db.close()
    return 1

def CreateTable(CreateTableAuto, CreateTableMachineLearning, CreateTbaleStatus, db):#創建新的資料表
    CreateTableAuto = "create table " + CreateTableAuto +"(id int(20) auto_increment, app_table_id int(11), v_val float(255,6), i_val float(255,6), p_val float(255,6), pt_val float(255,6), pf_val float(255,6), date int(20), primary key (id) );"
    CreateTableMachineLearning = "create table " + CreateTableMachineLearning +"(id int(20) auto_increment, app_table_id int(11), v_val float(255,6), i_val float(255,6), p_val float(255,6), pt_val float(255,6), pf_val float(255,6), date int(20), primary key (id) );"
    CreateTbaleStatus = "create table " + CreateTbaleStatus +"(socket_code int(20) auto_increment, appliance int(1), status int(1), overload int(1), noload int(1), ageing int(1), primary key (socket_code) );"
    cursor = db.cursor()
    cursor.execute(CreateTableAuto)
    cursor.execute(CreateTableMachineLearning)
    cursor.execute(CreateTbaleStatus)
    db.commit()
    db.close()

def Connect(db, Command):    #使用SQL指令來控制MySQL
    cursor = db.cursor()
    OutputResult = cursor.execute(Command)
    db.commit()
    db.close()
    return OutputResult

def ReadMySQL(db, Command):    #使用SQL指令來控制MySQL
    cursor = db.cursor()
    cursor.execute(Command)
    results = cursor.fetchall()
    db.commit()
    db.close()
    return results
