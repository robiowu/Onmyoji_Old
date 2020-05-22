# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from viewmodel.yysElf_Model import YysMainViewModel

# class test(Ui_MainWindow, QtWidgets):

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) > 1:
        print(sys.argv)
    # 每个GUI程序有且仅有一个QApplication的实例，传入参数为list类型
    app = QApplication(sys.argv)

    yysWindowsInstance = YysMainViewModel()
    print(yysWindowsInstance.get_game_hwnd_list())
    yysWindowsInstance.show()

    # 运行主循环
    sys.exit(app.exec_())
