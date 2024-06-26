# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PV Validation_v2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1370, 789)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 130, 1321, 591))
        self.stackedWidget.setStyleSheet(u"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.Data_download_frame = QFrame(self.page)
        self.Data_download_frame.setObjectName(u"Data_download_frame")
        self.Data_download_frame.setGeometry(QRect(50, 30, 1221, 211))
        self.Data_download_frame.setStyleSheet(u"border:2px solid rgb(0, 0, 0);")
        self.Data_download_frame.setFrameShape(QFrame.StyledPanel)
        self.Data_download_frame.setFrameShadow(QFrame.Raised)
        self.Download_ZECMM772_TABLE = QPushButton(self.Data_download_frame)
        self.Download_ZECMM772_TABLE.setObjectName(u"Download_ZECMM772_TABLE")
        self.Download_ZECMM772_TABLE.setGeometry(QRect(270, 110, 111, 31))
        self.Download_ZECMM772_TABLE.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(255, 168, 17);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 219, 192);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Download_ZQRYFI_TABLE = QPushButton(self.Data_download_frame)
        self.Download_ZQRYFI_TABLE.setObjectName(u"Download_ZQRYFI_TABLE")
        self.Download_ZQRYFI_TABLE.setGeometry(QRect(110, 110, 111, 31))
        self.Download_ZQRYFI_TABLE.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(255, 168, 17);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 219, 192);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.LABEL_SAP = QLabel(self.Data_download_frame)
        self.LABEL_SAP.setObjectName(u"LABEL_SAP")
        self.LABEL_SAP.setGeometry(QRect(70, 80, 331, 21))
        self.LABEL_SAP.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 51, 97);\n"
"border:2px solid  rgb(0, 0, 0);\n"
"")
        self.LABEL_SAP.setAlignment(Qt.AlignCenter)
        self.LABEL_ENOVIA = QLabel(self.Data_download_frame)
        self.LABEL_ENOVIA.setObjectName(u"LABEL_ENOVIA")
        self.LABEL_ENOVIA.setGeometry(QRect(440, 80, 331, 21))
        self.LABEL_ENOVIA.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 51, 97);\n"
"border:2px solid  rgb(0, 0, 0);\n"
"")
        self.LABEL_ENOVIA.setAlignment(Qt.AlignCenter)
        self.Download_REP077_TABLE = QPushButton(self.Data_download_frame)
        self.Download_REP077_TABLE.setObjectName(u"Download_REP077_TABLE")
        self.Download_REP077_TABLE.setGeometry(QRect(540, 110, 111, 31))
        self.Download_REP077_TABLE.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(255, 168, 17);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 219, 192);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Download_Label_ZQRYFI = QLabel(self.Data_download_frame)
        self.Download_Label_ZQRYFI.setObjectName(u"Download_Label_ZQRYFI")
        self.Download_Label_ZQRYFI.setGeometry(QRect(80, 110, 21, 21))
        self.Download_Label_ZQRYFI.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.Download_Label_ZECMM772 = QLabel(self.Data_download_frame)
        self.Download_Label_ZECMM772.setObjectName(u"Download_Label_ZECMM772")
        self.Download_Label_ZECMM772.setGeometry(QRect(240, 110, 21, 21))
        self.Download_Label_ZECMM772.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.Download_Label_REP077 = QLabel(self.Data_download_frame)
        self.Download_Label_REP077.setObjectName(u"Download_Label_REP077")
        self.Download_Label_REP077.setGeometry(QRect(510, 110, 21, 21))
        self.Download_Label_REP077.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.LABEL_ENOVIA_2 = QLabel(self.Data_download_frame)
        self.LABEL_ENOVIA_2.setObjectName(u"LABEL_ENOVIA_2")
        self.LABEL_ENOVIA_2.setGeometry(QRect(810, 80, 371, 21))
        self.LABEL_ENOVIA_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 51, 97);\n"
"border:2px solid  rgb(0, 0, 0);\n"
"")
        self.LABEL_ENOVIA_2.setAlignment(Qt.AlignCenter)
        self.Refresh_tblRequestedtoCOE = QPushButton(self.Data_download_frame)
        self.Refresh_tblRequestedtoCOE.setObjectName(u"Refresh_tblRequestedtoCOE")
        self.Refresh_tblRequestedtoCOE.setGeometry(QRect(840, 110, 131, 31))
        self.Refresh_tblRequestedtoCOE.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 12px;\n"
