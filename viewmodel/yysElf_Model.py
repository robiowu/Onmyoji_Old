# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from view.yysElf import Ui_MainWindow
from robiowu_ScriptEft import winhandle as winhandle
import resource.config as config
from model.yys import YysHelper
import threading
import time
import sys
# from robiowu_ScriptEft import mylog as mylog
# 全局注册快捷键有问题啊，现在还是不搞着先了
# from robiowu_ScriptEft.third_lib.pyhk3 import pyhk
hotkey = False


class YysMainViewModel:
    form_mainwindow = None
    _qMainWindow = None
    player1 = None
    player2 = None

    def __init__(self):
        """
        python Qt的逻辑是，Qt designer设计的ui转化的python文件中，仅包含一个类，类内两个函数
        这两个函数一个是用来传入一个QMainWindow实例
        """

        self._qMainWindow = QMainWindow()
        self.form_mainwindow = Ui_MainWindow()
        self.form_mainwindow.setupUi(self._qMainWindow)
        self.player1 = Player1(self.form_mainwindow)
        self.player2 = Player2(self.form_mainwindow)

    def show(self):
        """
        将窗口show出来
        :return:
        """
        self._qMainWindow.show()

    @staticmethod
    def get_game_hwnd_list():
        return winhandle.find_listSubHandle(pHandle=0, winClass=config.yys_list[0], winName=config.yys_list[1])


class Player:
    """
    基类主要用来展示一个Player模块中包含多少的控件与值
    以及定义几个checkbox的property属性
    """
    # region 成员变量
    _ui_instance = None

    _is_autoReady_checkbox = None
    _is_autoTryEvent_checkbox = None
    _is_autoYeYuanHuo_checkbox = None
    _is_captain_checkbox = None
    _is_catch_inout_checkbox = None
    _is_catch_gouyu_checkbox = None

    _hwd_comboBox = None
    _call_thumbnail_button = None
    _refresh_list_button = None

    _yys_helper = None
    _hotkey = None
    _hotkey_accept_eventId = None
    _hotkey_refuse_eventId = None
    _cyclethread = None
    _stop_thread = False

    _go_button_threadId = None
    _back_button_threadId = None
    _go_button_clicked = False
    _back_button_clicked = False
    # endregion

    def __init__(self, ui_MainWindow: Ui_MainWindow):
        """
        初始化Player板块，因为QT中每个控件的名称各不相同，并且貌似没有方便的找类函数
        因此抽象化Player模板以供函数复用
        由于这是父类，因此不做别的操作
        :param ui_MainWindow: <Ui_MainWindow> 指定要操作的界面ui控件布局的py文件
        """
        self._ui_instance = ui_MainWindow
        self._is_catch_gouyu_checkbox = self._ui_instance.is_autoRefuseGoldOffer
        return

    # region 各个checkbox的check值的getter和setter
    @property
    def is_autoGouyu(self):
        return self._is_catch_gouyu_checkbox.isChecked()
    @is_autoGouyu.setter
    def is_autoGouyu(self, value):
        self._is_catch_gouyu_checkbox.setChecked(value)

    @property
    def is_autoReady(self):
        return self._is_autoReady_checkbox.isChecked()
    @is_autoReady.setter
    def is_autoReady(self, value):
        self._is_autoReady_checkbox.setChecked(value)


    @property
    def is_autoTryEvent(self):
        return self._is_autoTryEvent_checkbox.isChecked()
    @is_autoTryEvent.setter
    def is_autoTryEvent(self, value):
        self._is_autoTryEvent_checkbox.setChecked(value)


    @property
    def is_autoYeYuanHuo(self):
        return self._is_autoYeYuanHuo_checkbox.isChecked()
    @is_autoYeYuanHuo.setter
    def is_autoYeYuanHuo(self, value):
        self._is_autoYeYuanHuo_checkbox.setChecked(value)


    @property
    def is_captain(self):
        return self._is_captain_checkbox.isChecked()
    @is_captain.setter
    def is_captain(self, value):
        self._is_captain_checkbox.setChecked(value)


    @property
    def is_catch_inout(self):
        return self._is_catch_inout_checkbox.isChecked()
    @is_catch_inout.setter
    def is_catch_inout(self, value):
        self._is_catch_inout_checkbox.setChecked(value)
    # endregion

    def _signal_connect_init(self):
        self._refresh_list_button.clicked.connect(self.refresh_hwnd_combox_list)
        self._hwd_comboBox.currentTextChanged.connect(self.change_hwnd_combox_list)
        self._ui_instance.go_button.clicked.connect(self.accept_invitation)
        self._ui_instance.back_button.clicked.connect(self.back_return)
        return

    # region 各个控件的新号对应的函数功能
    # 刷新按钮的clicked点击信号
    def refresh_hwnd_combox_list(self):
        self._hwd_comboBox.clear()
        temp = YysMainViewModel.get_game_hwnd_list()
        temp.sort()
        temp_str = [str(x) for x in temp]
        # 因为combox会默认展示第一个（即index = 0）的text，因此往最上面插入一个空字符串""用来停止线程
        temp_str.insert(0, "")
        print(temp_str)
        self._hwd_comboBox.addItems(temp_str)

    def change_hwnd_combox_list(self, currentText):
        # time.perf_counter()是墙上时间，即外部世界的时间
        # starttime = time.perf_counter()
        # starttime = time.process_time()
        # print(starttime)
        # 点击刷新的时候由于会先clear再加项目，因此中间会是 "旧hwnd"——""——"新hwnd" 的字符串变化
        # print(currentText)
        if self._cyclethread is not None:
            self._stop_thread = True
            try:
                self._cyclethread.join()
                self._cyclethread = None
                self._stop_thread = False
            except Exception as err:
                print("catch error in waiting thread stop :%s" % err)
        if self._yys_helper is not None:
            del self._yys_helper
            self._yys_helper = None
        if currentText == "":
            return
        try:
            self._yys_helper = YysHelper(int(currentText))
            # self._yys_helper.blink_border()
            self._yys_helper.findpic_helper.save_image("zzx.bmp")
            self._yys_helper.findpic_helper.save_image("zzx.jpg")
            print("change hwnd: %s" % currentText)
            self._cyclethread = threading.Thread(target=Player.cycle_working, args=(self,))
            self._cyclethread.start()
            # self._yys_helper = YysHelper(int(self._hwd_comboBox.currentText()))
        except Exception as e:
            print(e)

    def cycle_working(self):
        while True:
            if self.is_autoGouyu:
                self._yys_helper.catch_Gouyu_refuse_GoldOffer()
            self._yys_helper.win_click()
            self._yys_helper.lose_click()
            if self.is_captain:
                self._yys_helper.captain_start()
            if self.is_autoReady:
                self._yys_helper.battle_ready()
            if self.is_autoTryEvent:
                # 这里还没做
                self._yys_helper.battle_ready()
            if self.is_autoYeYuanHuo:
                self._yys_helper.battle_yeyuanhuo()
            if self._stop_thread:
                self._stop_thread = False
                break

    def accept_invitation(self):
        """
        响应接受邀请的逻辑
        :return:
        """
        if self._go_button_clicked:
            return
        self._go_button_clicked = True
        if self._go_button_threadId is not None:
            print("等待上一次 %s 结束" % sys._getframe().f_code.co_name)
            self._go_button_threadId.join()
            self._go_button_threadId = None
        if self.is_catch_inout and self._yys_helper is not None:
            self._go_button_threadId = threading.Thread(target=YysHelper.accept_invitation, args=(self._yys_helper,))
            self._go_button_threadId.start()
        self._go_button_clicked = False
        return

    def back_return(self):
        """
        响应返回退出的逻辑
        :return:
        """
        if self._back_button_clicked:
            return
        self._back_button_clicked = True
        if self._back_button_threadId is not None:
            print("等待上一次 %s 结束" % sys._getframe().f_code.co_name)
            self._back_button_threadId.join()
        if self.is_catch_inout and self._yys_helper is not None:
            self._back_button_threadId = threading.Thread(target=YysHelper.back_return, args=(self._yys_helper,))
            self._back_button_threadId.start()
        self._back_button_clicked = False
        return

    # endregion


