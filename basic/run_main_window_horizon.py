import sys
import mainlayout
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    # 实例化对象
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWindow = QMainWindow()

    ui = mainlayout.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())