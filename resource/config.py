"""
因为findpic不支持中文路径，会报错：
error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'
因此要全部切换成英文
"""
# -*- coding: utf-8 -*-
import os

yys_list = ["Win32Window0", "阴阳师-网易游戏"]
resource_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "./featuremap"))


class BattleWin:
    _sub_dir = os.path.abspath(os.path.join(resource_dir, "BattleWin"))
    _win1 = "roll.bmp"   # 战斗结束之轮子
    _win2 = "bowl.bmp"    # 战斗结束之碗
    _win3 = "bottom.bmp"    # 战斗结束之点击任意键
    _win4 = "gouyu.bmp"   # 战斗结束之勾玉
    x_click_win = 0
    y_click_win = 200
    random_x = 180
    random_y = 200

    @property
    def win(self):
        """
        :return: <list> 战斗结束结算画面的标志性特征图的路径list
        """
        win_imag_list = list()
        win_imag_list.append(os.path.join(self._sub_dir, self._win1))
        win_imag_list.append(os.path.join(self._sub_dir, self._win2))
        win_imag_list.append(os.path.join(self._sub_dir, self._win3))
        win_imag_list.append(os.path.join(self._sub_dir, self._win4))
        return win_imag_list


class BattleLose:
    _sub_dir = os.path.abspath(os.path.join(resource_dir, "BattleLose"))
    _lose1 = "lose.bmp"    # 失败
    random_x = 150
    random_y = 25

    @property
    def lose(self):
        _list = list()
        _list.append(os.path.join(self._sub_dir, self._lose1))
        return _list


class BattleStart:
    _sub_dir = os.path.abspath(os.path.join(resource_dir, "BattleStart"))
    _start = "start.bmp"    # 开始战斗
    _ready = "ready.bmp"    # 准备圆盘
    random_x = 150
    random_y = 25

    @property
    def start(self):
        _list = list()
        _list.append(os.path.join(self._sub_dir, self._start))
        return _list

    @property
    def ready(self):
        _list = list()
        _list.append(os.path.join(self._sub_dir, self._ready))
        return _list


class BattleStartYeyuanhuo:
    _sub_dir = os.path.abspath(os.path.join(resource_dir, "BattleStart"))
    _yeyuanhuo = "yeyuanhuo.bmp"    # 业原火界面
    x_click_yeyuanhuo = 1000
    y_click_yeyuanhuo = 540
    random_x = 150
    random_y = 25

    @property
    def yeyuanhuo(self):
        _list = list()
        _list.append(os.path.join(self._sub_dir, self._yeyuanhuo))
        return _list


class RefuseGoldOffer:
    _sub_dir = os.path.abspath(os.path.join(resource_dir, "RefuseGoldOffer"))
    _refuse_button = "refuse.bmp"    # 悬赏拒绝
    _accept_button = "accept.bmp"    # 悬赏接受
    _gouyu = "gouyu.bmp"   # 勾协
    # 找到悬赏图后，一次轮回中尝试
    check_times = 3
    random_x = 150
    random_y = 25

    def __init__(self):
        self._refuse_button = os.path.join(self._sub_dir, self._refuse_button)
        self._accept_button = os.path.join(self._sub_dir, self._accept_button)
        self._gouyu = os.path.join(self._sub_dir, self._gouyu)

    @property
    def refuse(self):
        # _list = list()
        # _list.append(os.path.join(self._sub_dir, self._refuse_button))
        return self._refuse_button

    @property
    def accept(self):
        # _list = list()
        # _list.append(os.path.join(self._sub_dir, self._accept_button))
        return self._accept_button

    @property
    def gouyu(self):
        # _list = list()
        # _list.append(os.path.join(self._sub_dir, self._gouyu))
        return self._gouyu


class Invitation:
    _sub_dir = os.path.abspath(os.path.join(resource_dir, "Invitation"))
    _invitation = "invitation.bmp"    # 邀请叉勾
    x_click_Invitation = 120
    y_click_Invitation = 40
    random_x = 25
    random_y = 25
    invite_accept_hotkey = ['Ctrl', 'F1']
    invite_refuse_hotkey = ['Ctrl', 'F2']

    def __init__(self):
        self._invitation = os.path.join(self._sub_dir, self._invitation)

    @property
    def invitation(self):
        # _list = list()
        # _list.append(os.path.join(self._sub_dir, self._invitation))
        return self._invitation


class Back:
    _sub_dir = os.path.abspath(os.path.join(resource_dir, "Back"))
    _story = "storyback.bmp"    # 探索返回
    _boundary = "boundaryback.bmp"    # 结界返回
    _confirm = "confirm.bmp"    # 确认
    random_x = 25
    random_y = 25
    func_loop_times = 3
    back_check_times = 3
    confirm_check_times = 3

    def __init__(self):
        self._story = os.path.join(self._sub_dir, self._story)
        self._boundary = os.path.join(self._sub_dir, self._boundary)
        self._confirm = os.path.join(self._sub_dir, self._confirm)

    @property
    def story(self):
        # _list = list()
        # _list.append(os.path.join(self._sub_dir, self._story))
        return self._story

    @property
    def boundary(self):
        # _list = list()
        # _list.append(os.path.join(self._sub_dir, self._boundary))
        return self._boundary

    @property
    def confirm(self):
        # _list = list()
        # _list.append(os.path.join(self._sub_dir, self._confirm))
        return self._confirm


battleWin = BattleWin()
battleLose = BattleLose()
battleStart = BattleStart()
battleStartYeyuanhuo = BattleStartYeyuanhuo()
refuseGoldOffer = RefuseGoldOffer()
invitation = Invitation()
back = Back()