"	background-color: rgb(255, 168, 17);\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 219, 192);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Refresh_PLC_Wave = QPushButton(self.Data_download_frame)
        self.Refresh_PLC_Wave.setObjectName(u"Refresh_PLC_Wave")
        self.Refresh_PLC_Wave.setGeometry(QRect(840, 150, 131, 31))
        self.Refresh_PLC_Wave.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(255, 168, 17);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 219, 192);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Refresh_Source_file_Process_Text = QPushButton(self.Data_download_frame)
        self.Refresh_Source_file_Process_Text.setObjectName(u"Refresh_Source_file_Process_Text")
        self.Refresh_Source_file_Process_Text.setGeometry(QRect(1010, 110, 161, 31))
        self.Refresh_Source_file_Process_Text.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(255, 168, 17);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 219, 192);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Refresh_Source_file_COEL_LORE = QPushButton(self.Data_download_frame)
        self.Refresh_Source_file_COEL_LORE.setObjectName(u"Refresh_Source_file_COEL_LORE")
        self.Refresh_Source_file_COEL_LORE.setGeometry(QRect(1010, 150, 161, 31))
        self.Refresh_Source_file_COEL_LORE.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(255, 168, 17);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 219, 192);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Refresh_Label_tblRequestedtoCOE = QLabel(self.Data_download_frame)
        self.Refresh_Label_tblRequestedtoCOE.setObjectName(u"Refresh_Label_tblRequestedtoCOE")
        self.Refresh_Label_tblRequestedtoCOE.setGeometry(QRect(810, 110, 21, 21))
        self.Refresh_Label_tblRequestedtoCOE.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.Refresh_Label_Source_file_Process_Text = QLabel(self.Data_download_frame)
        self.Refresh_Label_Source_file_Process_Text.setObjectName(u"Refresh_Label_Source_file_Process_Text")
        self.Refresh_Label_Source_file_Process_Text.setGeometry(QRect(980, 110, 21, 21))
        self.Refresh_Label_Source_file_Process_Text.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.Refresh_Label_Source_file_COEL_LORE = QLabel(self.Data_download_frame)
        self.Refresh_Label_Source_file_COEL_LORE.setObjectName(u"Refresh_Label_Source_file_COEL_LORE")
        self.Refresh_Label_Source_file_COEL_LORE.setGeometry(QRect(980, 150, 21, 21))
        self.Refresh_Label_Source_file_COEL_LORE.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.Refresh_Label_PLC_Wave = QLabel(self.Data_download_frame)
        self.Refresh_Label_PLC_Wave.setObjectName(u"Refresh_Label_PLC_Wave")
        self.Refresh_Label_PLC_Wave.setGeometry(QRect(810, 150, 21, 21))
        self.Refresh_Label_PLC_Wave.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.Download_Reports_All = QPushButton(self.Data_download_frame)
        self.Download_Reports_All.setObjectName(u"Download_Reports_All")
        self.Download_Reports_All.setGeometry(QRect(140, 20, 941, 41))
        self.Download_Reports_All.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(85, 0, 0);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(255, 168, 17);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Check_Input_Folder = QPushButton(self.Data_download_frame)
        self.Check_Input_Folder.setObjectName(u"Check_Input_Folder")
        self.Check_Input_Folder.setGeometry(QRect(1090, 20, 121, 41))
        self.Check_Input_Folder.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"font:10pt;\n"
