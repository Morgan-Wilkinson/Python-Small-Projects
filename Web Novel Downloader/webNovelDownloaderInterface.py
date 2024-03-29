# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webNovelDownloaderInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_webNovelDownloader(object):
    def setupUi(self, webNovelDownloader):
        webNovelDownloader.setObjectName("webNovelDownloader")
        webNovelDownloader.resize(800, 350)
        webNovelDownloader.setMinimumSize(QtCore.QSize(800, 350))
        webNovelDownloader.setMaximumSize(QtCore.QSize(950, 450))
        self.centralwidget = QtWidgets.QWidget(webNovelDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.novelSpecificationsLayout = QtWidgets.QGridLayout()
        self.novelSpecificationsLayout.setObjectName("novelSpecificationsLayout")
        self.chapterIndexStart = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chapterIndexStart.sizePolicy().hasHeightForWidth())
        self.chapterIndexStart.setSizePolicy(sizePolicy)
        self.chapterIndexStart.setMaximumSize(QtCore.QSize(200, 50))
        self.chapterIndexStart.setMinimum(0)
        self.chapterIndexStart.setMaximum(10000)
        self.chapterIndexStart.setProperty("value", 0)
        self.chapterIndexStart.setObjectName("chapterIndexStart")
        self.novelSpecificationsLayout.addWidget(self.chapterIndexStart, 2, 1, 1, 1)
        self.latestChapter = QtWidgets.QCheckBox(self.centralwidget)
        self.latestChapter.setObjectName("latestChapter")
        self.novelSpecificationsLayout.addWidget(self.latestChapter, 2, 5, 1, 1)
        self.chapterIndexEnd = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chapterIndexEnd.sizePolicy().hasHeightForWidth())
        self.chapterIndexEnd.setSizePolicy(sizePolicy)
        self.chapterIndexEnd.setMaximumSize(QtCore.QSize(200, 50))
        self.chapterIndexEnd.setMinimum(0)
        self.chapterIndexEnd.setMaximum(10000)
        self.chapterIndexEnd.setProperty("value", 0)
        self.chapterIndexEnd.setObjectName("chapterIndexEnd")
        self.novelSpecificationsLayout.addWidget(self.chapterIndexEnd, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.novelSpecificationsLayout.addWidget(self.label, 2, 2, 1, 1)
        self.novelLabel = QtWidgets.QLabel(self.centralwidget)
        self.novelLabel.setObjectName("novelLabel")
        self.novelSpecificationsLayout.addWidget(self.novelLabel, 1, 0, 1, 1)
        self.websiteMenu = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.websiteMenu.sizePolicy().hasHeightForWidth())
        self.websiteMenu.setSizePolicy(sizePolicy)
        self.websiteMenu.setMinimumSize(QtCore.QSize(200, 0))
        self.websiteMenu.setMaximumSize(QtCore.QSize(200, 100))
        self.websiteMenu.setObjectName("websiteMenu")
        self.websiteMenu.addItem("")
        self.novelSpecificationsLayout.addWidget(self.websiteMenu, 0, 1, 1, 1)
        self.novelMenu = QtWidgets.QComboBox(self.centralwidget)
        self.novelMenu.setObjectName("novelMenu")
        self.novelSpecificationsLayout.addWidget(self.novelMenu, 1, 1, 1, 1)
        self.websiteLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.websiteLabel.sizePolicy().hasHeightForWidth())
        self.websiteLabel.setSizePolicy(sizePolicy)
        self.websiteLabel.setMinimumSize(QtCore.QSize(120, 0))
        self.websiteLabel.setMaximumSize(QtCore.QSize(70, 16777215))
        self.websiteLabel.setObjectName("websiteLabel")
        self.novelSpecificationsLayout.addWidget(self.websiteLabel, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.novelSpecificationsLayout.addWidget(self.line, 2, 4, 1, 1)
        self.chapterIndexLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chapterIndexLabel.sizePolicy().hasHeightForWidth())
        self.chapterIndexLabel.setSizePolicy(sizePolicy)
        self.chapterIndexLabel.setMinimumSize(QtCore.QSize(130, 0))
        self.chapterIndexLabel.setObjectName("chapterIndexLabel")
        self.novelSpecificationsLayout.addWidget(self.chapterIndexLabel, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.novelSpecificationsLayout)
        self.saveSpecificationsLayout = QtWidgets.QGridLayout()
        self.saveSpecificationsLayout.setObjectName("saveSpecificationsLayout")
        self.saveDirectoryLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveDirectoryLabel.sizePolicy().hasHeightForWidth())
        self.saveDirectoryLabel.setSizePolicy(sizePolicy)
        self.saveDirectoryLabel.setMinimumSize(QtCore.QSize(130, 0))
        self.saveDirectoryLabel.setMaximumSize(QtCore.QSize(70, 50))
        self.saveDirectoryLabel.setObjectName("saveDirectoryLabel")
        self.saveSpecificationsLayout.addWidget(self.saveDirectoryLabel, 0, 0, 1, 1)
        self.openDirectory = QtWidgets.QPushButton(self.centralwidget)
        self.openDirectory.setMaximumSize(QtCore.QSize(100, 16777215))
        self.openDirectory.setObjectName("openDirectory")
        self.saveSpecificationsLayout.addWidget(self.openDirectory, 0, 2, 1, 1)
        self.directoryPath = QtWidgets.QLineEdit(self.centralwidget)
        self.directoryPath.setObjectName("directoryPath")
        self.saveSpecificationsLayout.addWidget(self.directoryPath, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.saveSpecificationsLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.saveSpecificationsLayout)
        self.conversionsSpecificationsLayout = QtWidgets.QGridLayout()
        self.conversionsSpecificationsLayout.setObjectName("conversionsSpecificationsLayout")
        self.combinePDF = QtWidgets.QCheckBox(self.centralwidget)
        self.combinePDF.setObjectName("combinePDF")
        self.conversionsSpecificationsLayout.addWidget(self.combinePDF, 0, 1, 1, 1)
        self.convertPDF = QtWidgets.QCheckBox(self.centralwidget)
        self.convertPDF.setObjectName("convertPDF")
        self.conversionsSpecificationsLayout.addWidget(self.convertPDF, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.conversionsSpecificationsLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.deleteFiles = QtWidgets.QCheckBox(self.centralwidget)
        self.deleteFiles.setObjectName("deleteFiles")
        self.conversionsSpecificationsLayout.addWidget(self.deleteFiles, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.conversionsSpecificationsLayout)
        self.startLayout = QtWidgets.QGridLayout()
        self.startLayout.setObjectName("startLayout")
        spacerItem2 = QtWidgets.QSpacerItem(270, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.startLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.startButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startButton.setAutoFillBackground(False)
        self.startButton.setObjectName("startButton")
        self.startLayout.addWidget(self.startButton, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(270, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.startLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.startLayout.addWidget(self.progressBar, 2, 0, 1, 3)
        self.verticalLayout.addLayout(self.startLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        webNovelDownloader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(webNovelDownloader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuWebNovel_Downloader = QtWidgets.QMenu(self.menubar)
        self.menuWebNovel_Downloader.setObjectName("menuWebNovel_Downloader")
        self.menuPreferences = QtWidgets.QMenu(self.menuWebNovel_Downloader)
        self.menuPreferences.setObjectName("menuPreferences")
        webNovelDownloader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(webNovelDownloader)
        self.statusbar.setObjectName("statusbar")
        webNovelDownloader.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(webNovelDownloader)
        self.actionOpen.setObjectName("actionOpen")
        self.actionStop = QtWidgets.QAction(webNovelDownloader)
        self.actionStop.setObjectName("actionStop")
        self.actionResume = QtWidgets.QAction(webNovelDownloader)
        self.actionResume.setObjectName("actionResume")
        self.actionPause = QtWidgets.QAction(webNovelDownloader)
        self.actionPause.setObjectName("actionPause")
        self.actionDark_Mode_2 = QtWidgets.QAction(webNovelDownloader)
        self.actionDark_Mode_2.setObjectName("actionDark_Mode_2")
        self.actionLight_Mode = QtWidgets.QAction(webNovelDownloader)
        self.actionLight_Mode.setObjectName("actionLight_Mode")
        self.menuFIle.addAction(self.actionOpen)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionResume)
        self.menuFIle.addAction(self.actionPause)
        self.menuFIle.addAction(self.actionStop)
        self.menuPreferences.addAction(self.actionDark_Mode_2)
        self.menuPreferences.addAction(self.actionLight_Mode)
        self.menuWebNovel_Downloader.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuWebNovel_Downloader.menuAction())
        self.menubar.addAction(self.menuFIle.menuAction())
        self.label.setBuddy(self.chapterIndexEnd)
        self.novelLabel.setBuddy(self.novelMenu)
        self.websiteLabel.setBuddy(self.websiteMenu)
        self.chapterIndexLabel.setBuddy(self.chapterIndexStart)
        self.saveDirectoryLabel.setBuddy(self.directoryPath)

        self.retranslateUi(webNovelDownloader)
        QtCore.QMetaObject.connectSlotsByName(webNovelDownloader)
        webNovelDownloader.setTabOrder(self.websiteMenu, self.novelMenu)
        webNovelDownloader.setTabOrder(self.novelMenu, self.chapterIndexStart)
        webNovelDownloader.setTabOrder(self.chapterIndexStart, self.chapterIndexEnd)
        webNovelDownloader.setTabOrder(self.chapterIndexEnd, self.latestChapter)
        webNovelDownloader.setTabOrder(self.latestChapter, self.directoryPath)
        webNovelDownloader.setTabOrder(self.directoryPath, self.openDirectory)
        webNovelDownloader.setTabOrder(self.openDirectory, self.convertPDF)
        webNovelDownloader.setTabOrder(self.convertPDF, self.combinePDF)
        webNovelDownloader.setTabOrder(self.combinePDF, self.startButton)

    def retranslateUi(self, webNovelDownloader):
        _translate = QtCore.QCoreApplication.translate
        webNovelDownloader.setWindowTitle(_translate("webNovelDownloader", "Web Novel Downloader"))
        self.latestChapter.setText(_translate("webNovelDownloader", "Latest Chapter"))
        self.label.setText(_translate("webNovelDownloader", "To"))
        self.novelLabel.setText(_translate("webNovelDownloader", "Novels:"))
        self.websiteMenu.setItemText(0, _translate("webNovelDownloader", "WuxiaWorld"))
        self.websiteLabel.setText(_translate("webNovelDownloader", "Download from:"))
        self.chapterIndexLabel.setText(_translate("webNovelDownloader", "Download Chapters: "))
        self.saveDirectoryLabel.setText(_translate("webNovelDownloader", "Save Directory:"))
        self.openDirectory.setText(_translate("webNovelDownloader", "Open"))
        self.combinePDF.setText(_translate("webNovelDownloader", "Combine All Files into One PDF"))
        self.convertPDF.setText(_translate("webNovelDownloader", "Convert Files to PDF Format"))
        self.deleteFiles.setText(_translate("webNovelDownloader", "Delete existing files in the specfied directory"))
        self.startButton.setText(_translate("webNovelDownloader", "Start"))
        self.menuFIle.setTitle(_translate("webNovelDownloader", "FIle"))
        self.menuWebNovel_Downloader.setTitle(_translate("webNovelDownloader", "WebNovel Downloader"))
        self.menuPreferences.setTitle(_translate("webNovelDownloader", "Preferences"))
        self.actionOpen.setText(_translate("webNovelDownloader", "Open"))
        self.actionStop.setText(_translate("webNovelDownloader", "Cancel"))
        self.actionResume.setText(_translate("webNovelDownloader", "Resume"))
        self.actionPause.setText(_translate("webNovelDownloader", "Pause"))
        self.actionDark_Mode_2.setText(_translate("webNovelDownloader", "Dark Mode"))
        self.actionLight_Mode.setText(_translate("webNovelDownloader", "Light Mode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    webNovelDownloader = QtWidgets.QMainWindow()
    ui = Ui_webNovelDownloader()
    ui.setupUi(webNovelDownloader)
    webNovelDownloader.show()
    sys.exit(app.exec_())
