# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NBA_Player_Stats_UI_V01IuHTOP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NBA_Player_Stats(object):
    def setupUi(self, NBA_Player_Stats):
        if not NBA_Player_Stats.objectName():
            NBA_Player_Stats.setObjectName(u"NBA_Player_Stats")
        NBA_Player_Stats.resize(1269, 712)
        self.Reset_Button = QPushButton(NBA_Player_Stats)
        self.Reset_Button.setObjectName(u"Reset_Button")
        self.Reset_Button.setEnabled(True)
        self.Reset_Button.setGeometry(QRect(160, 70, 91, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Reset_Button.setFont(font)
        self.List_Label = QLabel(NBA_Player_Stats)
        self.List_Label.setObjectName(u"List_Label")
        self.List_Label.setGeometry(QRect(30, 170, 301, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.List_Label.setFont(font1)
        self.List_Label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.WillyF_Label = QLabel(NBA_Player_Stats)
        self.WillyF_Label.setObjectName(u"WillyF_Label")
        self.WillyF_Label.setGeometry(QRect(10, 680, 411, 31))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.WillyF_Label.setFont(font2)
        self.WillyF_Label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Pic_Label = QLabel(NBA_Player_Stats)
        self.Pic_Label.setObjectName(u"Pic_Label")
        self.Pic_Label.setGeometry(QRect(30, 30, 81, 81))
        self.Pic_Label.setFont(font1)
        self.Pic_Label.setFrameShape(QFrame.NoFrame)
        self.Pic_Label.setAlignment(Qt.AlignCenter)
        self.Player_ComboBox = QComboBox(NBA_Player_Stats)
        self.Player_ComboBox.addItem("")
        self.Player_ComboBox.setObjectName(u"Player_ComboBox")
        self.Player_ComboBox.setGeometry(QRect(220, 170, 321, 41))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        self.Player_ComboBox.setFont(font3)
        self.Player_ComboBox.setMaxVisibleItems(15)
        self.Info_Table = QTableWidget(NBA_Player_Stats)
        self.Info_Table.setObjectName(u"Info_Table")
        self.Info_Table.setGeometry(QRect(30, 310, 1221, 361))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        self.Info_Table.setFont(font4)
        self.Info_Table.setAlternatingRowColors(False)
        self.label_4 = QLabel(NBA_Player_Stats)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 250, 411, 41))
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.MarkdownText)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Search_Button = QPushButton(NBA_Player_Stats)
        self.Search_Button.setObjectName(u"Search_Button")
        self.Search_Button.setEnabled(True)
        self.Search_Button.setGeometry(QRect(490, 250, 251, 41))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.Search_Button.setFont(font5)
        self.Team_ComboBox = QComboBox(NBA_Player_Stats)
        self.Team_ComboBox.addItem("")
        self.Team_ComboBox.setObjectName(u"Team_ComboBox")
        self.Team_ComboBox.setGeometry(QRect(650, 60, 301, 41))
        self.Team_ComboBox.setFont(font3)
        self.Team_ComboBox.setMaxVisibleItems(15)
        self.List_Label_3 = QLabel(NBA_Player_Stats)
        self.List_Label_3.setObjectName(u"List_Label_3")
        self.List_Label_3.setGeometry(QRect(650, 10, 301, 41))
        self.List_Label_3.setFont(font1)
        self.List_Label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.KeyWord_Text = QLineEdit(NBA_Player_Stats)
        self.KeyWord_Text.setObjectName(u"KeyWord_Text")
        self.KeyWord_Text.setGeometry(QRect(300, 60, 321, 41))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(16)
        self.KeyWord_Text.setFont(font6)
        self.KeyWord_Text.setEchoMode(QLineEdit.Normal)
        self.KeyWord_Text.setAlignment(Qt.AlignCenter)
        self.KeyWord_Text.setReadOnly(False)
        self.label_5 = QLabel(NBA_Player_Stats)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 10, 341, 41))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.List_Label_2 = QLabel(NBA_Player_Stats)
        self.List_Label_2.setObjectName(u"List_Label_2")
        self.List_Label_2.setGeometry(QRect(980, 10, 221, 41))
        self.List_Label_2.setFont(font1)
        self.List_Label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Season_ComboBox = QComboBox(NBA_Player_Stats)
        self.Season_ComboBox.addItem("")
        self.Season_ComboBox.setObjectName(u"Season_ComboBox")
        self.Season_ComboBox.setGeometry(QRect(980, 60, 191, 41))
        self.Season_ComboBox.setFont(font3)
        self.Season_ComboBox.setMaxVisibleItems(15)
        self.label_9 = QLabel(NBA_Player_Stats)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 120, 1251, 31))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_10 = QLabel(NBA_Player_Stats)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(160, 20, 151, 61))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_5.raise_()
        self.List_Label_3.raise_()
        self.List_Label.raise_()
        self.List_Label_2.raise_()
        self.Pic_Label.raise_()
        self.WillyF_Label.raise_()
        self.Reset_Button.raise_()
        self.Info_Table.raise_()
        self.label_4.raise_()
        self.Search_Button.raise_()
        self.KeyWord_Text.raise_()
        self.Team_ComboBox.raise_()
        self.Season_ComboBox.raise_()
        self.Player_ComboBox.raise_()
        self.label_9.raise_()
        self.label_10.raise_()

        self.retranslateUi(NBA_Player_Stats)

        QMetaObject.connectSlotsByName(NBA_Player_Stats)
    # setupUi

    def retranslateUi(self, NBA_Player_Stats):
        NBA_Player_Stats.setWindowTitle(QCoreApplication.translate("NBA_Player_Stats", u"NBA Player Statistics (from 1996-97 to 2022-23)", None))
        self.Reset_Button.setText(QCoreApplication.translate("NBA_Player_Stats", u"Reset", None))
        self.List_Label.setText(QCoreApplication.translate("NBA_Player_Stats", u"Player:", None))
        self.WillyF_Label.setText(QCoreApplication.translate("NBA_Player_Stats", u"Developed by WillyF", None))
        self.Pic_Label.setText("")
        self.Player_ComboBox.setItemText(0, QCoreApplication.translate("NBA_Player_Stats", u"All Players", None))

        self.Player_ComboBox.setCurrentText(QCoreApplication.translate("NBA_Player_Stats", u"All Players", None))
        self.label_4.setText(QCoreApplication.translate("NBA_Player_Stats", u"Player Statistics:", None))
        self.Search_Button.setText(QCoreApplication.translate("NBA_Player_Stats", u"Search", None))
        self.Team_ComboBox.setItemText(0, QCoreApplication.translate("NBA_Player_Stats", u"All Teams", None))

        self.Team_ComboBox.setCurrentText(QCoreApplication.translate("NBA_Player_Stats", u"All Teams", None))
        self.List_Label_3.setText(QCoreApplication.translate("NBA_Player_Stats", u"Team:", None))
        self.label_5.setText(QCoreApplication.translate("NBA_Player_Stats", u"Player Name Keyword: ", None))
        self.List_Label_2.setText(QCoreApplication.translate("NBA_Player_Stats", u"Season:", None))
        self.Season_ComboBox.setItemText(0, QCoreApplication.translate("NBA_Player_Stats", u"All Seasons", None))

        self.Season_ComboBox.setCurrentText(QCoreApplication.translate("NBA_Player_Stats", u"All Seasons", None))
        self.label_9.setText(QCoreApplication.translate("NBA_Player_Stats", u"================================================================================================", None))
        self.label_10.setText(QCoreApplication.translate("NBA_Player_Stats", u"Filters: ", None))
    # retranslateUi