"}")
        self.Data_Preprocessing_frame = QFrame(self.page)
        self.Data_Preprocessing_frame.setObjectName(u"Data_Preprocessing_frame")
        self.Data_Preprocessing_frame.setGeometry(QRect(50, 300, 561, 281))
        self.Data_Preprocessing_frame.setStyleSheet(u"border:2px solid rgb(0, 0, 0);")
        self.Data_Preprocessing_frame.setFrameShape(QFrame.StyledPanel)
        self.Data_Preprocessing_frame.setFrameShadow(QFrame.Raised)
        self.Generate_ZQRYFI_Consolidate = QPushButton(self.Data_Preprocessing_frame)
        self.Generate_ZQRYFI_Consolidate.setObjectName(u"Generate_ZQRYFI_Consolidate")
        self.Generate_ZQRYFI_Consolidate.setGeometry(QRect(60, 110, 291, 31))
        self.Generate_ZQRYFI_Consolidate.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(0, 132, 193);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color:rgb(109, 172, 222);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Generate_C223_LCO = QPushButton(self.Data_Preprocessing_frame)
        self.Generate_C223_LCO.setObjectName(u"Generate_C223_LCO")
        self.Generate_C223_LCO.setGeometry(QRect(60, 180, 291, 31))
        self.Generate_C223_LCO.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(0, 132, 193);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color:rgb(109, 172, 222);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Generate_ALL_Consolidate = QPushButton(self.Data_Preprocessing_frame)
        self.Generate_ALL_Consolidate.setObjectName(u"Generate_ALL_Consolidate")
        self.Generate_ALL_Consolidate.setGeometry(QRect(110, 20, 341, 41))
        self.Generate_ALL_Consolidate.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(0, 132, 193);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(82, 130, 167);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Generate_Label_ZQRYFI_Consolidate = QLabel(self.Data_Preprocessing_frame)
        self.Generate_Label_ZQRYFI_Consolidate.setObjectName(u"Generate_Label_ZQRYFI_Consolidate")
        self.Generate_Label_ZQRYFI_Consolidate.setGeometry(QRect(30, 110, 21, 21))
        self.Generate_Label_ZQRYFI_Consolidate.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.Generate_Label_LCO_C223 = QLabel(self.Data_Preprocessing_frame)
        self.Generate_Label_LCO_C223.setObjectName(u"Generate_Label_LCO_C223")
        self.Generate_Label_LCO_C223.setGeometry(QRect(30, 180, 21, 21))
        self.Generate_Label_LCO_C223.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.LABEL_ZQRYFI_Consolidate = QLabel(self.Data_Preprocessing_frame)
        self.LABEL_ZQRYFI_Consolidate.setObjectName(u"LABEL_ZQRYFI_Consolidate")
        self.LABEL_ZQRYFI_Consolidate.setGeometry(QRect(30, 80, 501, 21))
        self.LABEL_ZQRYFI_Consolidate.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 51, 97);\n"
"border:2px solid  rgb(0, 0, 0);\n"
"")
        self.LABEL_ZQRYFI_Consolidate.setAlignment(Qt.AlignCenter)
        self.LABEL_ZQRFYI_Consolidate_2 = QLabel(self.Data_Preprocessing_frame)
        self.LABEL_ZQRFYI_Consolidate_2.setObjectName(u"LABEL_ZQRFYI_Consolidate_2")
        self.LABEL_ZQRFYI_Consolidate_2.setGeometry(QRect(30, 150, 501, 20))
        self.LABEL_ZQRFYI_Consolidate_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 51, 97);\n"
"border:2px solid  rgb(0, 0, 0);\n"
"")
        self.LABEL_ZQRFYI_Consolidate_2.setAlignment(Qt.AlignCenter)
        self.Check_Generate_ZQRYFI_Consolidate = QPushButton(self.Data_Preprocessing_frame)
        self.Check_Generate_ZQRYFI_Consolidate.setObjectName(u"Check_Generate_ZQRYFI_Consolidate")
        self.Check_Generate_ZQRYFI_Consolidate.setGeometry(QRect(360, 110, 171, 31))
        self.Check_Generate_ZQRYFI_Consolidate.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"font:10pt;\n"
"}")
        self.Check_Generate_C223 = QPushButton(self.Data_Preprocessing_frame)
        self.Check_Generate_C223.setObjectName(u"Check_Generate_C223")
        self.Check_Generate_C223.setGeometry(QRect(360, 180, 91, 31))
        self.Check_Generate_C223.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"font:10pt;\n"
"}")
        self.Check_Generate_LCO = QPushButton(self.Data_Preprocessing_frame)
        self.Check_Generate_LCO.setObjectName(u"Check_Generate_LCO")
        self.Check_Generate_LCO.setGeometry(QRect(360, 220, 91, 31))
        self.Check_Generate_LCO.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"font:10pt;\n"
"}")
        self.LABEL_Import_3 = QLabel(self.page)
        self.LABEL_Import_3.setObjectName(u"LABEL_Import_3")
        self.LABEL_Import_3.setGeometry(QRect(80, 10, 161, 31))
        self.LABEL_Import_3.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(223, 223, 223);\n"
