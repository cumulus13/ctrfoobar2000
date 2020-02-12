import sys
import os
try:
    from PyQt4 import QtGui, QtCore
    inherit = QtGui.QDialog
except ImportError:
    from PyQt5 import QtGui, QtCore
    inherit = QtGui.QWindow

class econsole():
    def __init__(self, parent=None):
        pass
        
    def getError(self, data):
        print "\n"
        print "\t" + data
        
class Dialog(inherit):
    def __init__(self, info, data, parent=None):
        try:
            QtGui.QWidget.__init__(self, parent)
        except:
            QtGui.QWindow.__init__(self, parent)
        self.info = info
        self.data = data
        
        if os.getcwd() == os.path.split(sys.argv[0])[0]:
            mypath = os.path.split(sys.argv[0])[0] + "/images/"
        else:
            if "c:" in os.getcwd():
                if "pyx" in os.getcwd():
                    #os.chdir("..\\")
                    mypath = os.getcwd() + '/images/' 
                else:
                    mypath = r'c:/pyx/images/' 
            else:
                mypath = mypath = r'c:/pyx/images/' 

        #print "mypath = ", mypath                #for test only
        #print "os.getcwd() = ", os.getcwd()      #for test only
        #print "sys.argv[0] = ", sys.argv[0]      #for test only
            
        self.setGeometry(300, 300, 550, 350)
        try:
            self.setFixedSize(500, 350)
        except:
            self.setMaximumSize(QtGui.QSize(500, 350))
        self.setWindowTitle(str(self.info))
        self.setWindowIcon(QtGui.QIcon(mypath + str(self.info) + '2.png'))

        self.btOK = QtGui.QPushButton('Close', self)
        self.btOK.setFocusPolicy(QtCore.Qt.NoFocus)

        self.btOK.move(225, 310)
        self.connect(self.btOK, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))
        self.setFocus()
        
        self.img_label = QtGui.QLabel(self)
        self.img_label.setMinimumSize(50, 50)
        self.img_label.setGeometry(5, 5, 50, 50)
        self.img_info = QtGui.QImage(mypath + str(self.info) + '2.png')
        self.img_label.setPixmap(QtGui.QPixmap.fromImage(self.img_info))

        self.label = QtGui.QTextEdit(self)
        self.label.setGeometry(70, 10, 420, 280)
        self.label.setFont(QtGui.QFont('Arial',15, 500))
        self.label.setText(self.data)
        self.label.setBackgroundRole(QtGui.QPalette.Dark)
        self.label.setAutoFillBackground(True)
        self.label.setReadOnly(True)
        #self.label.setHtml(text)
        
        self.setModal(True)
        
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

def main(info, data):
    try:
        app = QtGui.QApplication(sys.argv)
    except:
        from PyQt5.QtWidgets import QApplication
        app = QApplication(sys.argv)
    icon = Dialog(info,data)
    icon.show()
    app.exec_()

if __name__ == '__main__':
    main('error', 'test error data')
#main('error','just test')

