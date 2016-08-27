import numpy as np
from PyQt4 import QtCore, QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.signal import step, bode, step2
from controls import tf, pzmap, tfchar

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


        MainWindow.setFixedSize(503, 637)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 60, 91, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 550, 181, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.plot = MatplotlibCanvas()
        self.plot2 = MatplotlibCanvas()
        self.plot3 = MatplotlibCanvas()
        self.plot4 = MatplotlibCanvas()
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(False)
        
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 120, 61, 141))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_2)
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_2)
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_2)
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_2)
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 201, 26))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(310, 30, 171, 61))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 181, 16))
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(65, 60, 121, 21))
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 120, 71, 141))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        
        self.lineEdit_4 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.verticalLayout.addWidget(self.lineEdit_4)
        
        self.lineEdit_5 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 270, 201, 111))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        
        self.checkBox_2 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_3.addWidget(self.checkBox_2)
        
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_3.addWidget(self.checkBox)
        
        self.checkBox_3 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout_3.addWidget(self.checkBox_3)
        
        self.checkBox_4 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout_3.addWidget(self.checkBox_4)
        
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 100, 201, 141))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_4)
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(False)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_4)
        
        font = QtGui.QFont()
        font.setUnderline(False)
        
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_4.addWidget(self.label_8)
        self.lineEdit_3 = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_4)
        
        font = QtGui.QFont()
        font.setUnderline(False)
        
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_4.addWidget(self.label_9)
        self.lineEdit_7 = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        
        self.verticalLayout_4.addWidget(self.lineEdit_7)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 250, 31, 16))
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        
        self.System_Characteristics_textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.System_Characteristics_textBrowser.setGeometry(QtCore.QRect(260, 290, 171, 41))
        self.System_Characteristics_textBrowser.setObjectName(_fromUtf8("System_Characteristics_textBrowser"))
        
        self.Plant_tf_textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.Plant_tf_textBrowser.setGeometry(QtCore.QRect(260, 360, 171, 71))
        self.Plant_tf_textBrowser.setObjectName(_fromUtf8("Plant_tf_textBrowser"))
        self.Label_System_Char = QtGui.QLabel(self.centralwidget)
        self.Label_System_Char.setGeometry(QtCore.QRect(280, 270, 131, 20))
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.Label_System_Char.setFont(font)
        self.Label_System_Char.setObjectName(_fromUtf8("Label_System_Char"))
        self.Label_Plant_TF = QtGui.QLabel(self.centralwidget)
        self.Label_Plant_TF.setGeometry(QtCore.QRect(280, 340, 131, 21))
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.Label_Plant_TF.setFont(font)
        self.Label_Plant_TF.setObjectName(_fromUtf8("Label_Plant_TF"))
        self.pushButton_clear_fields = QtGui.QPushButton(self.centralwidget)
        self.pushButton_clear_fields.setGeometry(QtCore.QRect(50, 520, 101, 31))
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        
        self.pushButton_clear_fields.setFont(font)
        self.pushButton_clear_fields.setObjectName(_fromUtf8("pushButton_clear_fields"))
        self.Controller_Plant_textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.Controller_Plant_textBrowser.setGeometry(QtCore.QRect(260, 460, 171, 81))
        self.Controller_Plant_textBrowser.setObjectName(_fromUtf8("Controller_Plant_textBrowser"))
        self.label_Controller_Plant_Label = QtGui.QLabel(self.centralwidget)
        self.label_Controller_Plant_Label.setGeometry(QtCore.QRect(250, 440, 191, 21))
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_Controller_Plant_Label.setFont(font)
        self.label_Controller_Plant_Label.setObjectName(_fromUtf8("label_Controller_Plant_Label"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(60, 380, 101, 91))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.checkBox_OS = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        
        font = QtGui.QFont()
        font.setPointSize(11)
        
        self.checkBox_OS.setFont(font)
        self.checkBox_OS.setAutoFillBackground(False)
        self.checkBox_OS.setObjectName(_fromUtf8("checkBox_OS"))
        self.verticalLayout_5.addWidget(self.checkBox_OS)
        self.checkBox_Ts = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        
        font = QtGui.QFont()
        font.setPointSize(11)
        
        self.checkBox_Ts.setFont(font)
        self.checkBox_Ts.setObjectName(_fromUtf8("checkBox_Ts"))
        self.verticalLayout_5.addWidget(self.checkBox_Ts)
        self.checkBox_Error = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_Error.setFont(font)
        self.checkBox_Error.setObjectName(_fromUtf8("checkBox_Error"))
        self.verticalLayout_5.addWidget(self.checkBox_Error)
        self.checkBox_Fill = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_Fill.setFont(font)
        self.checkBox_Fill.setChecked(True)
        self.checkBox_Fill.setObjectName(_fromUtf8("checkBox_Fill"))
        self.verticalLayout_5.addWidget(self.checkBox_Fill)
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(420, 120, 61, 141))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.lineEdit_z1_im = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_z1_im.setObjectName(_fromUtf8("lineEdit_z1_im"))
        self.verticalLayout_6.addWidget(self.lineEdit_z1_im)
        self.lineEdit_z2_im = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_z2_im.setObjectName(_fromUtf8("lineEdit_z2_im"))
        self.verticalLayout_6.addWidget(self.lineEdit_z2_im)
        self.lineEdit_p1_im = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_p1_im.setObjectName(_fromUtf8("lineEdit_p1_im"))
        self.verticalLayout_6.addWidget(self.lineEdit_p1_im)
        self.lineEdit_p2_im = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_p2_im.setObjectName(_fromUtf8("lineEdit_p2_im"))
        self.verticalLayout_6.addWidget(self.lineEdit_p2_im)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 96, 131, 20))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_Re = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_Re.setObjectName(_fromUtf8("label_Re"))
        self.horizontalLayout.addWidget(self.label_Re)
        self.label_Im = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_Im.setObjectName(_fromUtf8("label_Im"))
        self.horizontalLayout.addWidget(self.label_Im)
        self.pushButton_Quit = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Quit.setGeometry(QtCore.QRect(350, 550, 91, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Quit.setFont(font)
        self.pushButton_Quit.setObjectName(_fromUtf8("pushButton_Quit"))
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(241, 120, 31, 141))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.verticalLayout_complex_buttons = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_complex_buttons.setObjectName(_fromUtf8("verticalLayout_complex_buttons"))

        self.label_Plot_Options = QtGui.QLabel(self.centralwidget)
        self.label_Plot_Options.setGeometry(QtCore.QRect(10, 400, 51, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.label_Plot_Options.setFont(font)
        self.label_Plot_Options.setObjectName(_fromUtf8("label_Plot_Options"))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)

        self.label_x_times = QtGui.QLabel(self.centralwidget)
        self.label_x_times.setGeometry(QtCore.QRect(290, 60, 16, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_x_times.setFont(font)
        self.label_x_times.setObjectName(_fromUtf8("label_x_times"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSISO_Toolbox = QtGui.QMenu(self.menubar)
        self.menuSISO_Toolbox.setObjectName(_fromUtf8("menuSISO_Toolbox"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionSave_Image = QtGui.QAction(MainWindow)
        self.actionSave_Image.setObjectName(_fromUtf8("actionSave_Image"))
        self.actionSISO_Documentation = QtGui.QAction(MainWindow)
        self.actionSISO_Documentation.setObjectName(_fromUtf8("actionSISO_Documentation"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuSISO_Toolbox.addAction(self.actionAbout)
        self.menuSISO_Toolbox.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionSISO_Documentation)
        self.menubar.addAction(self.menuSISO_Toolbox.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.textBrowser.insertPlainText('SISO Toolbox')
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_2.clicked.connect(self.updateUI)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lineEdit_6.setText(_translate("MainWindow", '1.0', None))
        self.pushButton_2.setText(_translate("MainWindow", "Run", None))
        self.label_3.setText(_translate("MainWindow", "Zero 1:", None))
        self.label_4.setText(_translate("MainWindow", "Zero 2:", None))
        self.label_5.setText(_translate("MainWindow", "Pole 1:", None))
        self.label_6.setText(_translate("MainWindow", "Pole 2:", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "PID", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "PI-Lead", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "PD", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Proportional", None))
        self.label_2.setText(_translate("MainWindow", "Zero / Pole Controller Form", None))
        self.label.setText(_translate("MainWindow", "Controller Gain (K)", None))
        self.lineEdit.setText(_translate("MainWindow", "0", None))
        self.lineEdit_2.setText(_translate("MainWindow", "0", None))
        self.lineEdit_4.setText(_translate("MainWindow", "0", None))
        self.lineEdit_5.setText(_translate("MainWindow", "0", None))
        self.checkBox_2.setText(_translate("MainWindow", "Plant Step Response", None))
        self.checkBox.setText(_translate("MainWindow", "Pole Zero Map", None))
        self.checkBox_3.setText(_translate("MainWindow", "Bode", None))
        self.checkBox_4.setText(_translate("MainWindow", "Add Controller", None))
        self.label_7.setText(_translate("MainWindow", "  TRANSFER FUNCTION", None))
        self.label_8.setText(_translate("MainWindow", "       Numerator Polynomial", None))
        self.lineEdit_3.setText(_translate("MainWindow", "1,4", None))
        self.label_9.setText(_translate("MainWindow", "     Denominator Polynomial   ", None))
        self.lineEdit_7.setText(_translate("MainWindow", "1,3,6", None))
        self.label_10.setText(_translate("MainWindow", "Plots", None))
        self.Label_System_Char.setText(_translate("MainWindow", "System Characteristics ", None))
        self.Label_Plant_TF.setText(_translate("MainWindow", "Plant Transfer Function      ", None))
        self.pushButton_clear_fields.setText(_translate("MainWindow", "Clear All Fields", None))
        self.label_Controller_Plant_Label.setText(_translate("MainWindow", "Controller + Plant Transfer Function", None))
        self.checkBox_OS.setText(_translate("MainWindow", "%OS", None))
        self.checkBox_Ts.setText(_translate("MainWindow", "Settling Time", None))
        self.checkBox_Error.setText(_translate("MainWindow", "Error", None))
        self.checkBox_Fill.setText(_translate("MainWindow", "Step Fill", None))
        self.lineEdit_z1_im.setText(_translate("MainWindow", "0j", None))
        self.lineEdit_z2_im.setText(_translate("MainWindow", "0j", None))
        self.lineEdit_p1_im.setText(_translate("MainWindow", "0j", None))
        self.lineEdit_p2_im.setText(_translate("MainWindow", "0j", None))
        self.label_Re.setText(_translate("MainWindow", "      Re", None))
        self.label_Im.setText(_translate("MainWindow", "        Im", None))
        self.pushButton_Quit.setText(_translate("MainWindow", "QUIT", None))
        self.label_Plot_Options.setText(_translate("MainWindow", "Controller\n"
"     Plot\n"
"  Options", None))

        self.label_x_times.setText(_translate("MainWindow", "X", None))
        self.menuSISO_Toolbox.setTitle(_translate("MainWindow", "SISO Toolbox", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionSave.setText(_translate("MainWindow", "Save Images", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionExport.setText(_translate("MainWindow", "Export", None))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image", None))
        self.actionSISO_Documentation.setText(_translate("MainWindow", "SISO Documentation", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

    def updateUI(self) :
        get_num = self.lineEdit_3.text()
        get_den = self.lineEdit_7.text()
        num = get_num.split(",")
        num = map(float,num)
        den = get_den.split(",")
        den = map(float,den)
        system = (num,den)
        t, y = step2(system)
        w, mag, phase = bode(system)
        TF = tf(num,den)
        OS_TS = tfchar(TF)
        os = str(OS_TS[0])
        ts = str(OS_TS[1])      
        size = len(t)
        dcgain = y[size-1]
        x = np.linspace(dcgain,dcgain,size)
        self.Plant_tf_textBrowser.insertPlainText(TF)

                
        if self.checkBox_2.isChecked():
            self.plot.axes.plot(t,x,'k--')
            self.plot.axes.plot(t,y,'k')
            self.plot.axes.fill_between(t,y,dcgain,color='b',alpha=0.5)
            self.plot.axes.set_title('Step Response')
            self.plot.axes.set_xlabel('Time (sec)')
            self.plot.axes.set_ylabel('Amplitude')
            self.plot.axes.grid()
            self.plot.show()
            self.plot.draw()
            
        if self.checkBox_3.isChecked():
            self.plot2.axes.semilogx(w,mag,'k')
            self.plot2.axes.set_title('Bode Magnitude Plot')
            self.plot2.axes.set_xlabel('Magnitude')
            self.plot2.axes.set_ylabel('Omega (w)')
            self.plot2.axes.grid()
            self.plot2.draw()
            self.plot2.show()
            
            self.plot3.axes.semilogx(w,phase,'k')
            self.plot3.axes.set_title('Bode Phase Plot')
            self.plot3.axes.set_xlabel('Phase Angle')
            self.plot3.axes.set_ylabel('Omega (w)')
            self.plot3.axes.grid()
            self.plot3.draw()
            self.plot3.show()

        if self.checkBox.isChecked():
            self.root()
            
        if self.checkBox_4.isChecked():
            z1 = self.lineEdit.text()
            z2 = self.lineEdit_2.text()
            p1 = self.lineEdit_4.text()
            p2 = self.lineEdit_5.text()
            K = self.lineEdit_6.text()
            z1 = float(z1)
            z2 = float(z2)
            p1 = float(p1)
            p2 = float(p2)
            K = float(K)
            selection = self.comboBox.currentText()
            selection = str(selection)
            
            if K == 0.0:
                return_error = 'K = 0' + '\n' + 'The gain of the system is 0' + '\n' + 'Can not step response'
                self.textBrowser.insertPlainText(return_error)
                
            if selection == 'Proportional':
                num_P = []
                for i in num:
                    num_P.append(K*i)
                
                den_P = np.polyadd(den,num_P)
                system_P = (num_P,den_P)
                t_P, y_P = step2(system_P)
                w_P, mag_P, phase_P = bode(system_P)
                
                # %OverShoot & Settling time
                a_max = np.amax(y_P)
                size_P = len(t_P)
                dcgain_P = y_P[size_P - 1]
                OS = (a_max - dcgain_P)*100
                OS = format(OS, '.2f')
                OS = str(OS + '%')
                if y_P[0] == 0:
                    dcgain_P = 0.0
                count = 0
                count2 = -1
                for i in y_P:
                    count = count + 1
                    if i == a_max:
                        stop_value = count - 1
                        break
                for j in t_P:
                    count2 = count2 + 1


                OS_x = np.linspace(0,t_P[stop_value],size_P)
                OS_y = np.linspace(a_max,a_max,size_P)
                OS_x1 = np.linspace(t_P[stop_value],t_P[stop_value],size_P)
                OS_y2 = np.linspace(dcgain_P,a_max,size_P)
                x_P = np.linspace(dcgain_P,dcgain_P,size_P)

                if self.checkBox_OS.isChecked():
                    OS_x = np.linspace(0,t_P[stop_value],size_P)
                    OS_y = np.linspace(a_max,a_max,size_P)
                    OS_x1 = np.linspace(t_P[stop_value],t_P[stop_value],size_P)
                    OS_y2 = np.linspace(dcgain_P,a_max,size_P)
                else:
                    OS_x = np.linspace(0,0,size_P)
                    OS_y = np.linspace(0,0,size_P)
                    OS_x1 = np.linspace(0,0,size_P)
                    OS_y2 = np.linspace(0,0,size_P)

                if self.checkBox_Error.isChecked():
                    e_t = 0.02*(dcgain_P) + dcgain_P
                    e_b = dcgain_P - 0.02*(dcgain_P)
                    error_t_x = np.linspace(0,t_P[count2],size_P)
                    error_t_y = np.linspace(e_t,e_t,size_P)
                    error_b_x = np.linspace(0,t_P[count2],size_P)
                    error_b_y = np.linspace(e_b,e_b,size_P)
                else:
                    e_t = 0.02*(dcgain_P) + dcgain_P
                    e_b = dcgain_P - 0.02*(dcgain_P)
                    error_t_x = np.linspace(0,0,size_P)
                    error_t_y = np.linspace(0,0,size_P)
                    error_b_x = np.linspace(0,0,size_P)
                    error_b_y = np.linspace(0,0,size_P)

                flag = -1
                for i in reversed(y_P):
                    flag = flag + 1
                    if (i > e_t or i < e_b):
                        break

                new_t = []
                for j in reversed(t_P):
                    new_t.append(j)

                Ts = new_t[flag]

                if self.checkBox_Ts.isChecked():
                    t_s_x = np.linspace(Ts,Ts,size_P)
                    t_s_y = np.linspace(0,dcgain_P,size_P)
                else:
                    t_s_x = np.linspace(0,0,size_P)
                    t_s_y = np.linspace(0,0,size_P)

                self.plot4.axes.plot(t_P,y_P,'k',t_P,x_P, 'k--', OS_x, OS_y, 'k-.',OS_x1, OS_y2, 'k-.', error_t_x,error_t_y,'r--', error_b_x,error_b_y,'r--', t_s_x, t_s_y, 'k--')
                if self.checkBox_Fill.isChecked():
                    self.plot4.axes.fill_between(t_P,y_P,dcgain_P,color='b',alpha=0.5)
                else:
                    pass
                self.plot4.axes.set_title('Step Response (P)')
                self.plot4.axes.set_xlabel('Time (sec)')
                self.plot4.axes.set_ylabel('Amplitude')
                self.plot4.axes.grid()
                self.plot4.draw()
                self.plot4.show()
                
                Ts = format(Ts, '.2f')
                Ts = str(Ts + 's')
                K = str(K)
                return_P  = 'K = ' + ' ' +  K 
                self.textBrowser.insertPlainText(return_P)
                return_char = 'Overshoot = ' + ' ' + OS + '\n' + 'Settling Time =' + ' ' + Ts 
                self.System_Characteristics_textBrowser.insertPlainText(return_char)

                if self.checkBox_3.isChecked():
                    self.plot2.axes.semilogx(w_P,mag_P,'k')
                    self.plot2.axes.set_title('Bode Magnitude Plot (P)')
                    self.plot2.axes.set_xlabel('Magnitude')
                    self.plot2.axes.set_ylabel('Omega (w)')
                    self.plot2.axes.grid()
                    self.plot2.draw()
                    self.plot2.show()
                    
                    self.plot3.axes.semilogx(w_P,phase_P,'k')
                    self.plot3.axes.set_title('Bode Phase Plot (P)')
                    self.plot3.axes.set_xlabel('Phase Angle')
                    self.plot3.axes.set_ylabel('Omega (w)')
                    self.plot3.axes.grid()
                    self.plot3.draw()
                    self.plot3.show()
                
            if selection == 'PID':
                N_c = [K, K*(z1 + z2), K*z1*z2]
                D_c = [1,0]
                Numerator = np.convolve(num,N_c)
                DgDc = np.convolve(den,D_c)
                Denominator = np.polyadd(DgDc,Numerator)
                system_PID = (Numerator,Denominator)

                t_PID, y_PID = step2(system_PID)
                w_PID, mag_PID, phase_PID = bode(system_PID)
                
                 # %OverShoot & Settling time
                a_max = np.amax(y_PID)
                size_PID = len(t_PID)
                dcgain_PID = y_PID[size_PID - 1]
                OS = (a_max - dcgain_PID)*100
                OS = format(OS, '.2f')
                OS = str(OS + '%')
                if y_PID[0] == 0:
                    dcgain_PID = 0.0
                count = 0
                count2 = -1
                for i in y_PID:
                    count = count + 1
                    if i == a_max:
                        stop_value = count - 1
                        break
                for j in t_PID:
                    count2 = count2 + 1

                x_PID = np.linspace(dcgain_PID,dcgain_PID,size_PID)
                if self.checkBox_OS.isChecked():
                    OS_x = np.linspace(0,t_PID[stop_value],size_PID)
                    OS_y = np.linspace(a_max,a_max,size_PID)
                    OS_x1 = np.linspace(t_PID[stop_value],t_PID[stop_value],size_PID)
                    OS_y2 = np.linspace(dcgain_PID,a_max,size_PID)
                else:
                    OS_x = np.linspace(0,0,size_PID)
                    OS_y = np.linspace(0,0,size_PID)
                    OS_x1 = np.linspace(0,0,size_PID)
                    OS_y2 = np.linspace(0,0,size_PID)

                if self.checkBox_Error.isChecked():
                    e_t = 0.02*(dcgain_PID) + dcgain_PID
                    e_b = dcgain_PID - 0.02*(dcgain_PID)
                    error_t_x = np.linspace(0,t_PID[count2],size_PID)
                    error_t_y = np.linspace(e_t,e_t,size_PID)
                    error_b_x = np.linspace(0,t_PID[count2],size_PID)
                    error_b_y = np.linspace(e_b,e_b,size_PID)
                else:
                    e_t = 0.02*(dcgain_PID) + dcgain_PID
                    e_b = dcgain_PID - 0.02*(dcgain_PID)
                    error_t_x = np.linspace(0,0,size_PID)
                    error_t_y = np.linspace(0,0,size_PID)
                    error_b_x = np.linspace(0,0,size_PID)
                    error_b_y = np.linspace(0,0,size_PID)

                flag = -1
                for i in reversed(y_PID):
                    flag = flag + 1
                    if (i > e_t or i < e_b):
                        break

                new_t = []
                for j in reversed(t_PID):
                    new_t.append(j)

                Ts = new_t[flag]

                if self.checkBox_Ts.isChecked():
                    t_s_x = np.linspace(Ts,Ts,size_PID)
                    t_s_y = np.linspace(0,dcgain_PID,size_PID)
                else:
                    t_s_x = np.linspace(0,0,size_PID)
                    t_s_y = np.linspace(0,0,size_PID)

                self.plot4.axes.plot(t_PID,y_PID,'k',t_PID,x_PID, 'k--', OS_x, OS_y, 'k-.',OS_x1, OS_y2, 'k-.', error_t_x,error_t_y,'r--', error_b_x,error_b_y,'r--', t_s_x, t_s_y, 'k--')
                if self.checkBox_Fill.isChecked():
                    self.plot4.axes.fill_between(t_PID,y_PID,dcgain_PID,color='b',alpha=0.5)
                else:
                    pass

                self.plot4.axes.set_title('Step Response (PID)')
                self.plot4.axes.set_xlabel('Time (sec)')
                self.plot4.axes.set_ylabel('Amplitude')
                self.plot4.axes.grid()
                self.plot4.draw()
                self.plot4.show()
                z1_dis = str(z1)
                z2_dis = str(z2)
                Ts = format(Ts, '.2f')
                Ts = str(Ts + 's')
                
                return_char = 'Overshoot = ' + ' ' + OS + '\n' + 'Settling Time =' + ' ' + Ts
                return_PID = '(s' + ' ' + '+' + ' ' + z1_dis + ')' + ' ' + '(s' + ' ' + '+' + ' ' + z2_dis + ')' + '\n' + '-----------------------' + '\n' + '           ' + 's' 
                self.textBrowser.insertPlainText(return_PID)
                self.System_Characteristics_textBrowser.insertPlainText(return_char)
                
                if self.checkBox_3.isChecked():
                    self.plot2.axes.semilogx(w_PID,mag_PID,'k')
                    self.plot2.axes.set_title('Bode Magnitude Plot (PID)')
                    self.plot2.axes.set_xlabel('Magnitude')
                    self.plot2.axes.set_ylabel('Omega (w)')
                    self.plot2.axes.grid()
                    self.plot2.draw()
                    self.plot2.show()
                    
                    self.plot3.axes.semilogx(w_PID,phase_PID,'k')
                    self.plot3.axes.set_title('Bode Phase Plot (PID)')
                    self.plot3.axes.set_xlabel('Phase Angle')
                    self.plot3.axes.set_ylabel('Omega (w)')
                    self.plot3.axes.grid()
                    self.plot3.draw()
                    self.plot3.show()
                
            if selection == 'PI-Lead':
                N_c = [K, K*(z1 + z2), K*z1*z2]
                D_c = [1,p1,0]
                Numerator = np.convolve(num,N_c)
                DgDc = np.convolve(den,D_c)
                Denominator = np.polyadd(DgDc,Numerator)
                system_PI_Lead = (Numerator,Denominator)
                t_PI_Lead, y_PI_Lead = step2(system_PI_Lead)
                w_PI_Lead, mag_PI_Lead, phase_PI_Lead = bode(system_PI_Lead)
                # %OverShoot & Settling time
                a_max = np.amax(y_PI_Lead)
                size_PI_Lead = len(t_PI_Lead)
                dcgain_PI_Lead = y_PI_Lead[size_PI_Lead - 1]
                OS = (a_max - dcgain_PI_Lead)*100
                OS = format(OS, '.2f')
                OS = str(OS + '%')
                if y_PI_Lead[0] == 0:
                    dcgain_PI_Lead = 0.0
                count = 0
                count2 = -1
                for i in y_PI_Lead:
                    count = count + 1
                    if i == a_max:
                        stop_value = count - 1
                        break
                for j in t_PI_Lead:
                    count2 = count2 + 1

                x_PI_Lead = np.linspace(dcgain_PI_Lead,dcgain_PI_Lead,size_PI_Lead)
                if self.checkBox_OS.isChecked():
                    OS_x = np.linspace(0,t_PI_Lead[stop_value],size_PI_Lead)
                    OS_y = np.linspace(a_max,a_max,size_PI_Lead)
                    OS_x1 = np.linspace(t_PI_Lead[stop_value],t_PI_Lead[stop_value],size_PI_Lead)
                    OS_y2 = np.linspace(dcgain_PI_Lead,a_max,size_PI_Lead)
                else:
                    OS_x = np.linspace(0,0,size_PI_Lead)
                    OS_y = np.linspace(0,0,size_PI_Lead)
                    OS_x1 = np.linspace(0,0,size_PI_Lead)
                    OS_y2 = np.linspace(0,0,size_PI_Lead)

                if self.checkBox_Error.isChecked():
                    e_t = 0.02*(dcgain_PI_Lead) + dcgain_PI_Lead
                    e_b = dcgain_PI_Lead - 0.02*(dcgain_PI_Lead)
                    error_t_x = np.linspace(0,t_PI_Lead[count2],size_PI_Lead)
                    error_t_y = np.linspace(e_t,e_t,size_PI_Lead)
                    error_b_x = np.linspace(0,t_PI_Lead[count2],size_PI_Lead)
                    error_b_y = np.linspace(e_b,e_b,size_PI_Lead)
                else:
                    e_t = 0.02*(dcgain_PI_Lead) + dcgain_PI_Lead
                    e_b = dcgain_PI_Lead - 0.02*(dcgain_PI_Lead)
                    error_t_x = np.linspace(0,0,size_PI_Lead)
                    error_t_y = np.linspace(0,0,size_PI_Lead)
                    error_b_x = np.linspace(0,0,size_PI_Lead)
                    error_b_y = np.linspace(0,0,size_PI_Lead)

                flag = -1
                for i in reversed(y_PI_Lead):
                    flag = flag + 1
                    if (i > e_t or i < e_b):
                        break

                new_t = []
                for j in reversed(t_PI_Lead):
                    new_t.append(j)

                Ts = new_t[flag]

                if self.checkBox_Ts.isChecked():
                    t_s_x = np.linspace(Ts,Ts,size_PI_Lead)
                    t_s_y = np.linspace(0,dcgain_PI_Lead,size_PI_Lead)
                else:
                    t_s_x = np.linspace(0,0,size_PI_Lead)
                    t_s_y = np.linspace(0,0,size_PI_Lead)

                self.plot4.axes.plot(t_PI_Lead,y_PI_Lead,'k',t_PI_Lead,x_PI_Lead, 'k--', OS_x, OS_y, 'k-.',OS_x1, OS_y2, 'k-.', error_t_x,error_t_y,'r--', error_b_x,error_b_y,'r--', t_s_x, t_s_y, 'k--')
                if self.checkBox_Fill.isChecked():
                    self.plot4.axes.fill_between(t_PI_Lead,y_PI_Lead,dcgain_PI_Lead,color='b',alpha=0.5)
                else:
                    pass
                self.plot4.axes.set_title('Step Response (PI-Lead)')
                self.plot4.axes.set_xlabel('Time (sec)')
                self.plot4.axes.set_ylabel('Amplitude')
                self.plot4.axes.grid()
                self.plot4.draw()
                self.plot4.show()
                z1_dis = str(z1)
                z2_dis = str(z2)
                p1_dis = str(p1)
                p2_dis = str(p2)
                Ts = format(Ts, '.2f')
                Ts = str(Ts + 's')
                return_PI_Lead = '(s' + ' ' + '+' + ' ' + z1_dis + ')' + ' ' + '(s' + ' ' + '+' + ' ' + z2_dis + ')' + '\n' + '-----------------------' + '\n' + '           ' + 's' + '(s' + ' ' + '+' + ' ' + p1_dis + ')'
                return_char = 'Overshoot = ' + ' ' + OS + '\n' + 'Settling Time =' + ' ' + Ts
                self.textBrowser.insertPlainText(return_PI_Lead)
                self.System_Characteristics_textBrowser.insertPlainText(return_char)
                
                if self.checkBox_3.isChecked():
                    self.plot2.axes.semilogx(w_PI_Lead,mag_PI_Lead,'k')
                    self.plot2.axes.set_title('Bode Magnitude Plot (PI-Lead)')
                    self.plot2.axes.set_xlabel('Magnitude')
                    self.plot2.axes.set_ylabel('Omega (w)')
                    self.plot2.axes.grid()
                    self.plot2.draw()
                    self.plot2.show()
                    
                    self.plot3.axes.semilogx(w_PI_Lead,phase_PI_Lead,'k')
                    self.plot3.axes.set_title('Bode Phase Plot (PI-Lead)')
                    self.plot3.axes.set_xlabel('Phase Angle')
                    self.plot3.axes.set_ylabel('Omega (w)')
                    self.plot3.axes.grid()
                    self.plot3.draw()
                    self.plot3.show()
                
            if selection == 'PD':
                N_c = [K, K*z1]
                Numerator = np.convolve(num,N_c)
                Denominator = np.polyadd(den,Numerator)
                system_PD = (Numerator,Denominator)
                t_PID, y_PID = step2(system_PD)
                w_PD, mag_PD, phase_PD = bode(system_PD)

                # %OverShoot & Settling time
                a_max = np.amax(y_PID)
                size_PID = len(t_PID)
                dcgain_PID = y_PID[size_PID - 1]
                OS = (a_max - dcgain_PID)*100
                OS = format(OS, '.2f')
                OS = str(OS + '%')
                if y_PID[0] == 0:
                    dcgain_PID = 0.0
                count = 0
                count2 = -1
                for i in y_PID:
                    count = count + 1
                    if i == a_max:
                        stop_value = count - 1
                        break
                for j in t_PID:
                    count2 = count2 + 1

                x_PID = np.linspace(dcgain_PID,dcgain_PID,size_PID)
                if self.checkBox_OS.isChecked():
                    OS_x = np.linspace(0,t_PID[stop_value],size_PID)
                    OS_y = np.linspace(a_max,a_max,size_PID)
                    OS_x1 = np.linspace(t_PID[stop_value],t_PID[stop_value],size_PID)
                    OS_y2 = np.linspace(dcgain_PID,a_max,size_PID)
                else:
                    OS_x = np.linspace(0,0,size_PID)
                    OS_y = np.linspace(0,0,size_PID)
                    OS_x1 = np.linspace(0,0,size_PID)
                    OS_y2 = np.linspace(0,0,size_PID)

                if self.checkBox_Error.isChecked():
                    e_t = 0.02*(dcgain_PID) + dcgain_PID
                    e_b = dcgain_PID - 0.02*(dcgain_PID)
                    error_t_x = np.linspace(0,t_PID[count2],size_PID)
                    error_t_y = np.linspace(e_t,e_t,size_PID)
                    error_b_x = np.linspace(0,t_PID[count2],size_PID)
                    error_b_y = np.linspace(e_b,e_b,size_PID)
                else:
                    e_t = 0.02*(dcgain_PID) + dcgain_PID
                    e_b = dcgain_PID - 0.02*(dcgain_PID)
                    error_t_x = np.linspace(0,0,size_PID)
                    error_t_y = np.linspace(0,0,size_PID)
                    error_b_x = np.linspace(0,0,size_PID)
                    error_b_y = np.linspace(0,0,size_PID)

                flag = -1
                for i in reversed(y_PID):
                    flag = flag + 1
                    if (i > e_t or i < e_b):
                        break

                new_t = []
                for j in reversed(t_PID):
                    new_t.append(j)

                Ts = new_t[flag]

                if self.checkBox_Ts.isChecked():
                    t_s_x = np.linspace(Ts,Ts,size_PID)
                    t_s_y = np.linspace(0,dcgain_PID,size_PID)
                else:
                    t_s_x = np.linspace(0,0,size_PID)
                    t_s_y = np.linspace(0,0,size_PID)

                self.plot4.axes.plot(t_PID,y_PID,'k',t_PID,x_PID, 'k--', OS_x, OS_y, 'k-.',OS_x1, OS_y2, 'k-.', error_t_x,error_t_y,'r--', error_b_x,error_b_y,'r--', t_s_x, t_s_y, 'k--')
                if self.checkBox_Fill.isChecked():
                    self.plot4.axes.fill_between(t_PID,y_PID,dcgain_PID,color='b',alpha=0.5)
                else:
                    pass
                self.plot4.axes.set_title('Step Response (PD)')
                self.plot4.axes.set_xlabel('Time (sec)')
                self.plot4.axes.set_ylabel('Amplitude')
                self.plot4.axes.grid()
                self.plot4.draw()
                self.plot4.show()
                z1_dis = str(z1)
                Ts = format(Ts, '.2f')
                Ts = str(Ts + 's')
                return_char = 'Overshoot = ' + ' ' + OS + '\n' + 'Settling Time =' + ' ' + Ts
                return_P  = '(s' + ' ' + '+' + ' ' + z1_dis + ')'
                self.textBrowser.insertPlainText(return_P)
                self.System_Characteristics_textBrowser.insertPlainText(return_char)


                if self.checkBox_3.isChecked():
                    self.plot2.axes.semilogx(w_PD,mag_PD,'k')
                    self.plot2.axes.set_title('Bode Magnitude Plot (PD)')
                    self.plot2.axes.set_xlabel('Magnitude')
                    self.plot2.axes.set_ylabel('Omega (w)')
                    self.plot2.axes.grid()
                    self.plot2.draw()
                    self.plot2.show()
                    
                    self.plot3.axes.semilogx(w_PD,phase_PD,'k')
                    self.plot3.axes.set_title('Bode Phase Plot (PD)')
                    self.plot3.axes.set_xlabel('Phase Angle')
                    self.plot3.axes.set_ylabel('Omega (w)')
                    self.plot3.axes.grid()
                    self.plot3.draw()
                    self.plot3.show()
                   
    def root(self):
        get_num = self.lineEdit_3.text()
        get_den = self.lineEdit_7.text()
        num = get_num.split(",")
        num = map(float,num)
        den = get_den.split(",")
        den = map(float,den)
        T = tf(num,den)
        pzmap(T)
        
    def clear(self):
        self.textBrowser.clear()
        self.System_Characteristics_textBrowser.clear()
        self.Plant_tf_textBrowser.clear()
        self.Controller_Plant_textBrowser.clear()


        
class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=7, height=6, dpi=60) :
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(False)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        t = np.arange(0.0,2.0,0.01)
        f = 1 - np.exp(-2*t)
        self.axes.plot(t,f,'k')
        self.axes.set_title('Step Response')
        self.axes.set_xlabel('Time (sec)')
        self.axes.set_ylabel('Amplitude')
        self.axes.grid()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