"color: rgb(0, 0, 0);\n"
"border:2px solid  rgb(0, 0, 0);\n"
"")
        self.LABEL_Import_3.setAlignment(Qt.AlignCenter)
        self.LABEL_DataPreprocessing = QLabel(self.page)
        self.LABEL_DataPreprocessing.setObjectName(u"LABEL_DataPreprocessing")
        self.LABEL_DataPreprocessing.setGeometry(QRect(80, 280, 161, 31))
        self.LABEL_DataPreprocessing.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(223, 223, 223);\n"
"border:2px solid  rgb(0, 0, 0);\n"
"")
        self.LABEL_DataPreprocessing.setAlignment(Qt.AlignCenter)
        self.LABEL_SAP_Update = QLabel(self.page)
        self.LABEL_SAP_Update.setObjectName(u"LABEL_SAP_Update")
        self.LABEL_SAP_Update.setGeometry(QRect(720, 280, 161, 31))
        self.LABEL_SAP_Update.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(223, 223, 223);\n"
"border:2px solid  rgb(0, 0, 0);\n"
"")
        self.LABEL_SAP_Update.setAlignment(Qt.AlignCenter)
        self.SAP_Update_frame = QFrame(self.page)
        self.SAP_Update_frame.setObjectName(u"SAP_Update_frame")
        self.SAP_Update_frame.setGeometry(QRect(690, 300, 581, 281))
        self.SAP_Update_frame.setStyleSheet(u"border:2px solid rgb(0, 0, 0);")
        self.SAP_Update_frame.setFrameShape(QFrame.StyledPanel)
        self.SAP_Update_frame.setFrameShadow(QFrame.Raised)
        self.Update_via_C223 = QPushButton(self.SAP_Update_frame)
        self.Update_via_C223.setObjectName(u"Update_via_C223")
        self.Update_via_C223.setGeometry(QRect(80, 70, 271, 41))
        self.Update_via_C223.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(109, 154, 69);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(191, 215, 48);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.SAP_Label_C223 = QLabel(self.SAP_Update_frame)
        self.SAP_Label_C223.setObjectName(u"SAP_Label_C223")
        self.SAP_Label_C223.setGeometry(QRect(50, 80, 21, 21))
        self.SAP_Label_C223.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.SAP_Label_LCO = QLabel(self.SAP_Update_frame)
        self.SAP_Label_LCO.setObjectName(u"SAP_Label_LCO")
        self.SAP_Label_LCO.setGeometry(QRect(50, 130, 21, 21))
        self.SAP_Label_LCO.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.Update_via_LCO = QPushButton(self.SAP_Update_frame)
        self.Update_via_LCO.setObjectName(u"Update_via_LCO")
        self.Update_via_LCO.setGeometry(QRect(80, 120, 271, 41))
        self.Update_via_LCO.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(109, 154, 69);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(191, 215, 48);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.Check_Update_Result = QPushButton(self.SAP_Update_frame)
        self.Check_Update_Result.setObjectName(u"Check_Update_Result")
        self.Check_Update_Result.setGeometry(QRect(80, 180, 131, 31))
        self.Check_Update_Result.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"font:10pt;\n"
"}")
        self.Check_Output_Folder = QPushButton(self.SAP_Update_frame)
        self.Check_Output_Folder.setObjectName(u"Check_Output_Folder")
        self.Check_Output_Folder.setGeometry(QRect(230, 180, 121, 31))
        self.Check_Output_Folder.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"font:10pt;\n"
"}")
        self.Label_AutiomationScript = QLabel(self.SAP_Update_frame)
        self.Label_AutiomationScript.setObjectName(u"Label_AutiomationScript")
        self.Label_AutiomationScript.setGeometry(QRect(30, 30, 521, 21))
        self.Label_AutiomationScript.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 51, 97);\n"
"border:2px solid  rgb(0, 0, 0);\n"
"")
        self.Label_AutiomationScript.setAlignment(Qt.AlignCenter)
        self.End_Task = QPushButton(self.SAP_Update_frame)
        self.End_Task.setObjectName(u"End_Task")
        self.End_Task.setGeometry(QRect(80, 230, 271, 31))
        self.End_Task.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(167, 167, 167);\n"
