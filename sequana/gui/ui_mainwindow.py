# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 695)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlayout.setContentsMargins(5, 0, 5, 0)
        self.vlayout.setSpacing(0)
        self.vlayout.setObjectName("vlayout")
        self.tabs_pipeline = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs_pipeline.sizePolicy().hasHeightForWidth())
        self.tabs_pipeline.setSizePolicy(sizePolicy)
        self.tabs_pipeline.setMinimumSize(QtCore.QSize(0, 118))
        self.tabs_pipeline.setStyleSheet("background-color:#aaddcc")
        self.tabs_pipeline.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs_pipeline.setMovable(True)
        self.tabs_pipeline.setObjectName("tabs_pipeline")
        self.tab_sequana_pipelines = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_sequana_pipelines.sizePolicy().hasHeightForWidth())
        self.tab_sequana_pipelines.setSizePolicy(sizePolicy)
        self.tab_sequana_pipelines.setObjectName("tab_sequana_pipelines")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_sequana_pipelines)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabs_sequana = QtWidgets.QTabWidget(self.tab_sequana_pipelines)
        self.tabs_sequana.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs_sequana.sizePolicy().hasHeightForWidth())
        self.tabs_sequana.setSizePolicy(sizePolicy)
        self.tabs_sequana.setBaseSize(QtCore.QSize(0, 0))
        self.tabs_sequana.setStyleSheet("background-color:#ffeedd")
        self.tabs_sequana.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs_sequana.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabs_sequana.setDocumentMode(False)
        self.tabs_sequana.setTabsClosable(False)
        self.tabs_sequana.setMovable(True)
        self.tabs_sequana.setTabBarAutoHide(False)
        self.tabs_sequana.setObjectName("tabs_sequana")
        self.Pipeline = QtWidgets.QWidget()
        self.Pipeline.setObjectName("Pipeline")
        self.layout_sequana = QtWidgets.QHBoxLayout(self.Pipeline)
        self.layout_sequana.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_sequana.setContentsMargins(6, 0, 6, 0)
        self.layout_sequana.setSpacing(6)
        self.layout_sequana.setObjectName("layout_sequana")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choice_button = QtWidgets.QComboBox(self.Pipeline)
        self.choice_button.setObjectName("choice_button")
        self.choice_button.addItem("")
        self.verticalLayout.addWidget(self.choice_button)
        self.layout_sequana.addLayout(self.verticalLayout)
        self.tabs_sequana.addTab(self.Pipeline, "")
        self.sequana_input_dir_tab = QtWidgets.QWidget()
        self.sequana_input_dir_tab.setObjectName("sequana_input_dir_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.sequana_input_dir_tab)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.sequana_input_dir_tab)
        self.tabWidget.setStyleSheet("background-color:white")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.layout_sequana_input_dir = QtWidgets.QHBoxLayout()
        self.layout_sequana_input_dir.setObjectName("layout_sequana_input_dir")
        self.gridLayout_10.addLayout(self.layout_sequana_input_dir, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.layout_sequana_input_files = QtWidgets.QHBoxLayout()
        self.layout_sequana_input_files.setObjectName("layout_sequana_input_files")
        self.gridLayout_9.addLayout(self.layout_sequana_input_files, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tabs_sequana.addTab(self.sequana_input_dir_tab, "")
        self.sequana_working_dir_tab = QtWidgets.QWidget()
        self.sequana_working_dir_tab.setObjectName("sequana_working_dir_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.sequana_working_dir_tab)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.layout_sequana_wkdir = QtWidgets.QHBoxLayout()
        self.layout_sequana_wkdir.setObjectName("layout_sequana_wkdir")
        self.gridLayout_8.addLayout(self.layout_sequana_wkdir, 0, 0, 1, 1)
        self.tabs_sequana.addTab(self.sequana_working_dir_tab, "")
        self.verticalLayout_4.addWidget(self.tabs_sequana)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabs_pipeline.addTab(self.tab_sequana_pipelines, "")
        self.tab_generic_pipelines = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_generic_pipelines.sizePolicy().hasHeightForWidth())
        self.tab_generic_pipelines.setSizePolicy(sizePolicy)
        self.tab_generic_pipelines.setObjectName("tab_generic_pipelines")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_generic_pipelines)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(6, -1, 6, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabs_generic = QtWidgets.QTabWidget(self.tab_generic_pipelines)
        self.tabs_generic.setStyleSheet("background-color:#ffeedd")
        self.tabs_generic.setObjectName("tabs_generic")
        self.snakefile = QtWidgets.QWidget()
        self.snakefile.setObjectName("snakefile")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.snakefile)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.layout_generic_snakefile = QtWidgets.QHBoxLayout()
        self.layout_generic_snakefile.setObjectName("layout_generic_snakefile")
        self.gridLayout_12.addLayout(self.layout_generic_snakefile, 0, 0, 1, 1)
        self.tabs_generic.addTab(self.snakefile, "")
        self.configfile = QtWidgets.QWidget()
        self.configfile.setObjectName("configfile")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.configfile)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.layout_generic_config = QtWidgets.QHBoxLayout()
        self.layout_generic_config.setObjectName("layout_generic_config")
        self.gridLayout_13.addLayout(self.layout_generic_config, 0, 0, 1, 1)
        self.tabs_generic.addTab(self.configfile, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.layout_generic_wkdir = QtWidgets.QHBoxLayout()
        self.layout_generic_wkdir.setObjectName("layout_generic_wkdir")
        self.gridLayout_14.addLayout(self.layout_generic_wkdir, 0, 0, 1, 1)
        self.tabs_generic.addTab(self.tab, "")
        self.verticalLayout_3.addWidget(self.tabs_generic)
        self.gridLayout_11.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabs_pipeline.addTab(self.tab_generic_pipelines, "")
        self.vlayout.addWidget(self.tabs_pipeline)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 89))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.until_box = QtWidgets.QComboBox(self.groupBox)
        self.until_box.setEditable(False)
        self.until_box.setCurrentText("")
        self.until_box.setObjectName("until_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.until_box)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.starting_box = QtWidgets.QComboBox(self.groupBox)
        self.starting_box.setObjectName("starting_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.starting_box)
        self.horizontalLayout_3.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.comboBox_local = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_local.setObjectName("comboBox_local")
        self.comboBox_local.addItem("")
        self.comboBox_local.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_local)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color:orange")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.gridLayout_15.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.vlayout.addWidget(self.groupBox)
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setMinimumSize(QtCore.QSize(0, 0))
        self.tabs.setMaximumSize(QtCore.QSize(16777215, 2000))
        self.tabs.setBaseSize(QtCore.QSize(0, 0))
        self.tabs.setToolTip("")
        self.tabs.setStyleSheet("background-color:#ffffff")
        self.tabs.setObjectName("tabs")
        self.snakemake = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snakemake.sizePolicy().hasHeightForWidth())
        self.snakemake.setSizePolicy(sizePolicy)
        self.snakemake.setObjectName("snakemake")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.snakemake)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.layout_snakemake = QtWidgets.QVBoxLayout()
        self.layout_snakemake.setObjectName("layout_snakemake")
        self.gridLayout_5.addLayout(self.layout_snakemake, 0, 0, 1, 1)
        self.tabs.addTab(self.snakemake, "")
        self.ipython = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ipython.sizePolicy().hasHeightForWidth())
        self.ipython.setSizePolicy(sizePolicy)
        self.ipython.setObjectName("ipython")
        self.gridLayout = QtWidgets.QGridLayout(self.ipython)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.layout_ipython = QtWidgets.QVBoxLayout()
        self.layout_ipython.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_ipython.setSpacing(6)
        self.layout_ipython.setObjectName("layout_ipython")
        self.gridLayout.addLayout(self.layout_ipython, 0, 0, 1, 1)
        self.tabs.addTab(self.ipython, "")
        self.logger = QtWidgets.QWidget()
        self.logger.setObjectName("logger")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.logger)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.layout_logger = QtWidgets.QVBoxLayout()
        self.layout_logger.setObjectName("layout_logger")
        self.gridLayout_3.addLayout(self.layout_logger, 0, 0, 1, 1)
        self.tabs.addTab(self.logger, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 561, 227))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabs.addTab(self.tab_3, "")
        self.vlayout.addWidget(self.tabs)
        self.widget_footer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_footer.sizePolicy().hasHeightForWidth())
        self.widget_footer.setSizePolicy(sizePolicy)
        self.widget_footer.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_footer.setObjectName("widget_footer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_footer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.run_btn = QtWidgets.QPushButton(self.widget_footer)
        self.run_btn.setObjectName("run_btn")
        self.horizontalLayout.addWidget(self.run_btn)
        self.stop_btn = QtWidgets.QPushButton(self.widget_footer)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout.addWidget(self.stop_btn)
        self.unlock_btn = QtWidgets.QPushButton(self.widget_footer)
        self.unlock_btn.setObjectName("unlock_btn")
        self.horizontalLayout.addWidget(self.unlock_btn)
        self.report_btn = QtWidgets.QPushButton(self.widget_footer)
        self.report_btn.setObjectName("report_btn")
        self.horizontalLayout.addWidget(self.report_btn)
        self.save_btn = QtWidgets.QPushButton(self.widget_footer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setAutoFillBackground(False)
        self.save_btn.setStyleSheet("background-color:orange")
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.dag_btn = QtWidgets.QPushButton(self.widget_footer)
        self.dag_btn.setObjectName("dag_btn")
        self.horizontalLayout.addWidget(self.dag_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.vlayout.addWidget(self.widget_footer)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setToolTipDuration(-1)
        self.progressBar.setStyleSheet("border: 2px solid grey;\n"
"margin:2px;\n"
"border-radius: 5px;\n"
"text-align: center;\n"
"")
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")
        self.vlayout.addWidget(self.progressBar)
        self.vlayout.setStretch(1, 1)
        self.vlayout.setStretch(4, 1)
        self.gridLayout_2.addLayout(self.vlayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImportConfig = QtWidgets.QAction(MainWindow)
        self.actionImportConfig.setObjectName("actionImportConfig")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSnakemake = QtWidgets.QAction(MainWindow)
        self.actionSnakemake.setCheckable(False)
        self.actionSnakemake.setObjectName("actionSnakemake")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionIPython = QtWidgets.QAction(MainWindow)
        self.actionIPython.setCheckable(True)
        self.actionIPython.setObjectName("actionIPython")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setEnabled(True)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuOption.addAction(self.actionSnakemake)
        self.menuOption.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs_pipeline.setCurrentIndex(1)
        self.tabs_sequana.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.tabs_generic.setCurrentIndex(1)
        self.tabs.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabs_pipeline, self.choice_button)
        MainWindow.setTabOrder(self.choice_button, self.until_box)
        MainWindow.setTabOrder(self.until_box, self.starting_box)
        MainWindow.setTabOrder(self.starting_box, self.tabs)
        MainWindow.setTabOrder(self.tabs, self.run_btn)
        MainWindow.setTabOrder(self.run_btn, self.stop_btn)
        MainWindow.setTabOrder(self.stop_btn, self.unlock_btn)
        MainWindow.setTabOrder(self.unlock_btn, self.report_btn)
        MainWindow.setTabOrder(self.report_btn, self.save_btn)
        MainWindow.setTabOrder(self.save_btn, self.dag_btn)
        MainWindow.setTabOrder(self.dag_btn, self.scrollArea)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sequanix (Sequana GUI)"))
        self.tabs_pipeline.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select a Sequana pipeline (left tab) or a generic Snakemake file (right tab).</p><p><br/>Go to Menu-&gt;QuickStart for more details (Ctrl+H key).</p></body></html>"))
        self.tabs_sequana.setToolTip(_translate("MainWindow", "<html><head/><body><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Left tab:</span> Select one of the pipeline in the combo box. In order to get information about a pipeline, please see the Help menu. </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Middle tab:</span> Select one of this option</li><ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Input directory: the directory where fastq.gz files are stored (all Sequana pipelines expect fastq.gz as input)</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Input samples: select one or two files (fastq.gz) in a directory</li></ol><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Right tab: </span>Select working directory where Snakefile/pipeline and config files will be copied. Pipelines are also ran in that directory. </li></ul></body></html>"))
        self.choice_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Sequana pipelines are automatically fetched from sequana library.</p><p>Each pipeline is defined by a pipeline name. Its config file is fetched automatically.</p><p>Each pipeline require the user to define the input. It may be one of:</p><p><ul><li> a directory</li><li> a set of FastQ input file</li></ul></body></html>"))
        self.choice_button.setCurrentText(_translate("MainWindow", "Select a Sequana pipeline"))
        self.choice_button.setItemText(0, _translate("MainWindow", "Select a Sequana pipeline"))
        self.tabs_sequana.setTabText(self.tabs_sequana.indexOf(self.Pipeline), _translate("MainWindow", "1 - Pipeline selection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "a - Input directory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "b - Input sample(s)"))
        self.tabs_sequana.setTabText(self.tabs_sequana.indexOf(self.sequana_input_dir_tab), _translate("MainWindow", "2 - Input data (directory or files)"))
        self.tabs_sequana.setTabText(self.tabs_sequana.indexOf(self.sequana_working_dir_tab), _translate("MainWindow", "3 - Working directory"))
        self.tabs_pipeline.setTabText(self.tabs_pipeline.indexOf(self.tab_sequana_pipelines), _translate("MainWindow", "A - Sequana pipelines"))
        self.tabs_generic.setToolTip(_translate("MainWindow", "<html><head/><body><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Left tab:</span> Select a valid local Snakefile. </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Middle tab:</span> Select a config file. This is optional. Note that Snakefiles may be using a config file or not. For instance if <i>configfile: \"config.yaml\"</i> is found, a config file is expected. Users have to check with the author of the snakefile whether a config file is required or not.</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Right tab: </span>Select working directory where Snakefile and config files will be copied. Pipelines are also ran in that directory. </li></ul></body></html>"))
        self.tabs_generic.setTabText(self.tabs_generic.indexOf(self.snakefile), _translate("MainWindow", "1 - Snakefile"))
        self.tabs_generic.setTabText(self.tabs_generic.indexOf(self.configfile), _translate("MainWindow", "2 - Config file"))
        self.tabs_generic.setTabText(self.tabs_generic.indexOf(self.tab), _translate("MainWindow", "3 - Working directory"))
        self.tabs_pipeline.setTabText(self.tabs_pipeline.indexOf(self.tab_generic_pipelines), _translate("MainWindow", "B - Generic pipelines"))
        self.groupBox.setTitle(_translate("MainWindow", "Pipeline control"))
        self.label.setText(_translate("MainWindow", "Until"))
        self.label_2.setText(_translate("MainWindow", "Starting"))
        self.label_3.setText(_translate("MainWindow", "Local or cluster run ?"))
        self.comboBox_local.setItemText(0, _translate("MainWindow", "local"))
        self.comboBox_local.setItemText(1, _translate("MainWindow", "cluster"))
        self.label_4.setText(_translate("MainWindow", "Please, Check the snakemake dialog to set the number of nodes in the local or cluster tabs"))
        self.snakemake.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is the output of the snakemake execution. </p><p>Be aware that we parse the output so colors and output may be slightly different.</p></body></html>"))
        self.tabs.setTabText(self.tabs.indexOf(self.snakemake), _translate("MainWindow", "&Snakemake output"))
        self.ipython.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is an IPython shell included in the GUI. The entire Sequana GUI is accessible as the variable <span style=\" font-weight:600;\">gui.</span></p><p>For instance, you can access to layout or values set in the graphical interface with:</p>\n"
"<pre>    \n"
"    gui.ui\n"
"</pre>\n"
"\n"
"<p>More generally, this is a pure IPython shell, so you can use e.g. matplotlib/pylab:</p>\n"
"<pre>    \n"
"    import pylab\n"
"    pylab.plot([1,2,3])\n"
"</pre></body></html>"))
        self.tabs.setTabText(self.tabs.indexOf(self.ipython), _translate("MainWindow", "&IPython shell"))
        self.logger.setToolTip(_translate("MainWindow", "<p>This tab contains the logging information from Sequana and possibly other Python packages that uses the logging package.</p>\n"
"\n"
"Color code:\n"
"\n"
"<pre>\n"
"- debug: cyan\n"
"- info: green\n"
"- warning: orange\n"
"- error: red\n"
"- critical: bold red \n"
"</pre>"))
        self.tabs.setTabText(self.tabs.indexOf(self.logger), _translate("MainWindow", "&Logger"))
        self.tab_3.setToolTip(_translate("MainWindow", "This tab contains the configuration file arguments. \n"
"\n"
"You can edit the form but will need to press SAVE to make it effective.\n"
"\n"
"Once saved, the DAG and RUN buttons should be available."))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), _translate("MainWindow", "&Config parameters"))
        self.run_btn.setToolTip(_translate("MainWindow", "Run the pipeline (shortcut: Ctrl+R)"))
        self.run_btn.setText(_translate("MainWindow", "&Run"))
        self.run_btn.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.stop_btn.setToolTip(_translate("MainWindow", "Stop the running pipeline"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.stop_btn.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.unlock_btn.setToolTip(_translate("MainWindow", "Unlock the directory where the pipeline is run.\n"
"This launch snakemake with the following arguments: \n"
"\n"
"snakemake -s Snakefile --unlock "))
        self.unlock_btn.setText(_translate("MainWindow", "&Unlock"))
        self.unlock_btn.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.report_btn.setToolTip(_translate("MainWindow", "This button open an HTML page present in the working directory (if found).\n"
"\n"
"This is essentially for the sequana pipeline (default filename is multi_summary.html but one can change the name in the option/preferences dialog."))
        self.report_btn.setText(_translate("MainWindow", "Open Report"))
        self.report_btn.setShortcut(_translate("MainWindow", "Shift+W"))
        self.save_btn.setText(_translate("MainWindow", "&Save"))
        self.save_btn.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.dag_btn.setToolTip(_translate("MainWindow", "Pressing this button, a DAG is created and shown. \n"
"This is a good way to check your config file ."))
        self.dag_btn.setText(_translate("MainWindow", "Show &Dag"))
        self.dag_btn.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.progressBar.setToolTip(_translate("MainWindow", "<p>Progress of the pipeline. color codes:\n"
"    <ul>\n"
"        <li style=\"color:red\">Red: an error occured</li>\n"
"        <li style=\"color:green\">Green: completed with success</li>\n"
"        <li style=\"color:blue\">Blue: in progress</li>\n"
"    </ul>\n"
"</p>"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuOption.setTitle(_translate("MainWindow", "&Option"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionImportConfig.setText(_translate("MainWindow", "&Import Config File"))
        self.actionImportConfig.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSnakemake.setText(_translate("MainWindow", "Snakemake &Options"))
        self.actionSnakemake.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionPreferences.setText(_translate("MainWindow", "&Preferences"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionIPython.setText(_translate("MainWindow", "Show/Hide IPython &Debug dialog"))
        self.actionIPython.setToolTip(_translate("MainWindow", "Show or Hide an IPython dialog for debugging"))
        self.actionIPython.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionHelp.setText(_translate("MainWindow", "Quick Start"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))

