# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Important\code\(Python)SampleSoftware\level.ui'
#
# Created: Wed Nov 14 14:05:59 2018
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(479, 467)
        Dialog.setModal(True)
        Dialog.setStyleSheet(_fromUtf8("#Dialog{border-image:url(./img/universe.jpg)}"))
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.widget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_high = QtGui.QPushButton(self.groupBox)
        self.pushButton_high.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Caslon Pro"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_high.setFont(font)
        self.pushButton_high.setObjectName(_fromUtf8("pushButton_high"))
        self.horizontalLayout.addWidget(self.pushButton_high)
        self.pushButton_middle = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_middle.sizePolicy().hasHeightForWidth())
        self.pushButton_middle.setSizePolicy(sizePolicy)
        self.pushButton_middle.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Caslon Pro"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_middle.setFont(font)
        self.pushButton_middle.setObjectName(_fromUtf8("pushButton_middle"))
        self.horizontalLayout.addWidget(self.pushButton_middle)
        self.pushButton_low = QtGui.QPushButton(self.groupBox)
        self.pushButton_low.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Caslon Pro"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_low.setFont(font)
        self.pushButton_low.setObjectName(_fromUtf8("pushButton_low"))
        self.horizontalLayout.addWidget(self.pushButton_low)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox1 = QtGui.QGroupBox(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        self.groupBox1.setFont(font)
        self.groupBox1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_culture = QtGui.QPushButton(self.groupBox1)
        self.pushButton_culture.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Caslon Pro"))
        font.setPointSize(16)
        self.pushButton_culture.setFont(font)
        self.pushButton_culture.setObjectName(_fromUtf8("pushButton_culture"))
        self.gridLayout.addWidget(self.pushButton_culture, 0, 1, 1, 1)
        self.pushButton_geo = QtGui.QPushButton(self.groupBox1)
        self.pushButton_geo.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Caslon Pro"))
        font.setPointSize(16)
        self.pushButton_geo.setFont(font)
        self.pushButton_geo.setObjectName(_fromUtf8("pushButton_geo"))
        self.gridLayout.addWidget(self.pushButton_geo, 1, 0, 1, 1)
        self.pushButton_history = QtGui.QPushButton(self.groupBox1)
        self.pushButton_history.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Caslon Pro"))
        font.setPointSize(16)
        self.pushButton_history.setFont(font)
        self.pushButton_history.setObjectName(_fromUtf8("pushButton_history"))
        self.gridLayout.addWidget(self.pushButton_history, 0, 0, 1, 1)
        self.pushButton_entertain = QtGui.QPushButton(self.groupBox1)
        self.pushButton_entertain.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Caslon Pro"))
        font.setPointSize(16)
        self.pushButton_entertain.setFont(font)
        self.pushButton_entertain.setObjectName(_fromUtf8("pushButton_entertain"))
        self.gridLayout.addWidget(self.pushButton_entertain, 0, 2, 1, 1)
        self.pushButton_sport = QtGui.QPushButton(self.groupBox1)
        self.pushButton_sport.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Caslon Pro"))
        font.setPointSize(16)
        self.pushButton_sport.setFont(font)
        self.pushButton_sport.setObjectName(_fromUtf8("pushButton_sport"))
        self.gridLayout.addWidget(self.pushButton_sport, 1, 2, 1, 1)
        self.pushButton_life = QtGui.QPushButton(self.groupBox1)
        self.pushButton_life.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Caslon Pro"))
        font.setPointSize(16)
        self.pushButton_life.setFont(font)
        self.pushButton_life.setObjectName(_fromUtf8("pushButton_life"))
        self.gridLayout.addWidget(self.pushButton_life, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_sure = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(12)
        self.pushButton_sure.setFont(font)
        self.pushButton_sure.setObjectName(_fromUtf8("pushButton_sure"))
        self.horizontalLayout_2.addWidget(self.pushButton_sure)
        self.pushButton_cancel = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(12)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 1)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "难度", None))
        self.pushButton_high.setText(_translate("Dialog", "高", None))
        self.pushButton_middle.setText(_translate("Dialog", "中", None))
        self.pushButton_low.setText(_translate("Dialog", "低", None))
        self.groupBox1.setTitle(_translate("Dialog", "科目", None))
        self.pushButton_culture.setText(_translate("Dialog", "文化", None))
        self.pushButton_geo.setText(_translate("Dialog", "地理", None))
        self.pushButton_history.setText(_translate("Dialog", "历史", None))
        self.pushButton_entertain.setText(_translate("Dialog", "娱乐", None))
        self.pushButton_sport.setText(_translate("Dialog", "体育", None))
        self.pushButton_life.setText(_translate("Dialog", "生活", None))
        self.pushButton_sure.setText(_translate("Dialog", "确认", None))
        self.pushButton_cancel.setText(_translate("Dialog", "取消", None))

