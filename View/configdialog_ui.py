# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/justinvieira/Documents/ezdmb/View/configdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName("ConfigDialog")
        ConfigDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ConfigDialog.resize(1058, 1023)
        ConfigDialog.setMinimumSize(QtCore.QSize(1054, 992))
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(ConfigDialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.importTab = QtWidgets.QTabWidget(ConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importTab.sizePolicy().hasHeightForWidth())
        self.importTab.setSizePolicy(sizePolicy)
        self.importTab.setMinimumSize(QtCore.QSize(1042, 928))
        self.importTab.setObjectName("importTab")
        self.tab_basic = QtWidgets.QWidget()
        self.tab_basic.setObjectName("tab_basic")
        self.groupBox = QtWidgets.QGroupBox(self.tab_basic)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1020, 885))
        self.groupBox.setMinimumSize(QtCore.QSize(1020, 885))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.use_html_file_check = QtWidgets.QCheckBox(self.groupBox)
        self.use_html_file_check.setGeometry(QtCore.QRect(30, 300, 951, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_html_file_check.sizePolicy().hasHeightForWidth())
        self.use_html_file_check.setSizePolicy(sizePolicy)
        self.use_html_file_check.setMinimumSize(QtCore.QSize(951, 241))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.use_html_file_check.setFont(font)
        self.use_html_file_check.setObjectName("use_html_file_check")
        self.use_images_check = QtWidgets.QCheckBox(self.groupBox)
        self.use_images_check.setGeometry(QtCore.QRect(30, 40, 981, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_images_check.sizePolicy().hasHeightForWidth())
        self.use_images_check.setSizePolicy(sizePolicy)
        self.use_images_check.setMinimumSize(QtCore.QSize(981, 241))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.use_images_check.setFont(font)
        self.use_images_check.setObjectName("use_images_check")
        self.use_menu_data_check = QtWidgets.QCheckBox(self.groupBox)
        self.use_menu_data_check.setGeometry(QtCore.QRect(30, 560, 991, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_menu_data_check.sizePolicy().hasHeightForWidth())
        self.use_menu_data_check.setSizePolicy(sizePolicy)
        self.use_menu_data_check.setMinimumSize(QtCore.QSize(981, 0))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.use_menu_data_check.setFont(font)
        self.use_menu_data_check.setObjectName("use_menu_data_check")
        self.importTab.addTab(self.tab_basic, "")
        self.tab_images = QtWidgets.QWidget()
        self.tab_images.setObjectName("tab_images")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_images)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 10, 1021, 121))
        self.groupBox_2.setMinimumSize(QtCore.QSize(1021, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(490, 30, 511, 71))
        self.label.setMinimumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.rotateTimeBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.rotateTimeBox.setGeometry(QtCore.QRect(310, 50, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotateTimeBox.sizePolicy().hasHeightForWidth())
        self.rotateTimeBox.setSizePolicy(sizePolicy)
        self.rotateTimeBox.setMinimumSize(QtCore.QSize(71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rotateTimeBox.setFont(font)
        self.rotateTimeBox.setDecimals(1)
        self.rotateTimeBox.setMinimum(0.5)
        self.rotateTimeBox.setMaximum(30.0)
        self.rotateTimeBox.setObjectName("rotateTimeBox")
        self.rotate_images_check = QtWidgets.QCheckBox(self.groupBox_2)
        self.rotate_images_check.setGeometry(QtCore.QRect(30, 30, 271, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_images_check.sizePolicy().hasHeightForWidth())
        self.rotate_images_check.setSizePolicy(sizePolicy)
        self.rotate_images_check.setMinimumSize(QtCore.QSize(271, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rotate_images_check.setFont(font)
        self.rotate_images_check.setObjectName("rotate_images_check")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_images)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 140, 1021, 601))
        self.groupBox_3.setMinimumSize(QtCore.QSize(1021, 601))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 971, 61))
        self.label_2.setMinimumSize(QtCore.QSize(971, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.loadedContentWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.loadedContentWidget.setGeometry(QtCore.QRect(20, 100, 991, 271))
        self.loadedContentWidget.setMinimumSize(QtCore.QSize(991, 271))
        self.loadedContentWidget.setObjectName("loadedContentWidget")
        self.deleteSelectionButton = QtWidgets.QPushButton(self.groupBox_3)
        self.deleteSelectionButton.setGeometry(QtCore.QRect(570, 400, 281, 81))
        self.deleteSelectionButton.setMinimumSize(QtCore.QSize(261, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteSelectionButton.setFont(font)
        self.deleteSelectionButton.setObjectName("deleteSelectionButton")
        self.addImageButton = QtWidgets.QPushButton(self.groupBox_3)
        self.addImageButton.setGeometry(QtCore.QRect(170, 400, 291, 81))
        self.addImageButton.setMinimumSize(QtCore.QSize(271, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addImageButton.setFont(font)
        self.addImageButton.setObjectName("addImageButton")
        self.importTab.addTab(self.tab_images, "")
        self.tab_import = QtWidgets.QWidget()
        self.tab_import.setObjectName("tab_import")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_import)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 851, 661))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.menuLbl = QtWidgets.QLabel(self.groupBox_5)
        self.menuLbl.setGeometry(QtCore.QRect(20, 40, 811, 601))
        self.menuLbl.setText("")
        self.menuLbl.setObjectName("menuLbl")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_import)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 680, 851, 201))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.importButton = QtWidgets.QPushButton(self.groupBox_6)
        self.importButton.setGeometry(QtCore.QRect(30, 50, 791, 131))
        self.importButton.setObjectName("importButton")
        self.importTab.addTab(self.tab_import, "")
        self.verticalLayout_6.addWidget(self.importTab)
        self.groupBox_4 = QtWidgets.QGroupBox(ConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(1040, 90))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.okCancelButtonBox = QtWidgets.QDialogButtonBox(self.groupBox_4)
        self.okCancelButtonBox.setGeometry(QtCore.QRect(-10, 20, 1040, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okCancelButtonBox.sizePolicy().hasHeightForWidth())
        self.okCancelButtonBox.setSizePolicy(sizePolicy)
        self.okCancelButtonBox.setMinimumSize(QtCore.QSize(1040, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.okCancelButtonBox.setFont(font)
        self.okCancelButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.okCancelButtonBox.setCenterButtons(False)
        self.okCancelButtonBox.setObjectName("okCancelButtonBox")
        self.verticalLayout_6.addWidget(self.groupBox_4)

        self.retranslateUi(ConfigDialog)
        self.importTab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigDialog.setWindowTitle(_translate("ConfigDialog", "Settings"))
        self.groupBox.setTitle(_translate("ConfigDialog", "Content"))
        self.use_html_file_check.setText(_translate("ConfigDialog", "Use HTML files"))
        self.use_images_check.setText(_translate("ConfigDialog", "Use images"))
        self.use_menu_data_check.setText(_translate("ConfigDialog", "Use menu data import"))
        self.importTab.setTabText(self.importTab.indexOf(self.tab_basic), _translate("ConfigDialog", "Basic"))
        self.groupBox_2.setTitle(_translate("ConfigDialog", "Rotation settings"))
        self.label.setText(_translate("ConfigDialog", "minutes"))
        self.rotate_images_check.setText(_translate("ConfigDialog", " Rotate content every"))
        self.groupBox_3.setTitle(_translate("ConfigDialog", "Add/Remove"))
        self.label_2.setText(_translate("ConfigDialog", "Loaded content:"))
        self.deleteSelectionButton.setText(_translate("ConfigDialog", "Delete Selection"))
        self.addImageButton.setText(_translate("ConfigDialog", "Add Content"))
        self.importTab.setTabText(self.importTab.indexOf(self.tab_images), _translate("ConfigDialog", "Content"))
        self.groupBox_5.setTitle(_translate("ConfigDialog", "Current Imported Menu Data"))
        self.groupBox_6.setTitle(_translate("ConfigDialog", "Import Menu Data"))
        self.importButton.setText(_translate("ConfigDialog", "Import from file"))
        self.importTab.setTabText(self.importTab.indexOf(self.tab_import), _translate("ConfigDialog", "Import"))
