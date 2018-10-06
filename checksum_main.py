from PyQt5.QtGui import *
import sys

 
# checksum_gui.py 모듈 import
import checksum_gui
 
# checksum_gui 모듈 안의 Ui_Dialog 클래스로부터 파생
class XDialog(QDialog, checksum_gui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)
 
app = QApplication(sys.argv)
dlg = XDialog()
dlg.show()
app.exec_()