class Player1(Player):
    def __init__(self, ui_MainWindow: Ui_MainWindow):
        """
        绑定一些控件关系
        :param ui_MainWindow:
        """
        Player.__init__(self, ui_MainWindow=ui_MainWindow)
        self._is_autoReady_checkbox = ui_MainWindow.is_autoReady_1
        self._is_autoTryEvent_checkbox = ui_MainWindow.is_autoTryEvent_1
        self._is_autoYeYuanHuo_checkbox = ui_MainWindow.is_autoYeYuanHuo_1
        self._is_captain_checkbox = ui_MainWindow.is_captain_1
        self._is_catch_inout_checkbox = ui_MainWindow.is_catch_inout_1

        self._hwd_comboBox = ui_MainWindow.hwd_comboBox_1
        self._call_thumbnail_button = ui_MainWindow.call_thumbnail_1
        self._refresh_list_button = ui_MainWindow.refresh_list_1

        # 绑定信号关系
        self._signal_connect_init()
        return


class Player2(Player):
    def __init__(self, ui_MainWindow: Ui_MainWindow):
        Player.__init__(self, ui_MainWindow=ui_MainWindow)
        self._is_autoReady_checkbox = ui_MainWindow.is_autoReady_2
        self._is_autoTryEvent_checkbox = ui_MainWindow.is_autoTryEvent_2
        self._is_autoYeYuanHuo_checkbox = ui_MainWindow.is_autoYeYuanHuo_2
        self._is_captain_checkbox = ui_MainWindow.is_captain_2
        self._is_catch_inout_checkbox = ui_MainWindow.is_catch_inout_2

        self._hwd_comboBox = ui_MainWindow.hwd_comboBox_2
        self._call_thumbnail_button = ui_MainWindow.call_thumbnail_2
        self._refresh_list_button = ui_MainWindow.refresh_list_2

        # 绑定信号关系
        self._signal_connect_init()
        return
