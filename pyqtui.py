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
from PyQt5.QtGui import QTextCursor
import os
import Integration

fileflag =0
class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent =None):
        super().__init__(parent)
        self.setMinimumSize(QSize(500, 500))    
        self.setWindowTitle("PyQt5 Textarea example")
        self.text1 = QTextBrowser(self)
        #Set original text to original text box
        self.text1.append("Original")
        self.text1.resize(250,250)
        self.text2 = QTextBrowser(self)
        #Set changed text to changed text box
        self.text2.append("Changed")
        self.text2.resize(250,250)
        layout = QtWidgets.QVBoxLayout()
        #Set File reading box
        self.btn = QPushButton("File Open")
        layout.addWidget(self.text1)
        layout.addWidget(self.text2)
        layout.addWidget(self.btn, alignment=Qt.AlignBottom)
        self.btn.clicked.connect(self.getfile)
        self.setLayout(layout)
        self.show()
    def getfile(self):
        global fileflag
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
            'C:\\',"Text files (*.txt)")
        #exception for error file name(null char)
        if fname[0] == '':
            self.text1.setText("there is no such file, research the file. If you do not find, this program ends")
            fileflag+=1
            if fileflag <3 :
                self.getfile()
            else:
                sys.exit(1)
        f = open(fname[0], 'r', encoding='UTF8')
        fname2 = fname[0].replace('.txt', 'fixed.txt')
        self.text1.setText("Original")
        self.text2.setText("Changed")
        collected_words2 =[]
        #read text file and add it to textboxes
        while True:
            line = f.readline()
            if not line: break
            collected_words2.append(line)
        self.text1.append(''.join(x for x in collected_words2))
        f.close()
        # changed word list
        if not Integration.fixingResume(fname[0], fname2):
            self.text2.append("error ocurred, please try again")
            return
        word_list = Integration.getFixedList()
        collected_words = []
        # open txt if ther is fixed file
        if os.path.isfile(fname2):
            f2 = open(fname2, 'r', encoding='UTF8')
        #if not, just open original file and show that error has occured
        else :
            self.text2.setText("error occured, there is no fixed file")
            f2 = open(fname[0], 'r', encoding='UTF8')
        #if some error occured, just show the error message
        if not word_list :
            self.text2.append("error ocurred, please try again")
        #if nothing changes, print just txt file
        elif word_list[0] =="SUCCESS":
            while True:
                line = f2.readline()
                if not line: break
                collected_words.append(line)
            self.text2.append(''.join(x for x in collected_words))
            f2.close()
        # if nothing happend, show the changed words
        else:
            self.text2.moveCursor(QTextCursor.End)
            self.text2.setTextColor(QtGui.QColor(0,0,0))
            self.text2.insertPlainText('\n')
            while True:
                line = f2.readline()
                if not line: break
                line_split = line.split()
                # split by words, and check them if they are changed
                for a in line_split:
                    iflag = 0
                    for b in word_list:
                        if b in a:
                            if collected_words:
                                self.text2.moveCursor(QTextCursor.End)
                                self.text2.setTextColor(QtGui.QColor(0,0,0))
                                self.text2.insertPlainText(''.join(x for x in collected_words))
                            collected_words = []
                            iflag +=1
                            #if changed, change the color
                            self.text2.moveCursor(QTextCursor.End)
                            self.text2.setTextColor(QtGui.QColor(255,0,0))
                            self.text2.insertPlainText(a)
                    if iflag ==0:
                        collected_words.append(a)
                    collected_words.append(' ')
                self.text2.moveCursor(QTextCursor.End)
                self.text2.setTextColor(QtGui.QColor(0,0,0))
                self.text2.insertPlainText(''.join(x for x in collected_words))
                self.text2.insertPlainText('\n')
                collected_words = []
            f2.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_Win = QtWidgets.QMainWindow()
    main_widget = MainWidget()
    main_Win.setCentralWidget(main_widget)
    main_Win.show()
    sys.exit( app.exec_() )