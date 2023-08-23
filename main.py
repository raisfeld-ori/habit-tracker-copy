import GUI.main_gui as gui
from PyQt5.QtWidgets import QMainWindow, QApplication
from sys import exit, argv

class Window(gui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

if __name__ == "__main__":
    try:
        app = QApplication(argv)
        window = Window()
        window.show()
        exit(app.exec())
    except Exception as error:
        print(error)