# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thinFlow_mainWdw.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(1043, 991)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)
        self.plotNTFFrame = QtGui.QFrame(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotNTFFrame.sizePolicy().hasHeightForWidth())
        self.plotNTFFrame.setSizePolicy(sizePolicy)
        self.plotNTFFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotNTFFrame.setObjectName(_fromUtf8("plotNTFFrame"))
        self.gridLayout.addWidget(self.plotNTFFrame, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.nodeSelectionListWidget = QtGui.QListWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.nodeSelectionListWidget.sizePolicy().hasHeightForWidth())
        self.nodeSelectionListWidget.setSizePolicy(sizePolicy)
        self.nodeSelectionListWidget.setObjectName(_fromUtf8("nodeSelectionListWidget"))
        self.gridLayout_3.addWidget(self.nodeSelectionListWidget, 0, 1, 1, 1)
        self.edgeSelectionListWidget = QtGui.QListWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.edgeSelectionListWidget.sizePolicy().hasHeightForWidth())
        self.edgeSelectionListWidget.setSizePolicy(sizePolicy)
        self.edgeSelectionListWidget.setObjectName(_fromUtf8("edgeSelectionListWidget"))
        self.gridLayout_3.addWidget(self.edgeSelectionListWidget, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 1, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 1, 1, 2)
        self.plotFrame = QtGui.QFrame(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotFrame.sizePolicy().hasHeightForWidth())
        self.plotFrame.setSizePolicy(sizePolicy)
        self.plotFrame.setFrameShape(QtGui.QFrame.Box)
        self.plotFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.plotFrame.setObjectName(_fromUtf8("plotFrame"))
        self.gridLayout.addWidget(self.plotFrame, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid rgb(0, 0, 127); \n"
"     border-radius: 1px; \n"
" } "))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cleanUpCheckBox = QtGui.QCheckBox(self.groupBox)
        self.cleanUpCheckBox.setObjectName(_fromUtf8("cleanUpCheckBox"))
        self.gridLayout_2.addWidget(self.cleanUpCheckBox, 0, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 4, 1, 1)
        self.timeoutLineEdit = QtGui.QLineEdit(self.groupBox)
        self.timeoutLineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeoutLineEdit.sizePolicy().hasHeightForWidth())
        self.timeoutLineEdit.setSizePolicy(sizePolicy)
        self.timeoutLineEdit.setObjectName(_fromUtf8("timeoutLineEdit"))
        self.gridLayout_2.addWidget(self.timeoutLineEdit, 1, 5, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.scipPathPushButton = QtGui.QPushButton(self.groupBox)
        self.scipPathPushButton.setObjectName(_fromUtf8("scipPathPushButton"))
        self.gridLayout_2.addWidget(self.scipPathPushButton, 1, 2, 1, 1)
        self.timeoutLabel = QtGui.QLabel(self.groupBox)
        self.timeoutLabel.setEnabled(False)
        self.timeoutLabel.setObjectName(_fromUtf8("timeoutLabel"))
        self.gridLayout_2.addWidget(self.timeoutLabel, 1, 4, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.outputDirectoryLineEdit = QtGui.QLineEdit(self.groupBox)
        self.outputDirectoryLineEdit.setObjectName(_fromUtf8("outputDirectoryLineEdit"))
        self.gridLayout_2.addWidget(self.outputDirectoryLineEdit, 0, 1, 1, 1)
        self.outputDirectoryPushButton = QtGui.QPushButton(self.groupBox)
        self.outputDirectoryPushButton.setObjectName(_fromUtf8("outputDirectoryPushButton"))
        self.gridLayout_2.addWidget(self.outputDirectoryPushButton, 0, 2, 1, 1)
        self.inflowLineEdit = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inflowLineEdit.sizePolicy().hasHeightForWidth())
        self.inflowLineEdit.setSizePolicy(sizePolicy)
        self.inflowLineEdit.setObjectName(_fromUtf8("inflowLineEdit"))
        self.gridLayout_2.addWidget(self.inflowLineEdit, 0, 5, 1, 1)
        self.templateComboBox = QtGui.QComboBox(self.groupBox)
        self.templateComboBox.setObjectName(_fromUtf8("templateComboBox"))
        self.templateComboBox.addItem(_fromUtf8(""))
        self.templateComboBox.addItem(_fromUtf8(""))
        self.templateComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.templateComboBox, 3, 1, 1, 1)
        self.scipPathLineEdit = QtGui.QLineEdit(self.groupBox)
        self.scipPathLineEdit.setObjectName(_fromUtf8("scipPathLineEdit"))
        self.gridLayout_2.addWidget(self.scipPathLineEdit, 1, 1, 1, 1)
        self.activateTimeoutCheckBox = QtGui.QCheckBox(self.groupBox)
        self.activateTimeoutCheckBox.setObjectName(_fromUtf8("activateTimeoutCheckBox"))
        self.gridLayout_2.addWidget(self.activateTimeoutCheckBox, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1043, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionLoad_Graph = QtGui.QAction(MainWindow)
        self.actionLoad_Graph.setObjectName(_fromUtf8("actionLoad_Graph"))
        self.actionSave_Graph = QtGui.QAction(MainWindow)
        self.actionSave_Graph.setObjectName(_fromUtf8("actionSave_Graph"))
        self.actionNew_graph = QtGui.QAction(MainWindow)
        self.actionNew_graph.setObjectName(_fromUtf8("actionNew_graph"))
        self.actionLoad_graph = QtGui.QAction(MainWindow)
        self.actionLoad_graph.setObjectName(_fromUtf8("actionLoad_graph"))
        self.actionSave_graph = QtGui.QAction(MainWindow)
        self.actionSave_graph.setObjectName(_fromUtf8("actionSave_graph"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionLoad_NashFlow = QtGui.QAction(MainWindow)
        self.actionLoad_NashFlow.setEnabled(False)
        self.actionLoad_NashFlow.setVisible(False)
        self.actionLoad_NashFlow.setObjectName(_fromUtf8("actionLoad_NashFlow"))
        self.actionSave_NashFlow = QtGui.QAction(MainWindow)
        self.actionSave_NashFlow.setVisible(False)
        self.actionSave_NashFlow.setObjectName(_fromUtf8("actionSave_NashFlow"))
        self.actionOpen_manual = QtGui.QAction(MainWindow)
        self.actionOpen_manual.setObjectName(_fromUtf8("actionOpen_manual"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Edge", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Node", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.groupBox.setTitle(_translate("MainWindow", "Config", None))
        self.cleanUpCheckBox.setText(_translate("MainWindow", "Clean-up", None))
        self.label_8.setText(_translate("MainWindow", "Inflow Rate", None))
        self.timeoutLineEdit.setText(_translate("MainWindow", "300", None))
        self.label_11.setText(_translate("MainWindow", "Algorithm & Template", None))
        self.scipPathPushButton.setText(_translate("MainWindow", "Select binary", None))
        self.timeoutLabel.setText(_translate("MainWindow", "Timeout (in s)", None))
        self.label_12.setText(_translate("MainWindow", "SCIP path", None))
        self.label_9.setText(_translate("MainWindow", "Output directory", None))
        self.outputDirectoryPushButton.setText(_translate("MainWindow", "Select directory", None))
        self.inflowLineEdit.setText(_translate("MainWindow", "0", None))
        self.templateComboBox.setItemText(0, _translate("MainWindow", "1. Basic algorithm", None))
        self.templateComboBox.setItemText(1, _translate("MainWindow", "2. Solve only LP/IP", None))
        self.templateComboBox.setItemText(2, _translate("MainWindow", "3. Advanced algorithm", None))
        self.activateTimeoutCheckBox.setText(_translate("MainWindow", "Timeout", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionLoad_Graph.setText(_translate("MainWindow", "Load Graph", None))
        self.actionSave_Graph.setText(_translate("MainWindow", "Save Graph", None))
        self.actionNew_graph.setText(_translate("MainWindow", "New graph", None))
        self.actionLoad_graph.setText(_translate("MainWindow", "Load graph", None))
        self.actionSave_graph.setText(_translate("MainWindow", "Save graph", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionLoad_NashFlow.setText(_translate("MainWindow", "Load NashFlow", None))
        self.actionSave_NashFlow.setText(_translate("MainWindow", "Save NashFlow", None))
        self.actionOpen_manual.setText(_translate("MainWindow", "Open manual", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

import icons_rc
