import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QToolTip,QLabel,QLineEdit,QPushButton)
from PyQt5.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("My Firts Title")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("joker.jpg"))
        self.setToolTip("My Tooltip")
        self.initUI()

    def initUI(self):
        self.lbl_name = QLabel(self)
        self.lbl_name.setText('Adınız :')
        self.lbl_name.move(50, 30)
        
        self.name = QLineEdit(self)
        self.name.move(150, 30)
        self.name.resize(100, 35)


        self.lbl_surnam = QLabel(self)
        self.lbl_surnam.setText('Soyadınız :')
        self.lbl_surnam.move(50, 80)
        
        self.surname = QLineEdit(self)
        self.surname.move(150, 70)
        self.surname.resize(100, 35)

        self.lbl_result = QLabel(self)
        self.lbl_result.resize(300, 50)
        self.lbl_result.move(150,150)
        
        self.btn = QPushButton(self)    
        self.btn.move(150, 110)
        self.btn.setText("Kaydet")
        self.btn.clicked.connect(self.clicked)
    
    def clicked(self):
        self.lbl_result.setText(f"Welcome {self.name.text()} {self.surname.text()}")
        
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()