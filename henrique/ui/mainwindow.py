# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/mainwindow.ui'
#
# Created: Fri Apr 25 15:25:21 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(545, 467)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 501, 381))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.sendReportButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendReportButton.sizePolicy().hasHeightForWidth())
        self.sendReportButton.setSizePolicy(sizePolicy)
        self.sendReportButton.setObjectName(_fromUtf8("sendReportButton"))
        self.verticalLayout.addWidget(self.sendReportButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuReport = QtGui.QMenu(self.menubar)
        self.menuReport.setObjectName(_fromUtf8("menuReport"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSendReport = QtGui.QAction(MainWindow)
        self.actionSendReport.setObjectName(_fromUtf8("actionSendReport"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSend = QtGui.QAction(MainWindow)
        self.actionSend.setObjectName(_fromUtf8("actionSend"))
        self.actionHistory = QtGui.QAction(MainWindow)
        self.actionHistory.setObjectName(_fromUtf8("actionHistory"))
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionClose)
        self.menuReport.addAction(self.actionSend)
        self.menuReport.addAction(self.actionHistory)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Dear Henrique, here\'s what I\'ve done today:", None))
        self.sendReportButton.setText(_translate("MainWindow", "Send", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuReport.setTitle(_translate("MainWindow", "Report", None))
        self.actionSendReport.setText(_translate("MainWindow", "Send Report", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionSend.setText(_translate("MainWindow", "Send", None))
        self.actionHistory.setText(_translate("MainWindow", "History", None))

