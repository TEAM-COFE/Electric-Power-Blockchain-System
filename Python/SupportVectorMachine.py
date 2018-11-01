#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
import DataImage as DI
import DataBase as DB
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import MySQLdb
import time

def TrainSupportVectorMachine():
    """
    函式說明:
    將訓練數據集以散佈圖呈現。
    改進項目:
    資料位置修改，圖片自動設定顏色(color)、標記(marker)、標籤(label)、資料起始結束位置。將SVM的輸入維度增加到4維以上，使預測精準度增加，誤分減少。
    """
    #建立函式
    df = pd.read_csv('../Data/Learn.csv', header=None)#讀取訓練數據集
    df.tail()
    # select setosa and versicolor
    y = df.iloc[1:, 0].values#y = df.iloc[數據開始行:數據結束行, 0].values
    # extract sepal length and petal length
    X = df.iloc[1:, [1, 2]].values#y = df.iloc[數據開始行:數據結束行,[特徵1,特徵2]].values
    # plot data
    plt.scatter(X[1:199, 0], X[1:199, 1],color='red', marker='o', label='FS')#plt.scatter(X[數據開始:, 0], X[1:199, 1],color='點的顏色', marker='點的樣子', label='特徵名稱')
    DI.OutputImage("I", "COS")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    #使用SVM訓練後進行測試，測試後顯示被誤分次數
    svm = SVC(kernel='linear', C=1.0, random_state=0)
    svm.fit(X_train_std, y_train)
    y_test.shape
    y_pred = svm.predict(X_test_std)
    print('Misclassified samples: %d' % (y_test != y_pred).sum())

    #顯示分類正確率
    print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))

    DI.plot_decision_regions(X_combined_std, y_combined,classifier=svm, test_idx=range(105, 150))
    DI.OutputImage("I", "COS")

    return svm

def SupportVectorMachinePrediction(svm):
    """
    說明:
    經過訓練SVM可以經由變數svm變數代入模組裡進行預測。此模組從資料庫取得預測數據集後預測電器結果回傳。
    改進項目:
    可以將資料庫的程式碼放入到DataBase裡面，可以利用指令達到同樣結果。
    數據集自動製作.csv。
    """
    #提供資料庫中的資料
    Select = "SELECT v_val, i_val, p_val, pf_val FROM auto order by id desc limit 1"
    db = MySQLdb.connect(host="192.168.43.122", user="root", passwd="openele", db="power", charset="utf8")
    for ReadData in DB.ReadMySQL(db, Select):#將查詢結果一筆一筆放入ReadData執行後續的程式。
        V = ReadData[0]#
        I = ReadData[1]
        P = ReadData[2]
        PF = ReadData[3]
        Xvalidation = [['%f' % I, '%f' % PF]]#這邊可以控制輸出預測數據集

    #使用的預測方法
    predictions = svm.predict(Xvalidation)
    print predictions
    for appliances in predictions:
            appliances = appliances

    #回傳資料
    return appliances

def SupportVectorMachineUpdataAppliancesStatus():
    svm = TrainSupportVectorMachine()
    while(1):
        appliances = SupportVectorMachinePrediction(svm)
        db = MySQLdb.connect(host="192.168.43.122", user="root", passwd="openele", db="power", charset="utf8")
        DB.UpdataStatusAppliances(db, "status", "x02", appliances)
        time.sleep(1)

SupportVectorMachineUpdataAppliancesStatus()
