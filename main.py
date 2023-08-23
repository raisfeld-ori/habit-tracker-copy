import GUI.main_gui as gui
from PyQt5.QtWidgets import QMainWindow, QApplication
from sys import exit, argv

class Window(gui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.habits = {}
        self.create_habit.clicked.connect(self.create_new_habit)

    def create_new_habit(self):
        self.habits.update({
            self.habit_name.text(): {
                "low": self.low_amout.text(), "normal": self.normal_amout.text(), "high": self.high_amout.text(),
                "current": self.start_amout.text(), "all": []}
            })
        self.listWidget.addItem(self.habit_name.text())
        self.habit_name.clear()
        self.low_amout.clear()
        self.normal_amout.clear()
        self.high_amout.clear()
        self.start_amout.clear()

if __name__ == "__main__":
    try:
        app = QApplication(argv)
        window = Window()
        window.show()
        exit(app.exec())
    except Exception as error:
        print(error)