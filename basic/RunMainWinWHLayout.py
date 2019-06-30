import sys
import Horizon_Vert
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    # 实例化对象
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWindow = QMainWindow()

    # 导入PyUIc 生成的类
    ui = Horizon_Vert.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())