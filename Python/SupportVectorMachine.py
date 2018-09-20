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
    #df = pd.read_csv('F:/JeinPoLiEnergySavingLamps_All_20180722.csv', header=None)
    df = pd.read_csv('F:/ok_appliances_20180726.csv', header=None)
    df.tail()
    # select setosa and versicolor
    y = df.iloc[1:, 0].values#數據開始行:數據結束行
    # extract sepal length and petal length
    #X = df.iloc[1:, [2, 4]].values#數據開始行:數據結束行,特徵1,特徵2
    X = df.iloc[1:, [1, 2]].values#數據開始行:數據結束行,特徵1,特徵2
    # plot data
    plt.scatter(X[1:199, 0], X[1:199, 1],color='red', marker='o', label='FS')
    plt.scatter(X[200:399, 0], X[200:399, 1],color='blue', marker='x', label='HW')
    plt.scatter(X[400:599, 0], X[400:599, 1],color='green', marker='^', label='SB')
    #plt.scatter(X[10000:15999, 0], X[10000:15999, 1],color='gray', marker='s', label='T5 Twenty Eight Watt')
    DI.OutputImage("I", "COS")

    y = df.iloc[1:, 0].values
    #X = df.iloc[1:, [2, 4]].values#數據開始行:數據結束行,特徵1,特徵2
    X = df.iloc[1:, [1, 2]].values#數據開始行:數據結束行,特徵1,特徵2
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    #顯示被誤分次數
    ppn = Perceptron(n_iter=100, eta0=0.1, random_state=0)
    ppn.fit(X_train_std, y_train)
    y_test.shape
    y_pred = ppn.predict(X_test_std)
    print('Misclassified samples: %d' % (y_test != y_pred).sum())

    #顯示分類正確率
    print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))

    svm = SVC(kernel='linear', C=1.0, random_state=0)
    svm = svm.fit(X_train_std, y_train)

    DI.plot_decision_regions(X_combined_std, y_combined,classifier=svm, test_idx=range(105, 150))
    DI.OutputImage("I", "COS")

    return svm

def SupportVectorMachinePrediction(svm):
    #提供資料庫中的資料
    Select = "SELECT v_val, i_val, p_val, pf_val FROM auto order by id desc limit 1"
    db = MySQLdb.connect(host="192.168.43.122", user="root", passwd="openele", db="power", charset="utf8")

    for ReadData in DB.ReadMySQL(db, Select):
        V = ReadData[0]#
        I = ReadData[1]
        P = ReadData[2]
        PF = ReadData[3]
        #Xvalidation = [["%f" % V,'%f' % I, '%f' % P, '%f' % PF]]#這邊可以控制輸出預測數據集
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
"""
def OutDecisionBoundary():
    from sklearn import svm
    df = pd.read_csv('F:/NoLoad_All_appliances_20180717.csv', header=None)
    y = df.iloc[:, 0].values
    X = df.iloc[:, [2, 4]].values#數據開始行:數據結束行,特徵1,特徵2
    svm = SVC(kernel='linear', C=1.0, random_state=0)
    svm.fit(X, y)
    c = svm.intercept_
    a = svm.coef_
    for intercept, coef in zip(svm.intercept_, svm.coef_):
        s = "y = {0:.3f}".format(intercept)
        for i, c in enumerate(coef):
            s += " +{0:.3f} * x{1}".format(c, i)
        print s
    return a, c
"""
