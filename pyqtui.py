# PyQt5 text area
# pythonprogramminglanguage.com

import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent =None):
        super().__init__(parent)
        self.setMinimumSize(QSize(500, 500))    
        self.setWindowTitle("PyQt5 Textarea example")
        self.text1 = QTextBrowser(self)
        self.text1.append("Original")
        self.text1.resize(250,250)
        self.text2 = QTextBrowser(self)
        self.text2.append("Changed")
        self.text2.resize(250,250)
        layout = QtWidgets.QVBoxLayout()
        self.btn = QPushButton("File Open")
        layout.addWidget(self.text1)
        layout.addWidget(self.text2)
        layout.addWidget(self.btn, alignment=Qt.AlignBottom)
        self.btn.clicked.connect(self.getfile)
        self.setLayout(layout)
        self.show()
    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
            'c:\\',"Text files (*.txt)")
        f = open(fname[0], 'r')
        while True:
            line = f.readline()
            if not line: break
            self.text1.append(line)
        f.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_Win = QtWidgets.QMainWindow()
    main_widget = MainWidget()
    main_Win.setCentralWidget(main_widget)
    main_Win.show()
    sys.exit( app.exec_() )