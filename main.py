import GUI.main_gui as gui
from PyQt5.QtWidgets import QMainWindow, QApplication
from sys import exit, argv

class Window(gui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.habits = {}
        self.spinBox_5.hide()
        self.label_14.hide()
        self.pushButton_2.hide()
        self.listWidget.itemClicked.connect(self.select_habit)
        self.create_habit.clicked.connect(self.create_new_habit)

    def select_habit(self):
        try:
            habit = self.habits[self.listWidget.currentItem().text()]
            if habit["current"] >= habit["high"]:
                print(habit["high"])
                level = "(high)"
            elif habit["current"] >= habit["normal"]:
                level = "(normal)"
            else:
                level = "(low)"
            self.current_habit.setText(self.listWidget.currentItem().text())
            self.current_amount.setText(str(habit["current"]) + level)
            self.listWidget_2.addItems(habit["all"])
            self.spinBox_5.show()
            self.label_14.show()
            self.pushButton_2.show()

        except Exception as error:
            print(error)
    def create_new_habit(self):
        self.habits.update({
            self.habit_name.text(): {
                "low": self.low_amout.value(), "normal": self.normal_amout.value(), "high": self.high_amout.value(),
                "current": self.start_amout.value(), "all": []}
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