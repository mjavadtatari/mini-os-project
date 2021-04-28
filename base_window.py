import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore


class BaseWindow(QMainWindow):
    """docstring fo BaseWindow."""

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(BaseWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("miniOS")
        # self.setFixedSize(1024,512)
        self.setGeometry(400, 400, 1024, 512)

        self.login_page = QWidget()

        self.initMenuBar()
        self.statusBar()

    def initMenuBar(self):
        # ------------------->Account Menu
        userNameAct = QAction('&Logged in as MJavadTatari', self)
        # userNameAct.setShortcut('Ctrl+W')
        userNameAct.setStatusTip('Welcome MJavadTatari')
        # userNameAct.triggered.connect(qApp.quit)

        chEmailAct = QAction('&Change Email', self)
        chEmailAct.setShortcut('Ctrl+E')
        chEmailAct.setStatusTip('Change Account Email')
        chEmailAct.triggered.connect(qApp.quit)

        chPassAct = QAction('&Change Password', self)
        chPassAct.setShortcut('Ctrl+P')
        chPassAct.setStatusTip('Change Account Password')
        chPassAct.triggered.connect(qApp.quit)

        logOutAct = QAction('&LogOut', self)
        logOutAct.setShortcut('Ctrl+L')
        logOutAct.setStatusTip('LogOut User')
        logOutAct.triggered.connect(qApp.quit)

        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Account')
        fileMenu.addAction(userNameAct)
        fileMenu.addAction(chEmailAct)
        fileMenu.addAction(chPassAct)
        fileMenu.addAction(logOutAct)
        fileMenu.addAction(exitAct)

        # ------------------->File Menu
        newFileAct = QAction('&New', self)
        newFileAct.setShortcut('Ctrl+Shift+N')
        newFileAct.setStatusTip('Create New File')
        newFileAct.triggered.connect(qApp.quit)

        deleteFileAct = QAction('&Delete', self)
        deleteFileAct.setShortcut('Ctrl+Shift+D')
        deleteFileAct.setStatusTip('Delete a File')
        deleteFileAct.triggered.connect(qApp.quit)

        copyFileAct = QAction('&Copy', self)
        copyFileAct.setShortcut('Ctrl+Shift+C')
        copyFileAct.setStatusTip('Copy a File')
        copyFileAct.triggered.connect(qApp.quit)

        moveFileAct = QAction('&Move', self)
        moveFileAct.setShortcut('Ctrl+Shift+M')
        moveFileAct.setStatusTip('Move a File')
        moveFileAct.triggered.connect(qApp.quit)

        renameFileAct = QAction('&Rename', self)
        renameFileAct.setShortcut('Ctrl+Shift+R')
        renameFileAct.setStatusTip('Rename a File')
        renameFileAct.triggered.connect(qApp.quit)

        sortTextAct = QAction('&Sort Text', self)
        sortTextAct.setShortcut('Ctrl+Shift+T')
        sortTextAct.setStatusTip('Sort Text file')
        sortTextAct.triggered.connect(qApp.quit)

        sortExcelAct = QAction('&Sort Excel', self)
        sortExcelAct.setShortcut('Ctrl+Shift+E')
        sortExcelAct.setStatusTip('Sort Excel file')
        sortExcelAct.triggered.connect(qApp.quit)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newFileAct)
        fileMenu.addAction(deleteFileAct)
        fileMenu.addAction(copyFileAct)
        fileMenu.addAction(moveFileAct)
        fileMenu.addAction(renameFileAct)
        fileMenu.addAction(sortTextAct)
        fileMenu.addAction(sortExcelAct)

        # ------------------->Directory Menu
        homeDirAct = QAction('&Home', self)
        homeDirAct.setShortcut('Ctrl+Alt+H')
        homeDirAct.setStatusTip('Show User\'s Root Directory')
        homeDirAct.triggered.connect(qApp.quit)

        newDirAct = QAction('&New', self)
        newDirAct.setShortcut('Ctrl+Alt+N')
        newDirAct.setStatusTip('Create New Directory')
        newDirAct.triggered.connect(qApp.quit)

        deleteDirAct = QAction('&Delete', self)
        deleteDirAct.setShortcut('Ctrl+Alt+D')
        deleteDirAct.setStatusTip('Delete a Directory')
        deleteDirAct.triggered.connect(qApp.quit)

        copyDirAct = QAction('&Copy', self)
        copyDirAct.setShortcut('Ctrl+Alt+C')
        copyDirAct.setStatusTip('Copy a Directory')
        copyDirAct.triggered.connect(qApp.quit)

        moveDirAct = QAction('&Move', self)
        moveDirAct.setShortcut('Ctrl+Alt+M')
        moveDirAct.setStatusTip('Move a Directory')
        moveDirAct.triggered.connect(qApp.quit)

        renameDirAct = QAction('&Rename', self)
        renameDirAct.setShortcut('Ctrl+Alt+R')
        renameDirAct.setStatusTip('Rename a Directory')
        renameDirAct.triggered.connect(qApp.quit)

        exportDirAct = QAction('&Export', self)
        exportDirAct.setShortcut('Ctrl+Alt+E')
        exportDirAct.setStatusTip('Export Directories as Excel File')
        exportDirAct.triggered.connect(qApp.quit)

        fileMenu = menubar.addMenu('&Directory')
        fileMenu.addAction(homeDirAct)
        fileMenu.addAction(newDirAct)
        fileMenu.addAction(deleteDirAct)
        fileMenu.addAction(copyDirAct)
        fileMenu.addAction(moveDirAct)
        fileMenu.addAction(renameDirAct)
        fileMenu.addAction(exportDirAct)

        # ------------------->Calculator Menu
        additionAct = QAction('&Addition', self)
        additionAct.setShortcut('Ctrl+Alt+Shift+A')
        additionAct.setStatusTip('Addition Multiple Numbers')
        additionAct.triggered.connect(qApp.quit)

        submissionAct = QAction('&Submission', self)
        submissionAct.setShortcut('Ctrl+Alt+Shift+S')
        submissionAct.setStatusTip('Submission Multiple Numbers')
        submissionAct.triggered.connect(qApp.quit)

        multiplicationAct = QAction('&Multiplication', self)
        multiplicationAct.setShortcut('Ctrl+Alt+Shift+M')
        multiplicationAct.setStatusTip('Multiplication Multiple Numbers')
        multiplicationAct.triggered.connect(qApp.quit)

        divisionAct = QAction('&Division', self)
        divisionAct.setShortcut('Ctrl+Alt+Shift+D')
        divisionAct.setStatusTip('Division Multiple Numbers')
        divisionAct.triggered.connect(qApp.quit)

        powerAct = QAction('&Power', self)
        powerAct.setShortcut('Ctrl+Alt+Shift+P')
        powerAct.setStatusTip('Power Multiple Numbers')
        powerAct.triggered.connect(qApp.quit)

        squaredAct = QAction('&Squared', self)
        squaredAct.setShortcut('Ctrl+Alt+Shift+Q')
        squaredAct.setStatusTip('Squared Multiple Numbers')
        squaredAct.triggered.connect(qApp.quit)

        modulusAct = QAction('&Modulus', self)
        modulusAct.setShortcut('Ctrl+Alt+Shift+O')
        modulusAct.setStatusTip('Modulus')
        modulusAct.triggered.connect(qApp.quit)

        lcmAct = QAction('&LCM', self)
        lcmAct.setShortcut('Ctrl+Alt+Shift+L')
        lcmAct.setStatusTip('Calculate Least Common Multiple')
        lcmAct.triggered.connect(qApp.quit)

        gcdAct = QAction('&GCD', self)
        gcdAct.setShortcut('Ctrl+Alt+Shift+G')
        gcdAct.setStatusTip('Calculate Greatest Common Divisor')
        gcdAct.triggered.connect(qApp.quit)

        numBasesAct = QAction('&Convert Bases', self)
        numBasesAct.setShortcut('Ctrl+Alt+Shift+B')
        numBasesAct.setStatusTip('Converting Number Bases')
        numBasesAct.triggered.connect(qApp.quit)

        fileMenu = menubar.addMenu('&Calculator')
        fileMenu.addAction(additionAct)
        fileMenu.addAction(submissionAct)
        fileMenu.addAction(multiplicationAct)
        fileMenu.addAction(divisionAct)
        fileMenu.addAction(powerAct)
        fileMenu.addAction(squaredAct)
        fileMenu.addAction(modulusAct)
        fileMenu.addAction(lcmAct)
        fileMenu.addAction(gcdAct)
        fileMenu.addAction(numBasesAct)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())



if __name__ == "__main__":

    window = BaseWindow(sys.argv)
    window.show()

    sys.exit(app.exec_())
