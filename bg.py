from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys

class GUI_main(object):
    def setupGUI(self, mw):
        mw.setObjectName("MainWindow")
        mw.resize(645, 370)
        self.centralwidget = QtWidgets.QWidget(mw)
        self.centralwidget.setObjectName("centralwidget")

        # define label for Gif
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1, 1, 1000, 1000))
        self.label.setMinimumSize(QtCore.QSize(645, 370))
        self.label.setMaximumSize(QtCore.QSize(645, 370))
        self.label.setObjectName("label")

        # embed label to main window
        mw.setCentralWidget(self.centralwidget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = GUI_main()
    ui.setupGUI(window)
    window.show()
    sys.exit(app.exec_())
