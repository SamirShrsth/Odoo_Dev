import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Python App")
        self.setGeometry(100, 100, 500, 500) # (startx, starty, width, height)
        self.setWindowIcon(QIcon("Python/GUI_PyQt5/icon.jpg"))
        
        label = QLabel("Hello World", self)
        label.setGeometry(150, 0, 200, 100) # (startx, starty, width, height)
        label.setStyleSheet("font-size: 30px; color: blue; background-color: yellow; border: 2px solid black;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
# img "icon.jpg"
        img = QLabel(self)  
        img.setPixmap(QPixmap("Python/GUI_PyQt5/icon.jpg"))
        img.setGeometry(100, 100, 300, 300) # (startx, starty, width, height)
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()