"border-radius: 6px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"font:10pt;\n"
"}")
        self.Rename_End_Task = QLabel(self.SAP_Update_frame)
        self.Rename_End_Task.setObjectName(u"Rename_End_Task")
        self.Rename_End_Task.setGeometry(QRect(130, 230, 21, 21))
        self.Rename_End_Task.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        self.Display_Manual_Start = QLineEdit(self.SAP_Update_frame)
        self.Display_Manual_Start.setObjectName(u"Display_Manual_Start")
        self.Display_Manual_Start.setGeometry(QRect(440, 90, 111, 21))
        self.Display_Manual_Start.setStyleSheet(u"border:1px solid rgb(0, 0, 0);")
        self.Button_Manual_Start = QPushButton(self.SAP_Update_frame)
        self.Button_Manual_Start.setObjectName(u"Button_Manual_Start")
        self.Button_Manual_Start.setGeometry(QRect(390, 90, 51, 21))
        self.Button_Manual_Start.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(6, 249, 233);\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"background-color: rgb(43, 255, 209);\n"
"font:10pt;\n"
"}")
        self.Button_Manual_End = QPushButton(self.SAP_Update_frame)
        self.Button_Manual_End.setObjectName(u"Button_Manual_End")
        self.Button_Manual_End.setGeometry(QRect(390, 110, 51, 21))
        self.Button_Manual_End.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(6, 249, 233);\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"background-color: rgb(43, 255, 209);\n"
"font:10pt;\n"
"}")
        self.Display_Manual_End = QLineEdit(self.SAP_Update_frame)
        self.Display_Manual_End.setObjectName(u"Display_Manual_End")
        self.Display_Manual_End.setGeometry(QRect(440, 110, 111, 21))
        self.Display_Manual_End.setStyleSheet(u"border:1px solid rgb(0, 0, 0);")
        self.Display_Manual_Process = QLineEdit(self.SAP_Update_frame)
        self.Display_Manual_Process.setObjectName(u"Display_Manual_Process")
        self.Display_Manual_Process.setGeometry(QRect(470, 130, 81, 21))
        self.Display_Manual_Process.setStyleSheet(u"border:1px solid rgb(0, 0, 0);")
        self.LABEL_Manual_Processing_Time = QLabel(self.SAP_Update_frame)
        self.LABEL_Manual_Processing_Time.setObjectName(u"LABEL_Manual_Processing_Time")
        self.LABEL_Manual_Processing_Time.setGeometry(QRect(390, 70, 161, 21))
        self.LABEL_Manual_Processing_Time.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(39, 125, 255);\n"
"border-radius: 1px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"font:10pt;")
        self.LABEL_Manual_Processing_Time.setAlignment(Qt.AlignCenter)
        self.LABEL_Manual_Processing_Time_2 = QLabel(self.SAP_Update_frame)
        self.LABEL_Manual_Processing_Time_2.setObjectName(u"LABEL_Manual_Processing_Time_2")
        self.LABEL_Manual_Processing_Time_2.setGeometry(QRect(390, 130, 81, 21))
        self.LABEL_Manual_Processing_Time_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(58, 203, 255);\n"
