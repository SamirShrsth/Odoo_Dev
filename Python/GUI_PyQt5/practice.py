import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Application")
        self.setGeometry(800, 200, 500, 500)
        self.setWindowIcon(QIcon("Python\\GUI_PyQt5\\icon.jpg"))
        
        label = QLabel("Hello", self)
        label.setGeometry(100, 0, 100, 50)
        label.setStyleSheet("color: black; font-size: 30px;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        img = QLabel(self)
        img.setPixmap(QPixmap("Python/GUI_PyQt5/icon.jpg"))
        img.setGeometry(100, 50, 300, 300)
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()