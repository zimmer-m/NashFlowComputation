# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thinFlow_mainWdw.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_general = QtWidgets.QWidget()
        self.tab_general.setObjectName("tab_general")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_general)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_general)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.updateNodeButton_general = QtWidgets.QPushButton(self.groupBox_3)
        self.updateNodeButton_general.setAutoDefault(False)
        self.updateNodeButton_general.setDefault(False)
        self.updateNodeButton_general.setFlat(False)
        self.updateNodeButton_general.setObjectName("updateNodeButton_general")
        self.gridLayout_4.addWidget(self.updateNodeButton_general, 2, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nodeNameLineEdit_general = QtWidgets.QLineEdit(self.groupBox_3)
        self.nodeNameLineEdit_general.setObjectName("nodeNameLineEdit_general")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nodeNameLineEdit_general)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.nodeXLineEdit_general = QtWidgets.QLineEdit(self.groupBox_3)
        self.nodeXLineEdit_general.setObjectName("nodeXLineEdit_general")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nodeXLineEdit_general)
        self.nodeYLineEdit_general = QtWidgets.QLineEdit(self.groupBox_3)
        self.nodeYLineEdit_general.setObjectName("nodeYLineEdit_general")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nodeYLineEdit_general)
        self.gridLayout_4.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.deleteNodeButton_general = QtWidgets.QPushButton(self.groupBox_3)
        self.deleteNodeButton_general.setAutoDefault(False)
        self.deleteNodeButton_general.setDefault(False)
        self.deleteNodeButton_general.setFlat(False)
        self.deleteNodeButton_general.setObjectName("deleteNodeButton_general")
        self.gridLayout_4.addWidget(self.deleteNodeButton_general, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.nodeSelectionListWidget_general = QtWidgets.QListWidget(self.tab_general)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.nodeSelectionListWidget_general.sizePolicy().hasHeightForWidth())
        self.nodeSelectionListWidget_general.setSizePolicy(sizePolicy)
        self.nodeSelectionListWidget_general.setObjectName("nodeSelectionListWidget_general")
        self.gridLayout_3.addWidget(self.nodeSelectionListWidget_general, 0, 1, 1, 1)
        self.computeThinFlowPushButton_general = QtWidgets.QPushButton(self.tab_general)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.computeThinFlowPushButton_general.sizePolicy().hasHeightForWidth())
        self.computeThinFlowPushButton_general.setSizePolicy(sizePolicy)
        self.computeThinFlowPushButton_general.setObjectName("computeThinFlowPushButton_general")
        self.gridLayout_3.addWidget(self.computeThinFlowPushButton_general, 1, 0, 1, 2)
        self.edgeSelectionListWidget_general = QtWidgets.QListWidget(self.tab_general)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.edgeSelectionListWidget_general.sizePolicy().hasHeightForWidth())
        self.edgeSelectionListWidget_general.setSizePolicy(sizePolicy)
        self.edgeSelectionListWidget_general.setObjectName("edgeSelectionListWidget_general")
        self.gridLayout_3.addWidget(self.edgeSelectionListWidget_general, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 1, 1, 2)
        self.plotNTFFrame_general = QtWidgets.QFrame(self.tab_general)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotNTFFrame_general.sizePolicy().hasHeightForWidth())
        self.plotNTFFrame_general.setSizePolicy(sizePolicy)
        self.plotNTFFrame_general.setObjectName("plotNTFFrame_general")
        self.gridLayout.addWidget(self.plotNTFFrame_general, 1, 0, 1, 1)
        self.plotFrame_general = QtWidgets.QFrame(self.tab_general)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotFrame_general.sizePolicy().hasHeightForWidth())
        self.plotFrame_general.setSizePolicy(sizePolicy)
        self.plotFrame_general.setObjectName("plotFrame_general")
        self.gridLayout.addWidget(self.plotFrame_general, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_general)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.capacityLineEdit_general = QtWidgets.QLineEdit(self.groupBox_2)
        self.capacityLineEdit_general.setObjectName("capacityLineEdit_general")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.capacityLineEdit_general)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.resettingSwitchButton_general = QtWidgets.QPushButton(self.groupBox_2)
        self.resettingSwitchButton_general.setEnabled(False)
        self.resettingSwitchButton_general.setObjectName("resettingSwitchButton_general")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.resettingSwitchButton_general)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.updateEdgeButton_general = QtWidgets.QPushButton(self.groupBox_2)
        self.updateEdgeButton_general.setAutoDefault(False)
        self.updateEdgeButton_general.setDefault(False)
        self.updateEdgeButton_general.setFlat(False)
        self.updateEdgeButton_general.setObjectName("updateEdgeButton_general")
        self.verticalLayout_2.addWidget(self.updateEdgeButton_general)
        self.deleteEdgeButton_general = QtWidgets.QPushButton(self.groupBox_2)
        self.deleteEdgeButton_general.setAutoDefault(False)
        self.deleteEdgeButton_general.setDefault(False)
        self.deleteEdgeButton_general.setFlat(False)
        self.deleteEdgeButton_general.setObjectName("deleteEdgeButton_general")
        self.verticalLayout_2.addWidget(self.deleteEdgeButton_general)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_general, "")
        self.tab_spillback = QtWidgets.QWidget()
        self.tab_spillback.setObjectName("tab_spillback")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_spillback)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.plotNTFFrame_spillback = QtWidgets.QFrame(self.tab_spillback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotNTFFrame_spillback.sizePolicy().hasHeightForWidth())
        self.plotNTFFrame_spillback.setSizePolicy(sizePolicy)
        self.plotNTFFrame_spillback.setObjectName("plotNTFFrame_spillback")
        self.gridLayout_7.addWidget(self.plotNTFFrame_spillback, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_spillback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.capacityLineEdit_spillback = QtWidgets.QLineEdit(self.groupBox_4)
        self.capacityLineEdit_spillback.setObjectName("capacityLineEdit_spillback")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.capacityLineEdit_spillback)
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.boundLineEdit_spillback = QtWidgets.QLineEdit(self.groupBox_4)
        self.boundLineEdit_spillback.setObjectName("boundLineEdit_spillback")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.boundLineEdit_spillback)
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.resettingSwitchButton_spillback = QtWidgets.QPushButton(self.groupBox_4)
        self.resettingSwitchButton_spillback.setEnabled(False)
        self.resettingSwitchButton_spillback.setObjectName("resettingSwitchButton_spillback")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.resettingSwitchButton_spillback)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.updateEdgeButton_spillback = QtWidgets.QPushButton(self.groupBox_4)
        self.updateEdgeButton_spillback.setAutoDefault(False)
        self.updateEdgeButton_spillback.setDefault(False)
        self.updateEdgeButton_spillback.setFlat(False)
        self.updateEdgeButton_spillback.setObjectName("updateEdgeButton_spillback")
        self.verticalLayout_3.addWidget(self.updateEdgeButton_spillback)
        self.deleteEdgeButton_spillback = QtWidgets.QPushButton(self.groupBox_4)
        self.deleteEdgeButton_spillback.setAutoDefault(False)
        self.deleteEdgeButton_spillback.setDefault(False)
        self.deleteEdgeButton_spillback.setFlat(False)
        self.deleteEdgeButton_spillback.setObjectName("deleteEdgeButton_spillback")
        self.verticalLayout_3.addWidget(self.deleteEdgeButton_spillback)
        self.gridLayout_7.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.plotFrame_spillback = QtWidgets.QFrame(self.tab_spillback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotFrame_spillback.sizePolicy().hasHeightForWidth())
        self.plotFrame_spillback.setSizePolicy(sizePolicy)
        self.plotFrame_spillback.setObjectName("plotFrame_spillback")
        self.gridLayout_7.addWidget(self.plotFrame_spillback, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_spillback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.updateNodeButton_spillback = QtWidgets.QPushButton(self.groupBox_5)
        self.updateNodeButton_spillback.setAutoDefault(False)
        self.updateNodeButton_spillback.setDefault(False)
        self.updateNodeButton_spillback.setFlat(False)
        self.updateNodeButton_spillback.setObjectName("updateNodeButton_spillback")
        self.gridLayout_5.addWidget(self.updateNodeButton_spillback, 2, 0, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.nodeNameLineEdit_spillback = QtWidgets.QLineEdit(self.groupBox_5)
        self.nodeNameLineEdit_spillback.setObjectName("nodeNameLineEdit_spillback")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nodeNameLineEdit_spillback)
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setObjectName("label_17")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.nodeXLineEdit_spillback = QtWidgets.QLineEdit(self.groupBox_5)
        self.nodeXLineEdit_spillback.setObjectName("nodeXLineEdit_spillback")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nodeXLineEdit_spillback)
        self.nodeYLineEdit_spillback = QtWidgets.QLineEdit(self.groupBox_5)
        self.nodeYLineEdit_spillback.setObjectName("nodeYLineEdit_spillback")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nodeYLineEdit_spillback)
        self.gridLayout_5.addLayout(self.formLayout_4, 1, 0, 1, 1)
        self.deleteNodeButton_spillback = QtWidgets.QPushButton(self.groupBox_5)
        self.deleteNodeButton_spillback.setAutoDefault(False)
        self.deleteNodeButton_spillback.setDefault(False)
        self.deleteNodeButton_spillback.setFlat(False)
        self.deleteNodeButton_spillback.setObjectName("deleteNodeButton_spillback")
        self.gridLayout_5.addWidget(self.deleteNodeButton_spillback, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_5, 0, 2, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.computeThinFlowPushButton_spillback = QtWidgets.QPushButton(self.tab_spillback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.computeThinFlowPushButton_spillback.sizePolicy().hasHeightForWidth())
        self.computeThinFlowPushButton_spillback.setSizePolicy(sizePolicy)
        self.computeThinFlowPushButton_spillback.setObjectName("computeThinFlowPushButton_spillback")
        self.gridLayout_6.addWidget(self.computeThinFlowPushButton_spillback, 1, 0, 1, 3)
        self.nodeSelectionListWidget_spillback = QtWidgets.QListWidget(self.tab_spillback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.nodeSelectionListWidget_spillback.sizePolicy().hasHeightForWidth())
        self.nodeSelectionListWidget_spillback.setSizePolicy(sizePolicy)
        self.nodeSelectionListWidget_spillback.setObjectName("nodeSelectionListWidget_spillback")
        self.gridLayout_6.addWidget(self.nodeSelectionListWidget_spillback, 0, 2, 1, 1)
        self.edgeSelectionListWidget_spillback = QtWidgets.QListWidget(self.tab_spillback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.edgeSelectionListWidget_spillback.sizePolicy().hasHeightForWidth())
        self.edgeSelectionListWidget_spillback.setSizePolicy(sizePolicy)
        self.edgeSelectionListWidget_spillback.setObjectName("edgeSelectionListWidget_spillback")
        self.gridLayout_6.addWidget(self.edgeSelectionListWidget_spillback, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 1, 1, 2)
        self.tabWidget.addTab(self.tab_spillback, "")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cleanUpCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.cleanUpCheckBox.setObjectName("cleanUpCheckBox")
        self.gridLayout_2.addWidget(self.cleanUpCheckBox, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 4, 1, 1)
        self.timeoutLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.timeoutLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeoutLineEdit.sizePolicy().hasHeightForWidth())
        self.timeoutLineEdit.setSizePolicy(sizePolicy)
        self.timeoutLineEdit.setObjectName("timeoutLineEdit")
        self.gridLayout_2.addWidget(self.timeoutLineEdit, 1, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.scipPathPushButton = QtWidgets.QPushButton(self.groupBox)
        self.scipPathPushButton.setObjectName("scipPathPushButton")
        self.gridLayout_2.addWidget(self.scipPathPushButton, 1, 2, 1, 1)
        self.timeoutLabel = QtWidgets.QLabel(self.groupBox)
        self.timeoutLabel.setEnabled(False)
        self.timeoutLabel.setObjectName("timeoutLabel")
        self.gridLayout_2.addWidget(self.timeoutLabel, 1, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.outputDirectoryLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.outputDirectoryLineEdit.setObjectName("outputDirectoryLineEdit")
        self.gridLayout_2.addWidget(self.outputDirectoryLineEdit, 0, 1, 1, 1)
        self.outputDirectoryPushButton = QtWidgets.QPushButton(self.groupBox)
        self.outputDirectoryPushButton.setObjectName("outputDirectoryPushButton")
        self.gridLayout_2.addWidget(self.outputDirectoryPushButton, 0, 2, 1, 1)
        self.inflowLineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inflowLineEdit.sizePolicy().hasHeightForWidth())
        self.inflowLineEdit.setSizePolicy(sizePolicy)
        self.inflowLineEdit.setObjectName("inflowLineEdit")
        self.gridLayout_2.addWidget(self.inflowLineEdit, 0, 5, 1, 1)
        self.templateComboBox = QtWidgets.QComboBox(self.groupBox)
        self.templateComboBox.setObjectName("templateComboBox")
        self.templateComboBox.addItem("")
        self.templateComboBox.addItem("")
        self.templateComboBox.addItem("")
        self.gridLayout_2.addWidget(self.templateComboBox, 3, 1, 1, 1)
        self.scipPathLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.scipPathLineEdit.setObjectName("scipPathLineEdit")
        self.gridLayout_2.addWidget(self.scipPathLineEdit, 1, 1, 1, 1)
        self.activateTimeoutCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.activateTimeoutCheckBox.setObjectName("activateTimeoutCheckBox")
        self.gridLayout_2.addWidget(self.activateTimeoutCheckBox, 1, 3, 1, 1)
        self.showEdgesWithoutFlowCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.showEdgesWithoutFlowCheckBox.setChecked(True)
        self.showEdgesWithoutFlowCheckBox.setObjectName("showEdgesWithoutFlowCheckBox")
        self.gridLayout_2.addWidget(self.showEdgesWithoutFlowCheckBox, 3, 5, 1, 1)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 885, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew_graph = QtWidgets.QAction(MainWindow)
        self.actionNew_graph.setObjectName("actionNew_graph")
        self.actionLoad_graph = QtWidgets.QAction(MainWindow)
        self.actionLoad_graph.setObjectName("actionLoad_graph")
        self.actionSave_graph = QtWidgets.QAction(MainWindow)
        self.actionSave_graph.setObjectName("actionSave_graph")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLoad_Thinflow = QtWidgets.QAction(MainWindow)
        self.actionLoad_Thinflow.setObjectName("actionLoad_Thinflow")
        self.actionSave_Thinflow = QtWidgets.QAction(MainWindow)
        self.actionSave_Thinflow.setObjectName("actionSave_Thinflow")
        self.actionOpen_NashFlowComputation = QtWidgets.QAction(MainWindow)
        self.actionOpen_NashFlowComputation.setObjectName("actionOpen_NashFlowComputation")
        self.actionMove_current_graph_to_NashFlowComputation = QtWidgets.QAction(MainWindow)
        self.actionMove_current_graph_to_NashFlowComputation.setObjectName("actionMove_current_graph_to_NashFlowComputation")
        self.menuFile.addAction(self.actionNew_graph)
        self.menuFile.addAction(self.actionLoad_graph)
        self.menuFile.addAction(self.actionSave_graph)
        self.menuFile.addAction(self.actionLoad_Thinflow)
        self.menuFile.addAction(self.actionSave_Thinflow)
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionOpen_NashFlowComputation)
        self.menuOptions.addAction(self.actionMove_current_graph_to_NashFlowComputation)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.capacityLineEdit_general)
        MainWindow.setTabOrder(self.capacityLineEdit_general, self.resettingSwitchButton_general)
        MainWindow.setTabOrder(self.resettingSwitchButton_general, self.updateEdgeButton_general)
        MainWindow.setTabOrder(self.updateEdgeButton_general, self.deleteEdgeButton_general)
        MainWindow.setTabOrder(self.deleteEdgeButton_general, self.nodeNameLineEdit_general)
        MainWindow.setTabOrder(self.nodeNameLineEdit_general, self.nodeXLineEdit_general)
        MainWindow.setTabOrder(self.nodeXLineEdit_general, self.nodeYLineEdit_general)
        MainWindow.setTabOrder(self.nodeYLineEdit_general, self.updateNodeButton_general)
        MainWindow.setTabOrder(self.updateNodeButton_general, self.deleteNodeButton_general)
        MainWindow.setTabOrder(self.deleteNodeButton_general, self.edgeSelectionListWidget_general)
        MainWindow.setTabOrder(self.edgeSelectionListWidget_general, self.nodeSelectionListWidget_general)
        MainWindow.setTabOrder(self.nodeSelectionListWidget_general, self.computeThinFlowPushButton_general)
        MainWindow.setTabOrder(self.computeThinFlowPushButton_general, self.outputDirectoryLineEdit)
        MainWindow.setTabOrder(self.outputDirectoryLineEdit, self.outputDirectoryPushButton)
        MainWindow.setTabOrder(self.outputDirectoryPushButton, self.scipPathLineEdit)
        MainWindow.setTabOrder(self.scipPathLineEdit, self.scipPathPushButton)
        MainWindow.setTabOrder(self.scipPathPushButton, self.templateComboBox)
        MainWindow.setTabOrder(self.templateComboBox, self.cleanUpCheckBox)
        MainWindow.setTabOrder(self.cleanUpCheckBox, self.inflowLineEdit)
        MainWindow.setTabOrder(self.inflowLineEdit, self.activateTimeoutCheckBox)
        MainWindow.setTabOrder(self.activateTimeoutCheckBox, self.timeoutLineEdit)
        MainWindow.setTabOrder(self.timeoutLineEdit, self.showEdgesWithoutFlowCheckBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ThinFlowComputation"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Node"))
        self.updateNodeButton_general.setText(_translate("MainWindow", "Update node"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "X-position"))
        self.label_3.setText(_translate("MainWindow", "Y-position"))
        self.deleteNodeButton_general.setText(_translate("MainWindow", "Delete node"))
        self.computeThinFlowPushButton_general.setText(_translate("MainWindow", "Compute Thin Flow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Edge"))
        self.label_7.setText(_translate("MainWindow", "Capacity"))
        self.label_6.setText(_translate("MainWindow", "Resetting"))
        self.resettingSwitchButton_general.setText(_translate("MainWindow", "Off"))
        self.updateEdgeButton_general.setText(_translate("MainWindow", "Update edge"))
        self.deleteEdgeButton_general.setText(_translate("MainWindow", "Delete edge"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), _translate("MainWindow", "General"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Edge"))
        self.label_14.setText(_translate("MainWindow", "Capacity"))
        self.label_19.setText(_translate("MainWindow", "Flow bound"))
        self.label_15.setText(_translate("MainWindow", "Resetting"))
        self.resettingSwitchButton_spillback.setText(_translate("MainWindow", "Off"))
        self.updateEdgeButton_spillback.setText(_translate("MainWindow", "Update edge"))
        self.deleteEdgeButton_spillback.setText(_translate("MainWindow", "Delete edge"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Node"))
        self.updateNodeButton_spillback.setText(_translate("MainWindow", "Update node"))
        self.label_16.setText(_translate("MainWindow", "Name"))
        self.label_17.setText(_translate("MainWindow", "X-position"))
        self.label_18.setText(_translate("MainWindow", "Y-position"))
        self.deleteNodeButton_spillback.setText(_translate("MainWindow", "Delete node"))
        self.computeThinFlowPushButton_spillback.setText(_translate("MainWindow", "Compute Spillback Thin Flow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_spillback), _translate("MainWindow", "Spillback"))
        self.groupBox.setTitle(_translate("MainWindow", "Config"))
        self.cleanUpCheckBox.setText(_translate("MainWindow", "Clean-up"))
        self.label_8.setText(_translate("MainWindow", "Inflow Rate"))
        self.timeoutLineEdit.setText(_translate("MainWindow", "300"))
        self.label_11.setText(_translate("MainWindow", "Algorithm & Template"))
        self.scipPathPushButton.setText(_translate("MainWindow", "Select binary"))
        self.timeoutLabel.setText(_translate("MainWindow", "Timeout (in s)"))
        self.label_12.setText(_translate("MainWindow", "SCIP path"))
        self.label_9.setText(_translate("MainWindow", "Output directory"))
        self.outputDirectoryPushButton.setText(_translate("MainWindow", "Select directory"))
        self.inflowLineEdit.setText(_translate("MainWindow", "0"))
        self.templateComboBox.setItemText(0, _translate("MainWindow", "1. Basic algorithm"))
        self.templateComboBox.setItemText(1, _translate("MainWindow", "2. Solve only one LP/IP"))
        self.templateComboBox.setItemText(2, _translate("MainWindow", "3. Advanced algorithm"))
        self.activateTimeoutCheckBox.setText(_translate("MainWindow", "Timeout"))
        self.showEdgesWithoutFlowCheckBox.setText(_translate("MainWindow", "Show edges w/out flow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionNew_graph.setText(_translate("MainWindow", "New graph"))
        self.actionLoad_graph.setText(_translate("MainWindow", "Load graph"))
        self.actionSave_graph.setText(_translate("MainWindow", "Save graph"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLoad_Thinflow.setText(_translate("MainWindow", "Load Thinflow"))
        self.actionSave_Thinflow.setText(_translate("MainWindow", "Save Thinflow"))
        self.actionOpen_NashFlowComputation.setText(_translate("MainWindow", "Open NashFlowComputation"))
        self.actionMove_current_graph_to_NashFlowComputation.setText(_translate("MainWindow", "Move current graph to NashFlowComputation"))

