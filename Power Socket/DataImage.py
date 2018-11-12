#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
"""
20180711加上製作圖片的模組，讓製圖時比較方便，可惜沒有成功
"""
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap



def SDSPMI(Data):
    #ShowDataScatterPlotMatrixImage(資料來源)
    import sys
    import pandas
    from pandas.tools.plotting import scatter_matrix
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    Names = ['class', 'V', 'I', 'P', 'PF','Date']
    DataSet = pandas.read_csv(Data, names = Names)
    scatter_matrix(DataSet)
    plt.show()

def ShowDataImage(Data, StartRow, EndRow, ClassLabel, Features1, Features2, Label, XLabel, Ylabel):
    df = pd.read_csv(Data, header=None)
    df.tail()
    y = df.iloc[StartRow:EndRow, ClassLabel].values
    X = df.iloc[StartRow:EndRow, [Features1, Features2]].values
    PltScatter(StartRow, EndRow, 'blue', 'x', Label)
    OutputImage(XLabel, Ylabel)

def PltScatter(StartRow, EndRow, Colors, Markers, Label):
    plt.scatter(X[StartRow:EndRow, 0], X[StartRow:EndRow, 1], color = Colors, marker= Markers, label = Label)

"""
def dfInputData(Y_Input, X_Input, StartRow, EndRow, Interval, XLabel, Ylabel):#資料來源,開始行,結束行,
    y = Y_Input
    X = X_Input
    unique = np.unique(y)
    markers = ['s', 'x', 'o', '^', 'v', 's', 'x', 'o', '^', 'v']
    colors = ['red', 'blue', 'lightgreen', 'gray', 'cyan', 'yellow', 'black', 'green', 'purple', 'Orange']
    i = 1
    for Label in unique:
        i = + i
        if i > 1:
            StartRow += Interval
            EndRow += Interval
            PltScatter(StartRow, EndRow, colors, markers, Label)
        else:
            PltScatter(StartRow, EndRow, colors, markers, Label)
    OutputImage(XLabel, Ylabel)
"""
def versiontuple(v):
    return tuple(map(int, (v.split("."))))

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):

    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v', 's', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan', 'yellow', 'black', 'green', 'purple', 'Orange')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)

    # highlight test samples
    if test_idx:
        # plot all samples
        if not versiontuple(np.__version__) >= versiontuple('1.9.0'):
            X_test, y_test = X[list(test_idx), :], y[list(test_idx)]
            warnings.warn('Please update to NumPy 1.9.0 or newer')
        else:
            X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(X_test[:, 0],
                    X_test[:, 1],
                    c='',
                    alpha=1.0,
                    linewidths=1,
                    marker='o',
                    s=55, label='test set')

def OutputImage(XLabel, Ylabel):
    plt.xlabel(XLabel)
    plt.ylabel(Ylabel)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('./support_vector_machine_linear.png', dpi=1000)
    plt.show()
