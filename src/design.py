# Form implementation generated from reading ui file '.\res\design.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 490)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(632, 490))
        MainWindow.setMaximumSize(QtCore.QSize(632, 490))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWhatsThis("")
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitimagefolderLabel = QtWidgets.QLabel(self.centralwidget)
        self.splitimagefolderLabel.setGeometry(QtCore.QRect(20, 12, 98, 16))
        self.splitimagefolderLabel.setObjectName("splitimagefolderLabel")
        self.splitimagefolderLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.splitimagefolderLineEdit.setGeometry(QtCore.QRect(130, 10, 411, 22))
        self.splitimagefolderLineEdit.setReadOnly(True)
        self.splitimagefolderLineEdit.setObjectName("splitimagefolderLineEdit")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(539, 9, 75, 24))
        self.browseButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.browseButton.setObjectName("browseButton")
        self.xLabel = QtWidgets.QLabel(self.centralwidget)
        self.xLabel.setGeometry(QtCore.QRect(25, 139, 7, 16))
        self.xLabel.setObjectName("xLabel")
        self.liveimageCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.liveimageCheckBox.setEnabled(True)
        self.liveimageCheckBox.setGeometry(QtCore.QRect(120, 252, 129, 20))
        self.liveimageCheckBox.setChecked(True)
        self.liveimageCheckBox.setTristate(False)
        self.liveimageCheckBox.setObjectName("liveimageCheckBox")
        self.selectregionButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectregionButton.setGeometry(QtCore.QRect(5, 67, 101, 23))
        self.selectregionButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.selectregionButton.setObjectName("selectregionButton")
        self.similaritythresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.similaritythresholdLabel.setGeometry(QtCore.QRect(10, 380, 102, 32))
        self.similaritythresholdLabel.setObjectName("similaritythresholdLabel")
        self.similaritythresholdDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.similaritythresholdDoubleSpinBox.setGeometry(QtCore.QRect(150, 390, 64, 22))
        self.similaritythresholdDoubleSpinBox.setMaximum(1.0)
        self.similaritythresholdDoubleSpinBox.setSingleStep(0.01)
        self.similaritythresholdDoubleSpinBox.setProperty("value", 0.9)
        self.similaritythresholdDoubleSpinBox.setObjectName("similaritythresholdDoubleSpinBox")
        self.startautosplitterButton = QtWidgets.QPushButton(self.centralwidget)
        self.startautosplitterButton.setGeometry(QtCore.QRect(500, 425, 121, 31))
        self.startautosplitterButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.startautosplitterButton.setObjectName("startautosplitterButton")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(500, 385, 121, 31))
        self.resetButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.resetButton.setObjectName("resetButton")
        self.undosplitButton = QtWidgets.QPushButton(self.centralwidget)
        self.undosplitButton.setGeometry(QtCore.QRect(480, 250, 71, 24))
        self.undosplitButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.undosplitButton.setObjectName("undosplitButton")
        self.skipsplitButton = QtWidgets.QPushButton(self.centralwidget)
        self.skipsplitButton.setGeometry(QtCore.QRect(560, 250, 61, 24))
        self.skipsplitButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.skipsplitButton.setObjectName("skipsplitButton")
        self.pauseLabel = QtWidgets.QLabel(self.centralwidget)
        self.pauseLabel.setGeometry(QtCore.QRect(10, 420, 112, 32))
        self.pauseLabel.setObjectName("pauseLabel")
        self.checkfpsButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkfpsButton.setGeometry(QtCore.QRect(5, 225, 53, 21))
        self.checkfpsButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.checkfpsButton.setObjectName("checkfpsButton")
        self.fpsLabel = QtWidgets.QLabel(self.centralwidget)
        self.fpsLabel.setGeometry(QtCore.QRect(87, 225, 20, 20))
        self.fpsLabel.setObjectName("fpsLabel")
        self.showlivesimilarityCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.showlivesimilarityCheckBox.setEnabled(True)
        self.showlivesimilarityCheckBox.setGeometry(QtCore.QRect(10, 330, 124, 20))
        self.showlivesimilarityCheckBox.setChecked(True)
        self.showlivesimilarityCheckBox.setTristate(False)
        self.showlivesimilarityCheckBox.setObjectName("showlivesimilarityCheckBox")
        self.showhighestsimilarityCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.showhighestsimilarityCheckBox.setEnabled(True)
        self.showhighestsimilarityCheckBox.setGeometry(QtCore.QRect(10, 351, 145, 20))
        self.showhighestsimilarityCheckBox.setChecked(True)
        self.showhighestsimilarityCheckBox.setTristate(False)
        self.showhighestsimilarityCheckBox.setObjectName("showhighestsimilarityCheckBox")
        self.livesimilarityLabel = QtWidgets.QLabel(self.centralwidget)
        self.livesimilarityLabel.setGeometry(QtCore.QRect(160, 332, 46, 16))
        self.livesimilarityLabel.setText("")
        self.livesimilarityLabel.setObjectName("livesimilarityLabel")
        self.highestsimilarityLabel = QtWidgets.QLabel(self.centralwidget)
        self.highestsimilarityLabel.setGeometry(QtCore.QRect(160, 353, 46, 16))
        self.highestsimilarityLabel.setText("")
        self.highestsimilarityLabel.setObjectName("highestsimilarityLabel")
        self.splitLabel = QtWidgets.QLabel(self.centralwidget)
        self.splitLabel.setGeometry(QtCore.QRect(230, 317, 58, 16))
        self.splitLabel.setObjectName("splitLabel")
        self.resetLabel = QtWidgets.QLabel(self.centralwidget)
        self.resetLabel.setGeometry(QtCore.QRect(230, 341, 28, 16))
        self.resetLabel.setObjectName("resetLabel")
        self.skiptsplitLabel = QtWidgets.QLabel(self.centralwidget)
        self.skiptsplitLabel.setGeometry(QtCore.QRect(230, 367, 48, 16))
        self.skiptsplitLabel.setObjectName("skiptsplitLabel")
        self.undosplitLabel = QtWidgets.QLabel(self.centralwidget)
        self.undosplitLabel.setGeometry(QtCore.QRect(230, 393, 55, 16))
        self.undosplitLabel.setObjectName("undosplitLabel")
        self.splitLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.splitLineEdit.setGeometry(QtCore.QRect(300, 314, 81, 20))
        self.splitLineEdit.setReadOnly(True)
        self.splitLineEdit.setObjectName("splitLineEdit")
        self.undosplitLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.undosplitLineEdit.setGeometry(QtCore.QRect(300, 391, 81, 20))
        self.undosplitLineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.undosplitLineEdit.setReadOnly(True)
        self.undosplitLineEdit.setObjectName("undosplitLineEdit")
        self.skipsplitLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.skipsplitLineEdit.setGeometry(QtCore.QRect(300, 365, 81, 20))
        self.skipsplitLineEdit.setReadOnly(True)
        self.skipsplitLineEdit.setObjectName("skipsplitLineEdit")
        self.resetLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.resetLineEdit.setGeometry(QtCore.QRect(300, 339, 81, 20))
        self.resetLineEdit.setReadOnly(True)
        self.resetLineEdit.setObjectName("resetLineEdit")
        self.setsplithotkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.setsplithotkeyButton.setGeometry(QtCore.QRect(390, 314, 81, 21))
        self.setsplithotkeyButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.setsplithotkeyButton.setObjectName("setsplithotkeyButton")
        self.setresethotkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.setresethotkeyButton.setGeometry(QtCore.QRect(390, 339, 81, 21))
        self.setresethotkeyButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.setresethotkeyButton.setObjectName("setresethotkeyButton")
        self.setskipsplithotkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.setskipsplithotkeyButton.setGeometry(QtCore.QRect(390, 365, 81, 21))
        self.setskipsplithotkeyButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.setskipsplithotkeyButton.setObjectName("setskipsplithotkeyButton")
        self.setundosplithotkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.setundosplithotkeyButton.setGeometry(QtCore.QRect(390, 391, 81, 21))
        self.setundosplithotkeyButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.setundosplithotkeyButton.setObjectName("setundosplithotkeyButton")
        self.line_left = QtWidgets.QFrame(self.centralwidget)
        self.line_left.setGeometry(QtCore.QRect(220, 296, 2, 163))
        self.line_left.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_left.setLineWidth(1)
        self.line_left.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_left.setObjectName("line_left")
        self.timerglobalhotkeysLabel = QtWidgets.QLabel(self.centralwidget)
        self.timerglobalhotkeysLabel.setGeometry(QtCore.QRect(300, 293, 113, 16))
        self.timerglobalhotkeysLabel.setObjectName("timerglobalhotkeysLabel")
        self.line_right = QtWidgets.QFrame(self.centralwidget)
        self.line_right.setGeometry(QtCore.QRect(490, 296, 2, 163))
        self.line_right.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_right.setLineWidth(1)
        self.line_right.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_right.setObjectName("line_right")
        self.liveImage = QtWidgets.QLabel(self.centralwidget)
        self.liveImage.setGeometry(QtCore.QRect(120, 69, 240, 180))
        self.liveImage.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.liveImage.setText("")
        self.liveImage.setObjectName("liveImage")
        self.currentSplitImage = QtWidgets.QLabel(self.centralwidget)
        self.currentSplitImage.setGeometry(QtCore.QRect(380, 69, 240, 180))
        self.currentSplitImage.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.currentSplitImage.setText("")
        self.currentSplitImage.setObjectName("currentSplitImage")
        self.currentsplitimageLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentsplitimageLabel.setGeometry(QtCore.QRect(450, 50, 102, 16))
        self.currentsplitimageLabel.setObjectName("currentsplitimageLabel")
        self.widthLabel = QtWidgets.QLabel(self.centralwidget)
        self.widthLabel.setGeometry(QtCore.QRect(14, 177, 31, 16))
        self.widthLabel.setObjectName("widthLabel")
        self.heightLabel = QtWidgets.QLabel(self.centralwidget)
        self.heightLabel.setGeometry(QtCore.QRect(68, 177, 31, 16))
        self.heightLabel.setObjectName("heightLabel")
        self.fpsvalueLabel = QtWidgets.QLabel(self.centralwidget)
        self.fpsvalueLabel.setGeometry(QtCore.QRect(58, 225, 26, 20))
        self.fpsvalueLabel.setText("")
        self.fpsvalueLabel.setObjectName("fpsvalueLabel")
        self.widthSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.widthSpinBox.setGeometry(QtCore.QRect(6, 193, 44, 22))
        self.widthSpinBox.setMinimum(1)
        self.widthSpinBox.setMaximum(10000)
        self.widthSpinBox.setProperty("value", 640)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.heightSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.heightSpinBox.setGeometry(QtCore.QRect(62, 193, 44, 22))
        self.heightSpinBox.setMinimum(1)
        self.heightSpinBox.setMaximum(10000)
        self.heightSpinBox.setProperty("value", 480)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.captureregionLabel = QtWidgets.QLabel(self.centralwidget)
        self.captureregionLabel.setGeometry(QtCore.QRect(200, 50, 82, 16))
        self.captureregionLabel.setObjectName("captureregionLabel")
        self.fpslimitLabel = QtWidgets.QLabel(self.centralwidget)
        self.fpslimitLabel.setGeometry(QtCore.QRect(8, 251, 51, 16))
        self.fpslimitLabel.setObjectName("fpslimitLabel")
        self.fpslimitSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.fpslimitSpinBox.setGeometry(QtCore.QRect(62, 248, 44, 22))
        self.fpslimitSpinBox.setPrefix("")
        self.fpslimitSpinBox.setDecimals(0)
        self.fpslimitSpinBox.setMinimum(30.0)
        self.fpslimitSpinBox.setMaximum(5000.0)
        self.fpslimitSpinBox.setSingleStep(1.0)
        self.fpslimitSpinBox.setProperty("value", 60.0)
        self.fpslimitSpinBox.setObjectName("fpslimitSpinBox")
        self.currentsplitimagefileLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentsplitimagefileLabel.setGeometry(QtCore.QRect(380, 270, 241, 20))
        self.currentsplitimagefileLabel.setText("")
        self.currentsplitimagefileLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.currentsplitimagefileLabel.setObjectName("currentsplitimagefileLabel")
        self.takescreenshotButton = QtWidgets.QPushButton(self.centralwidget)
        self.takescreenshotButton.setGeometry(QtCore.QRect(250, 250, 92, 24))
        self.takescreenshotButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.takescreenshotButton.setObjectName("takescreenshotButton")
        self.xSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.xSpinBox.setGeometry(QtCore.QRect(6, 154, 44, 22))
        self.xSpinBox.setReadOnly(False)
        self.xSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.xSpinBox.setMinimum(0)
        self.xSpinBox.setMaximum(999999999)
        self.xSpinBox.setSingleStep(1)
        self.xSpinBox.setProperty("value", 0)
        self.xSpinBox.setObjectName("xSpinBox")
        self.ySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ySpinBox.setGeometry(QtCore.QRect(62, 154, 44, 22))
        self.ySpinBox.setReadOnly(False)
        self.ySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.ySpinBox.setMinimum(0)
        self.ySpinBox.setMaximum(999999999)
        self.ySpinBox.setProperty("value", 0)
        self.ySpinBox.setObjectName("ySpinBox")
        self.yLabel = QtWidgets.QLabel(self.centralwidget)
        self.yLabel.setGeometry(QtCore.QRect(81, 139, 7, 16))
        self.yLabel.setObjectName("yLabel")
        self.comparisonmethodComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comparisonmethodComboBox.setGeometry(QtCore.QRect(123, 300, 91, 22))
        self.comparisonmethodComboBox.setObjectName("comparisonmethodComboBox")
        self.comparisonmethodComboBox.addItem("")
        self.comparisonmethodComboBox.addItem("")
        self.comparisonmethodComboBox.addItem("")
        self.pauseDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pauseDoubleSpinBox.setGeometry(QtCore.QRect(150, 430, 64, 22))
        self.pauseDoubleSpinBox.setMaximum(999999999.0)
        self.pauseDoubleSpinBox.setSingleStep(1.0)
        self.pauseDoubleSpinBox.setProperty("value", 10.0)
        self.pauseDoubleSpinBox.setObjectName("pauseDoubleSpinBox")
        self.comparisonmethodLabel = QtWidgets.QLabel(self.centralwidget)
        self.comparisonmethodLabel.setGeometry(QtCore.QRect(10, 303, 110, 16))
        self.comparisonmethodLabel.setObjectName("comparisonmethodLabel")
        self.alignregionButton = QtWidgets.QPushButton(self.centralwidget)
        self.alignregionButton.setGeometry(QtCore.QRect(5, 92, 101, 23))
        self.alignregionButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.alignregionButton.setObjectName("alignregionButton")
        self.groupDummySplitsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.groupDummySplitsCheckBox.setGeometry(QtCore.QRect(230, 443, 261, 20))
        self.groupDummySplitsCheckBox.setChecked(False)
        self.groupDummySplitsCheckBox.setObjectName("groupDummySplitsCheckBox")
        self.selectwindowButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectwindowButton.setGeometry(QtCore.QRect(5, 117, 101, 23))
        self.selectwindowButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.selectwindowButton.setObjectName("selectwindowButton")
        self.imageloopLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageloopLabel.setGeometry(QtCore.QRect(380, 252, 108, 20))
        self.imageloopLabel.setObjectName("imageloopLabel")
        self.pausehotkeyLabel = QtWidgets.QLabel(self.centralwidget)
        self.pausehotkeyLabel.setGeometry(QtCore.QRect(230, 418, 31, 16))
        self.pausehotkeyLabel.setObjectName("pausehotkeyLabel")
        self.pausehotkeyLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pausehotkeyLineEdit.setGeometry(QtCore.QRect(300, 416, 81, 20))
        self.pausehotkeyLineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.pausehotkeyLineEdit.setReadOnly(True)
        self.pausehotkeyLineEdit.setObjectName("pausehotkeyLineEdit")
        self.setpausehotkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.setpausehotkeyButton.setGeometry(QtCore.QRect(390, 416, 81, 21))
        self.setpausehotkeyButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.setpausehotkeyButton.setObjectName("setpausehotkeyButton")
        self.loopCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.loopCheckBox.setEnabled(True)
        self.loopCheckBox.setGeometry(QtCore.QRect(500, 340, 117, 20))
        self.loopCheckBox.setChecked(False)
        self.loopCheckBox.setTristate(False)
        self.loopCheckBox.setObjectName("loopCheckBox")
        self.autostartonresetCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.autostartonresetCheckBox.setGeometry(QtCore.QRect(500, 360, 126, 20))
        self.autostartonresetCheckBox.setChecked(False)
        self.autostartonresetCheckBox.setTristate(False)
        self.autostartonresetCheckBox.setObjectName("autostartonresetCheckBox")
        self.startImageReloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.startImageReloadButton.setGeometry(QtCore.QRect(500, 300, 121, 31))
        self.startImageReloadButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.startImageReloadButton.setObjectName("startImageReloadButton")
        self.startImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.startImageLabel.setGeometry(QtCore.QRect(120, 270, 241, 16))
        self.startImageLabel.setObjectName("startImageLabel")
        self.splitimagefolderLabel.raise_()
        self.splitimagefolderLineEdit.raise_()
        self.browseButton.raise_()
        self.xLabel.raise_()
        self.liveimageCheckBox.raise_()
        self.selectregionButton.raise_()
        self.similaritythresholdLabel.raise_()
        self.similaritythresholdDoubleSpinBox.raise_()
        self.startautosplitterButton.raise_()
        self.resetButton.raise_()
        self.undosplitButton.raise_()
        self.skipsplitButton.raise_()
        self.pauseLabel.raise_()
        self.checkfpsButton.raise_()
        self.fpsLabel.raise_()
        self.showlivesimilarityCheckBox.raise_()
        self.showhighestsimilarityCheckBox.raise_()
        self.livesimilarityLabel.raise_()
        self.highestsimilarityLabel.raise_()
        self.splitLabel.raise_()
        self.resetLabel.raise_()
        self.skiptsplitLabel.raise_()
        self.undosplitLabel.raise_()
        self.splitLineEdit.raise_()
        self.undosplitLineEdit.raise_()
        self.skipsplitLineEdit.raise_()
        self.resetLineEdit.raise_()
        self.setsplithotkeyButton.raise_()
        self.setresethotkeyButton.raise_()
        self.setskipsplithotkeyButton.raise_()
        self.setundosplithotkeyButton.raise_()
        self.line_left.raise_()
        self.timerglobalhotkeysLabel.raise_()
        self.line_right.raise_()
        self.currentsplitimageLabel.raise_()
        self.liveImage.raise_()
        self.currentSplitImage.raise_()
        self.widthLabel.raise_()
        self.heightLabel.raise_()
        self.fpsvalueLabel.raise_()
        self.widthSpinBox.raise_()
        self.heightSpinBox.raise_()
        self.captureregionLabel.raise_()
        self.fpslimitLabel.raise_()
        self.fpslimitSpinBox.raise_()
        self.currentsplitimagefileLabel.raise_()
        self.takescreenshotButton.raise_()
        self.xSpinBox.raise_()
        self.ySpinBox.raise_()
        self.yLabel.raise_()
        self.comparisonmethodComboBox.raise_()
        self.pauseDoubleSpinBox.raise_()
        self.comparisonmethodLabel.raise_()
        self.alignregionButton.raise_()
        self.groupDummySplitsCheckBox.raise_()
        self.selectwindowButton.raise_()
        self.imageloopLabel.raise_()
        self.pausehotkeyLabel.raise_()
        self.pausehotkeyLineEdit.raise_()
        self.setpausehotkeyButton.raise_()
        self.loopCheckBox.raise_()
        self.autostartonresetCheckBox.raise_()
        self.startImageReloadButton.raise_()
        self.startImageLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 632, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionView_Help = QtGui.QAction(MainWindow)
        self.actionView_Help.setObjectName("actionView_Help")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSplit_Settings = QtGui.QAction(MainWindow)
        self.actionSplit_Settings.setObjectName("actionSplit_Settings")
        self.actionSave_Settings = QtGui.QAction(MainWindow)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionLoad_Settings = QtGui.QAction(MainWindow)
        self.actionLoad_Settings.setObjectName("actionLoad_Settings")
        self.actionSave_Settings_As = QtGui.QAction(MainWindow)
        self.actionSave_Settings_As.setObjectName("actionSave_Settings_As")
        self.menuHelp.addAction(self.actionView_Help)
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionSave_Settings)
        self.menuFile.addAction(self.actionSave_Settings_As)
        self.menuFile.addAction(self.actionLoad_Settings)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.splitimagefolderLineEdit, self.xSpinBox)
        MainWindow.setTabOrder(self.xSpinBox, self.ySpinBox)
        MainWindow.setTabOrder(self.ySpinBox, self.widthSpinBox)
        MainWindow.setTabOrder(self.widthSpinBox, self.heightSpinBox)
        MainWindow.setTabOrder(self.heightSpinBox, self.fpslimitSpinBox)
        MainWindow.setTabOrder(self.fpslimitSpinBox, self.liveimageCheckBox)
        MainWindow.setTabOrder(self.liveimageCheckBox, self.comparisonmethodComboBox)
        MainWindow.setTabOrder(self.comparisonmethodComboBox, self.showlivesimilarityCheckBox)
        MainWindow.setTabOrder(self.showlivesimilarityCheckBox, self.showhighestsimilarityCheckBox)
        MainWindow.setTabOrder(self.showhighestsimilarityCheckBox, self.similaritythresholdDoubleSpinBox)
        MainWindow.setTabOrder(self.similaritythresholdDoubleSpinBox, self.pauseDoubleSpinBox)
        MainWindow.setTabOrder(self.pauseDoubleSpinBox, self.splitLineEdit)
        MainWindow.setTabOrder(self.splitLineEdit, self.resetLineEdit)
        MainWindow.setTabOrder(self.resetLineEdit, self.skipsplitLineEdit)
        MainWindow.setTabOrder(self.skipsplitLineEdit, self.undosplitLineEdit)
        MainWindow.setTabOrder(self.undosplitLineEdit, self.groupDummySplitsCheckBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoSplit"))
        self.splitimagefolderLabel.setText(_translate("MainWindow", "Split Image Folder:"))
        self.browseButton.setText(_translate("MainWindow", "Browse.."))
        self.xLabel.setText(_translate("MainWindow", "X"))
        self.liveimageCheckBox.setText(_translate("MainWindow", "Live Capture Region"))
        self.selectregionButton.setText(_translate("MainWindow", "Select Region"))
        self.similaritythresholdLabel.setText(_translate("MainWindow", "Similarity threshold\n"
"Default value"))
        self.startautosplitterButton.setText(_translate("MainWindow", "Start Auto Splitter"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.undosplitButton.setText(_translate("MainWindow", "Undo Split"))
        self.skipsplitButton.setText(_translate("MainWindow", "Skip Split"))
        self.pauseLabel.setText(_translate("MainWindow", "Pause time (seconds)\n"
"Default value"))
        self.checkfpsButton.setText(_translate("MainWindow", "Max FPS"))
        self.fpsLabel.setText(_translate("MainWindow", "FPS"))
        self.showlivesimilarityCheckBox.setText(_translate("MainWindow", "Show live similarity"))
        self.showhighestsimilarityCheckBox.setText(_translate("MainWindow", "Show highest similarity"))
        self.splitLabel.setText(_translate("MainWindow", "Start / Split"))
        self.resetLabel.setText(_translate("MainWindow", "Reset"))
        self.skiptsplitLabel.setText(_translate("MainWindow", "Skip Split"))
        self.undosplitLabel.setText(_translate("MainWindow", "Undo Split"))
        self.setsplithotkeyButton.setText(_translate("MainWindow", "Set Hotkey"))
        self.setresethotkeyButton.setText(_translate("MainWindow", "Set Hotkey"))
        self.setskipsplithotkeyButton.setText(_translate("MainWindow", "Set Hotkey"))
        self.setundosplithotkeyButton.setText(_translate("MainWindow", "Set Hotkey"))
        self.timerglobalhotkeysLabel.setText(_translate("MainWindow", "Timer Global Hotkeys"))
        self.currentsplitimageLabel.setText(_translate("MainWindow", "Current Split Image"))
        self.widthLabel.setText(_translate("MainWindow", "Width"))
        self.heightLabel.setText(_translate("MainWindow", "Height"))
        self.captureregionLabel.setText(_translate("MainWindow", "Capture Region"))
        self.fpslimitLabel.setText(_translate("MainWindow", "FPS Limit:"))
        self.takescreenshotButton.setText(_translate("MainWindow", "Take Screenshot"))
        self.yLabel.setText(_translate("MainWindow", "Y"))
        self.comparisonmethodComboBox.setItemText(0, _translate("MainWindow", "L2 Norm"))
        self.comparisonmethodComboBox.setItemText(1, _translate("MainWindow", "Histograms"))
        self.comparisonmethodComboBox.setItemText(2, _translate("MainWindow", "pHash"))
        self.comparisonmethodLabel.setText(_translate("MainWindow", "Comparison Method"))
        self.alignregionButton.setText(_translate("MainWindow", "Align Region"))
        self.groupDummySplitsCheckBox.setText(_translate("MainWindow", "Group dummy splits when undoing/skipping"))
        self.selectwindowButton.setText(_translate("MainWindow", "Select Window"))
        self.imageloopLabel.setText(_translate("MainWindow", "Image Loop #:"))
        self.pausehotkeyLabel.setText(_translate("MainWindow", "Pause"))
        self.setpausehotkeyButton.setText(_translate("MainWindow", "Set Hotkey"))
        self.loopCheckBox.setText(_translate("MainWindow", "Loop Split Images"))
        self.autostartonresetCheckBox.setText(_translate("MainWindow", "Auto Start On Reset"))
        self.startImageReloadButton.setText(_translate("MainWindow", "Reload Start Image"))
        self.startImageLabel.setText(_translate("MainWindow", "Start image:"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionView_Help.setText(_translate("MainWindow", "View Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSplit_Settings.setText(_translate("MainWindow", "Split Image Settings"))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Settings"))
        self.actionLoad_Settings.setText(_translate("MainWindow", "Load Settings"))
        self.actionSave_Settings_As.setText(_translate("MainWindow", "Save Settings As..."))
