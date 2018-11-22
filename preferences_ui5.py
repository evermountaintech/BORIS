# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_prefDialog(object):
    def setupUi(self, prefDialog):
        prefDialog.setObjectName("prefDialog")
        prefDialog.setWindowModality(QtCore.Qt.WindowModal)
        prefDialog.resize(596, 525)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(prefDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(prefDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cbTimeFormat = QtWidgets.QComboBox(self.tab)
        self.cbTimeFormat.setObjectName("cbTimeFormat")
        self.cbTimeFormat.addItem("")
        self.cbTimeFormat.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbTimeFormat)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.sbffSpeed = QtWidgets.QSpinBox(self.tab)
        self.sbffSpeed.setMinimum(0)
        self.sbffSpeed.setMaximum(10000)
        self.sbffSpeed.setProperty("value", 10)
        self.sbffSpeed.setObjectName("sbffSpeed")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbffSpeed)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sbRepositionTimeOffset = QtWidgets.QSpinBox(self.tab)
        self.sbRepositionTimeOffset.setMinimum(-10000)
        self.sbRepositionTimeOffset.setMaximum(10000)
        self.sbRepositionTimeOffset.setProperty("value", -3)
        self.sbRepositionTimeOffset.setObjectName("sbRepositionTimeOffset")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sbRepositionTimeOffset)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.sbSpeedStep = QtWidgets.QDoubleSpinBox(self.tab)
        self.sbSpeedStep.setDecimals(1)
        self.sbSpeedStep.setMinimum(0.1)
        self.sbSpeedStep.setMaximum(1.0)
        self.sbSpeedStep.setSingleStep(0.1)
        self.sbSpeedStep.setProperty("value", 0.1)
        self.sbSpeedStep.setObjectName("sbSpeedStep")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbSpeedStep)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.sbAutomaticBackup = QtWidgets.QSpinBox(self.tab)
        self.sbAutomaticBackup.setMinimum(-10000)
        self.sbAutomaticBackup.setMaximum(10000)
        self.sbAutomaticBackup.setProperty("value", 10)
        self.sbAutomaticBackup.setObjectName("sbAutomaticBackup")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sbAutomaticBackup)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.leSeparator = QtWidgets.QLineEdit(self.tab)
        self.leSeparator.setObjectName("leSeparator")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.leSeparator)
        self.cbCloseSameEvent = QtWidgets.QCheckBox(self.tab)
        self.cbCloseSameEvent.setObjectName("cbCloseSameEvent")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.cbCloseSameEvent)
        self.cbConfirmSound = QtWidgets.QCheckBox(self.tab)
        self.cbConfirmSound.setObjectName("cbConfirmSound")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.cbConfirmSound)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.sbBeepEvery = QtWidgets.QSpinBox(self.tab)
        self.sbBeepEvery.setObjectName("sbBeepEvery")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.sbBeepEvery)
        self.cbAlertNoFocalSubject = QtWidgets.QCheckBox(self.tab)
        self.cbAlertNoFocalSubject.setObjectName("cbAlertNoFocalSubject")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.cbAlertNoFocalSubject)
        self.cbTrackingCursorAboveEvent = QtWidgets.QCheckBox(self.tab)
        self.cbTrackingCursorAboveEvent.setObjectName("cbTrackingCursorAboveEvent")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.cbTrackingCursorAboveEvent)
        self.cbCheckForNewVersion = QtWidgets.QCheckBox(self.tab)
        self.cbCheckForNewVersion.setObjectName("cbCheckForNewVersion")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.cbCheckForNewVersion)
        self.cb_pause_before_addevent = QtWidgets.QCheckBox(self.tab)
        self.cb_pause_before_addevent.setObjectName("cb_pause_before_addevent")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.cb_pause_before_addevent)
        self.verticalLayout.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbFFmpegPath = QtWidgets.QLabel(self.tab_2)
        self.lbFFmpegPath.setScaledContents(False)
        self.lbFFmpegPath.setWordWrap(True)
        self.lbFFmpegPath.setObjectName("lbFFmpegPath")
        self.verticalLayout_3.addWidget(self.lbFFmpegPath)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbFFmpegCacheDir = QtWidgets.QLabel(self.tab_2)
        self.lbFFmpegCacheDir.setObjectName("lbFFmpegCacheDir")
        self.horizontalLayout_3.addWidget(self.lbFFmpegCacheDir)
        self.leFFmpegCacheDir = QtWidgets.QLineEdit(self.tab_2)
        self.leFFmpegCacheDir.setObjectName("leFFmpegCacheDir")
        self.horizontalLayout_3.addWidget(self.leFFmpegCacheDir)
        self.pbBrowseFFmpegCacheDir = QtWidgets.QPushButton(self.tab_2)
        self.pbBrowseFFmpegCacheDir.setObjectName("pbBrowseFFmpegCacheDir")
        self.horizontalLayout_3.addWidget(self.pbBrowseFFmpegCacheDir)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbFFmpegCacheDirMaxSize = QtWidgets.QLabel(self.tab_2)
        self.lbFFmpegCacheDirMaxSize.setObjectName("lbFFmpegCacheDirMaxSize")
        self.horizontalLayout_4.addWidget(self.lbFFmpegCacheDirMaxSize)
        self.sbFFmpegCacheDirMaxSize = QtWidgets.QSpinBox(self.tab_2)
        self.sbFFmpegCacheDirMaxSize.setMaximum(10000)
        self.sbFFmpegCacheDirMaxSize.setSingleStep(10)
        self.sbFFmpegCacheDirMaxSize.setObjectName("sbFFmpegCacheDirMaxSize")
        self.horizontalLayout_4.addWidget(self.sbFFmpegCacheDirMaxSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbResize = QtWidgets.QLabel(self.tab_3)
        self.lbResize.setWordWrap(True)
        self.lbResize.setObjectName("lbResize")
        self.horizontalLayout_5.addWidget(self.lbResize)
        self.sbFrameResize = QtWidgets.QSpinBox(self.tab_3)
        self.sbFrameResize.setMaximum(1920)
        self.sbFrameResize.setSingleStep(10)
        self.sbFrameResize.setObjectName("sbFrameResize")
        self.horizontalLayout_5.addWidget(self.sbFrameResize)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.cbFrameBitmapFormat = QtWidgets.QComboBox(self.tab_3)
        self.cbFrameBitmapFormat.setObjectName("cbFrameBitmapFormat")
        self.cbFrameBitmapFormat.addItem("")
        self.cbFrameBitmapFormat.addItem("")
        self.horizontalLayout_8.addWidget(self.cbFrameBitmapFormat)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.sb_fbf_cache_size = QtWidgets.QSpinBox(self.tab_3)
        self.sb_fbf_cache_size.setMinimum(1)
        self.sb_fbf_cache_size.setMaximum(3600)
        self.sb_fbf_cache_size.setObjectName("sb_fbf_cache_size")
        self.horizontalLayout_9.addWidget(self.sb_fbf_cache_size)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbspectrogram = QtWidgets.QLabel(self.tab_4)
        self.lbspectrogram.setWordWrap(True)
        self.lbspectrogram.setObjectName("lbspectrogram")
        self.horizontalLayout_6.addWidget(self.lbspectrogram)
        self.sbSpectrogramHeight = QtWidgets.QSpinBox(self.tab_4)
        self.sbSpectrogramHeight.setMinimum(80)
        self.sbSpectrogramHeight.setMaximum(400)
        self.sbSpectrogramHeight.setSingleStep(80)
        self.sbSpectrogramHeight.setObjectName("sbSpectrogramHeight")
        self.horizontalLayout_6.addWidget(self.sbSpectrogramHeight)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.cbSpectrogramColorMap = QtWidgets.QComboBox(self.tab_4)
        self.cbSpectrogramColorMap.setObjectName("cbSpectrogramColorMap")
        self.horizontalLayout_7.addWidget(self.cbSpectrogramColorMap)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setOpenExternalLinks(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.te_plot_colors = QtWidgets.QPlainTextEdit(self.tab_5)
        self.te_plot_colors.setObjectName("te_plot_colors")
        self.verticalLayout_10.addWidget(self.te_plot_colors)
        self.pb_reset_colors = QtWidgets.QPushButton(self.tab_5)
        self.pb_reset_colors.setObjectName("pb_reset_colors")
        self.verticalLayout_10.addWidget(self.pb_reset_colors)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(241, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pbCancel = QtWidgets.QPushButton(prefDialog)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.pbOK = QtWidgets.QPushButton(prefDialog)
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout_2.addWidget(self.pbOK)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(prefDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(prefDialog)

    def retranslateUi(self, prefDialog):
        _translate = QtCore.QCoreApplication.translate
        prefDialog.setWindowTitle(_translate("prefDialog", "Preferences"))
        self.label.setText(_translate("prefDialog", "Default project time format"))
        self.cbTimeFormat.setItemText(0, _translate("prefDialog", "seconds"))
        self.cbTimeFormat.setItemText(1, _translate("prefDialog", "hh:mm:ss.mss"))
        self.label_4.setText(_translate("prefDialog", "Fast forward/backward speed (seconds)"))
        self.label_2.setText(_translate("prefDialog", "Time offset for video/audio reposition (seconds)"))
        self.label_5.setText(_translate("prefDialog", "Playback speed step value"))
        self.label_6.setText(_translate("prefDialog", "Automatic backup every (minutes)"))
        self.label_3.setText(_translate("prefDialog", "Separator for behavioural strings (events export)"))
        self.leSeparator.setText(_translate("prefDialog", "|"))
        self.cbCloseSameEvent.setText(_translate("prefDialog", "Close the same current event independently of modifiers"))
        self.cbConfirmSound.setText(_translate("prefDialog", "Play sound when a key is pressed"))
        self.label_8.setText(_translate("prefDialog", "Beep every (seconds)"))
        self.cbAlertNoFocalSubject.setText(_translate("prefDialog", "Alert if focal subject is not set"))
        self.cbTrackingCursorAboveEvent.setText(_translate("prefDialog", "Tracking cursor above current event"))
        self.cbCheckForNewVersion.setText(_translate("prefDialog", "Check for new version and news"))
        self.cb_pause_before_addevent.setText(_translate("prefDialog", "Pause media before \"Add event\" command"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("prefDialog", "Project"))
        self.lbFFmpegPath.setText(_translate("prefDialog", "FFmpeg path:"))
        self.lbFFmpegCacheDir.setText(_translate("prefDialog", "FFmpeg cache directory"))
        self.pbBrowseFFmpegCacheDir.setText(_translate("prefDialog", "..."))
        self.lbFFmpegCacheDirMaxSize.setText(_translate("prefDialog", "FFmpeg cache directory max size (Mb)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("prefDialog", "FFmpeg framework"))
        self.lbResize.setText(_translate("prefDialog", "Resize frame (horizontal number of pixels). The aspect ratio will be maintained"))
        self.label_9.setText(_translate("prefDialog", "Frame bitmap format (JPG: Low quality  PNG: High quality)"))
        self.cbFrameBitmapFormat.setItemText(0, _translate("prefDialog", "JPG"))
        self.cbFrameBitmapFormat.setItemText(1, _translate("prefDialog", "PNG"))
        self.label_11.setText(_translate("prefDialog", "Cache size (in seconds)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("prefDialog", "Frame-by-frame mode"))
        self.lbspectrogram.setText(_translate("prefDialog", "Spectrogram height"))
        self.label_7.setText(_translate("prefDialog", "Color map"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("prefDialog", "Spectrogram"))
        self.label_10.setText(_translate("prefDialog", "List of colors to be used in plot. See <a href=\"https://matplotlib.org/api/colors_api.html\">matplotlib colors</a>"))
        self.pb_reset_colors.setText(_translate("prefDialog", "Reset colors to default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("prefDialog", "Plot colors"))
        self.pbCancel.setText(_translate("prefDialog", "Cancel"))
        self.pbOK.setText(_translate("prefDialog", "OK"))