"border-radius: 1px;\n"
"border:1px solid  rgb(0, 0, 0);\n"
"font:10pt;")
        self.LABEL_Manual_Processing_Time_2.setAlignment(Qt.AlignCenter)
        self.Display_Processing_Time = QLineEdit(self.page)
        self.Display_Processing_Time.setObjectName(u"Display_Processing_Time")
        self.Display_Processing_Time.setGeometry(QRect(550, 270, 61, 21))
        self.Display_Download_Time = QLineEdit(self.page)
        self.Display_Download_Time.setObjectName(u"Display_Download_Time")
        self.Display_Download_Time.setGeometry(QRect(1200, 0, 61, 21))
        self.Display_Update_Time_C223 = QLineEdit(self.page)
        self.Display_Update_Time_C223.setObjectName(u"Display_Update_Time_C223")
        self.Display_Update_Time_C223.setGeometry(QRect(1020, 270, 61, 21))
        self.Label_Process_Time = QLabel(self.page)
        self.Label_Process_Time.setObjectName(u"Label_Process_Time")
        self.Label_Process_Time.setGeometry(QRect(430, 270, 141, 21))
        self.Label_Process_Time.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")
        self.Label_Process_Time.setAlignment(Qt.AlignCenter)
        self.Label_Process_Time_2 = QLabel(self.page)
        self.Label_Process_Time_2.setObjectName(u"Label_Process_Time_2")
        self.Label_Process_Time_2.setGeometry(QRect(1010, 0, 271, 21))
        self.Label_Process_Time_2.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")
        self.Label_Process_Time_2.setAlignment(Qt.AlignCenter)
        self.Label_Process_Time_3 = QLabel(self.page)
        self.Label_Process_Time_3.setObjectName(u"Label_Process_Time_3")
        self.Label_Process_Time_3.setGeometry(QRect(890, 270, 131, 21))
        self.Label_Process_Time_3.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")
        self.Label_Process_Time_3.setAlignment(Qt.AlignCenter)
        self.Label_Process_Time_4 = QLabel(self.page)
        self.Label_Process_Time_4.setObjectName(u"Label_Process_Time_4")
        self.Label_Process_Time_4.setGeometry(QRect(1090, 270, 131, 21))
        self.Label_Process_Time_4.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")
        self.Label_Process_Time_4.setAlignment(Qt.AlignCenter)
        self.Display_Update_Time_LCO = QLineEdit(self.page)
        self.Display_Update_Time_LCO.setObjectName(u"Display_Update_Time_LCO")
        self.Display_Update_Time_LCO.setGeometry(QRect(1220, 270, 61, 21))
        self.stackedWidget.addWidget(self.page)
        self.Data_Preprocessing_frame.raise_()
        self.Data_download_frame.raise_()
        self.LABEL_Import_3.raise_()
        self.LABEL_DataPreprocessing.raise_()
        self.SAP_Update_frame.raise_()
        self.LABEL_SAP_Update.raise_()
        self.Display_Processing_Time.raise_()
        self.Display_Download_Time.raise_()
        self.Display_Update_Time_C223.raise_()
        self.Label_Process_Time.raise_()
        self.Label_Process_Time_2.raise_()
        self.Label_Process_Time_3.raise_()
        self.Label_Process_Time_4.raise_()
        self.Display_Update_Time_LCO.raise_()
        self.Stop_GUI_button = QPushButton(self.centralwidget)
        self.Stop_GUI_button.setObjectName(u"Stop_GUI_button")
        self.Stop_GUI_button.setGeometry(QRect(1230, 40, 111, 41))
        self.Stop_GUI_button.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(97, 97, 145);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255,255,255);\n"
"border-radius: 8px;\n"
"background-color: rgb(63, 63, 95);\n"
"border:1px solid  rgb(255, 255, 255);\n"
"font:10pt;\n"
"}")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(0, 0, 1371, 791))
        self.listView.setStyleSheet(u"")
        self.Upload_SP_button = QPushButton(self.centralwidget)
        self.Upload_SP_button.setObjectName(u"Upload_SP_button")
        self.Upload_SP_button.setGeometry(QRect(1060, 40, 141, 41))
        self.Upload_SP_button.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(85, 85, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"color:  rgb(0, 0, 0);\n"
"border-radius: 8px;\n"
"background-color :rgb(98, 161, 255);\n"
"font:10pt;\n"
"}")
        self.Upload_SP_Label = QLabel(self.centralwidget)
        self.Upload_SP_Label.setObjectName(u"Upload_SP_Label")
        self.Upload_SP_Label.setGeometry(QRect(1030, 50, 21, 21))
        self.Upload_SP_Label.setStyleSheet(u"border: rgba(0, 0, 0, 0);\n"
"background-color:rgba(0, 0, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.listView.raise_()
        self.stackedWidget.raise_()
        self.Stop_GUI_button.raise_()
        self.Upload_SP_button.raise_()
        self.Upload_SP_Label.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Download_ZECMM772_TABLE.setText(QCoreApplication.translate("MainWindow", u"ZECMM772", None))
        self.Download_ZQRYFI_TABLE.setText(QCoreApplication.translate("MainWindow", u"ZQRYFI", None))
        self.LABEL_SAP.setText(QCoreApplication.translate("MainWindow", u"SAP Download", None))
        self.LABEL_ENOVIA.setText(QCoreApplication.translate("MainWindow", u"Enovia Download", None))
        self.Download_REP077_TABLE.setText(QCoreApplication.translate("MainWindow", u"REP-D077", None))
        self.Download_Label_ZQRYFI.setText("")
        self.Download_Label_ZECMM772.setText("")
        self.Download_Label_REP077.setText("")
        self.LABEL_ENOVIA_2.setText(QCoreApplication.translate("MainWindow", u"SharePoint Download", None))
        self.Refresh_tblRequestedtoCOE.setText(QCoreApplication.translate("MainWindow", u"tblRequestedtoCOE", None))
        self.Refresh_PLC_Wave.setText(QCoreApplication.translate("MainWindow", u"PLC Wave", None))
        self.Refresh_Source_file_Process_Text.setText(QCoreApplication.translate("MainWindow", u" Source_file_Process_Text", None))
        self.Refresh_Source_file_COEL_LORE.setText(QCoreApplication.translate("MainWindow", u" Source_file_COEL_LORE", None))
        self.Refresh_Label_tblRequestedtoCOE.setText("")
        self.Refresh_Label_Source_file_Process_Text.setText("")
        self.Refresh_Label_Source_file_COEL_LORE.setText("")
        self.Refresh_Label_PLC_Wave.setText("")
        self.Download_Reports_All.setText(QCoreApplication.translate("MainWindow", u"Download All Reports", None))
        self.Check_Input_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Input Folder", None))
        self.Generate_ZQRYFI_Consolidate.setText(QCoreApplication.translate("MainWindow", u"Generate ZQRYFI Condolidate File", None))
        self.Generate_C223_LCO.setText(QCoreApplication.translate("MainWindow", u"Generate C223 / LCO to be updated", None))
        self.Generate_ALL_Consolidate.setText(QCoreApplication.translate("MainWindow", u"Generate ALL Reports", None))
        self.Generate_Label_ZQRYFI_Consolidate.setText("")
        self.Generate_Label_LCO_C223.setText("")
        self.LABEL_ZQRYFI_Consolidate.setText(QCoreApplication.translate("MainWindow", u"ZQRYFI Consolidate", None))
        self.LABEL_ZQRFYI_Consolidate_2.setText(QCoreApplication.translate("MainWindow", u"SAP Update Reference", None))
        self.Check_Generate_ZQRYFI_Consolidate.setText(QCoreApplication.translate("MainWindow", u"Open Consolidated ZQRYFI", None))
        self.Check_Generate_C223.setText(QCoreApplication.translate("MainWindow", u"Open C223", None))
        self.Check_Generate_LCO.setText(QCoreApplication.translate("MainWindow", u"Open LCO", None))
        self.LABEL_Import_3.setText(QCoreApplication.translate("MainWindow", u"Download Data", None))
        self.LABEL_DataPreprocessing.setText(QCoreApplication.translate("MainWindow", u"Data Preprocessing", None))
        self.LABEL_SAP_Update.setText(QCoreApplication.translate("MainWindow", u"SAP Update", None))
        self.Update_via_C223.setText(QCoreApplication.translate("MainWindow", u"Update via C223", None))
        self.SAP_Label_C223.setText("")
        self.SAP_Label_LCO.setText("")
        self.Update_via_LCO.setText(QCoreApplication.translate("MainWindow", u"Update via LCO", None))
        self.Check_Update_Result.setText(QCoreApplication.translate("MainWindow", u"Open Update Result", None))
        self.Check_Output_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Output Folder", None))
        self.Label_AutiomationScript.setText(QCoreApplication.translate("MainWindow", u"SAP Automation Script", None))
        self.End_Task.setText(QCoreApplication.translate("MainWindow", u"End Task - File Name Update", None))
        self.Rename_End_Task.setText("")
        self.Button_Manual_Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Button_Manual_End.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.LABEL_Manual_Processing_Time.setText(QCoreApplication.translate("MainWindow", u"Manual Processing", None))
        self.LABEL_Manual_Processing_Time_2.setText(QCoreApplication.translate("MainWindow", u"Total TPT", None))
        self.Label_Process_Time.setText(QCoreApplication.translate("MainWindow", u"Processing Time: ", None))
        self.Label_Process_Time_2.setText(QCoreApplication.translate("MainWindow", u"Processing Time: ", None))
        self.Label_Process_Time_3.setText(QCoreApplication.translate("MainWindow", u"C223 Processing Time: ", None))
        self.Label_Process_Time_4.setText(QCoreApplication.translate("MainWindow", u"LCO Processing Time: ", None))
        self.Stop_GUI_button.setText(QCoreApplication.translate("MainWindow", u"Stop GUI", None))
        self.Upload_SP_button.setText(QCoreApplication.translate("MainWindow", u"Upload to SharePoint", None))
        self.Upload_SP_Label.setText("")
    # retranslateUi

