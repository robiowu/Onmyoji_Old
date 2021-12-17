# -*- coding: utf-8 -*-
import resource.config as config
from robiowu_ScriptEft import *
import time


class YysHelper(gamecase.MyGameCase, winhandle.Window):
    def __init__(self, hwnd):
        gamecase.MyGameCase.__init__(self, hwnd, "阴阳师")
        winhandle.Window.__init__(self, hwnd)

    def win_click(self):
        """
        找图判断是否已经战斗胜利进入结算界面
        :return:
        """
        self.findpic_helper.get_window_image()
        for sub_image in config.battleWin.win:
            intx, inty, threshold = self.findpic_helper.find_sub_pic(sub_image_path=sub_image, threshold=0.9)
            if intx >= 0 and inty >= 0:
                self.log.info("找到 战斗胜利 标志位")
                self.log.info("标志图：%s" % sub_image)
                self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (intx, inty, threshold))
                self.randomClick(point_x=config.battleWin.x_click_win, point_y=config.battleWin.y_click_win,
                                 random_x=config.battleWin.random_x, random_y=config.battleWin.random_y)
                break
        return

    def lose_click(self):
        self.findpic_helper.get_window_image()
        for sub_image in config.battleLose.lose:
            intx, inty, threshold = self.findpic_helper.find_sub_pic(sub_image_path=sub_image, threshold=0.9)
            if intx >= 0 and inty >= 0:
                self.log.info("找到 失败 窗口")
                self.log.info("标志图：%s" % sub_image)
                self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (intx, inty, threshold))
                self.randomClick(point_x=intx, point_y=inty,
                                 random_x=config.battleLose.random_x, random_y=config.battleLose.random_y)
                break
        return

    def captain_start(self):
        """
        用来给队长或者活动的时候，指定看到“开始战斗”就点击
        :return:
        """
        self.findpic_helper.get_window_image()
        for sub_image in config.battleStart.start:
            intx, inty, threshold = self.findpic_helper.find_sub_pic(sub_image_path=sub_image, threshold=0.9)
            if intx >= 0 and inty >= 0:
                self.log.info("找到 开始战斗 标志位")
                self.log.info("标志图：%s" % sub_image)
                self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (intx, inty, threshold))
                self.randomClick(point_x=intx, point_y=inty,
                                 random_x=config.battleStart.random_x, random_y=config.battleStart.random_y)
                break
        return

    def battle_ready(self):
        self.findpic_helper.get_window_image()
        for sub_image in config.battleStart.ready:
            intx, inty, threshold = self.findpic_helper.find_sub_pic(sub_image_path=sub_image, threshold=0.9)
            if intx >= 0 and inty >= 0:
                self.log.info("找到 开始战斗 标志位")
                self.log.info("标志图：%s" % sub_image)
                self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (intx, inty, threshold))
                self.randomClick(point_x=intx, point_y=inty,
                                 random_x=config.battleStart.random_x, random_y=config.battleStart.random_y)
                break
        return

    def battle_yeyuanhuo(self):
        self.findpic_helper.get_window_image()
        for sub_image in config.battleStartYeyuanhuo.yeyuanhuo:
            intx, inty, threshold = self.findpic_helper.find_sub_pic(sub_image_path=sub_image, threshold=0.9)
            if intx >= 0 and inty >= 0:
                self.log.info("找到 业原火 标志位")
                self.log.info("标志图：%s" % sub_image)
                self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (intx, inty, threshold))
                self.randomClick(point_x=config.battleStartYeyuanhuo.x_click_yeyuanhuo,
                                 point_y=config.battleStartYeyuanhuo.y_click_yeyuanhuo,
                                 random_x=config.battleStartYeyuanhuo.random_x,
                                 random_y=config.battleStartYeyuanhuo.random_y)
                break
        return

    def catch_Gouyu_refuse_GoldOffer(self):
        self.findpic_helper.get_window_image()
        sub_image = config.refuseGoldOffer.refuse
        # print(sub_image)
        refuse_x, refuse_y, threshold = self.findpic_helper.find_sub_pic(sub_image_path=sub_image, threshold=0.9)
        if refuse_x >= 0 and refuse_y >= 0:
            self.log.info("找到 悬赏拒绝 标志位")
            self.log.info("标志图：%s" % sub_image)
            self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (refuse_x, refuse_y, threshold))

            check_times = config.refuseGoldOffer.check_times
            while check_times > 0:
                # 判断是不是勾协
                self.findpic_helper.get_window_image()
                sub_image = config.refuseGoldOffer.gouyu
                intx, inty, threshold = self.findpic_helper.find_sub_pic(sub_image_path=sub_image, threshold=0.9)
                if intx >= 0 and inty >= 0:
                    self.log.info("找到 勾协勾玉 标志位")
                    self.log.info("标志图：%s" % sub_image)
                    self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (intx, inty, threshold))

                    # 判断是勾协，于是开始找能不能找到接受勾协的button
                    sub_image = config.refuseGoldOffer.accept
                    intx, inty, threshold = self.findpic_helper.find_sub_pic(sub_image_path=sub_image, threshold=0.9)
                    if intx >= 0 and inty >= 0:
                        self.log.info("找到 勾协勾玉 标志位")
                        self.log.info("标志图：%s" % sub_image)
                        self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (intx, inty, threshold))
                        self.randomClick(point_x=intx, point_y=inty,
                                         random_x=config.refuseGoldOffer.random_x,
                                         random_y=config.refuseGoldOffer.random_y)
                        # 找到了就不用再check了，退出循环
                        # check_times = 0
                        break
                else:
                    check_times = check_times - 1
                    self.log.info("判断不是勾协，剩余判断次数：%d 次" % check_times)
                    if check_times <= 0:
                        self.randomClick(point_x=refuse_x, point_y=refuse_y,
                                         random_x=config.refuseGoldOffer.random_x,
                                         random_y=config.refuseGoldOffer.random_y)
        return

    def accept_invitation(self):
        self.findpic_helper.get_window_image()
        sub_image = config.invitation.invitation
        intx, inty, threshold = self.findpic_helper.find_sub_pic(sub_image_path=sub_image, threshold=0.9)
        if intx >= 0 and inty >= 0:
            self.log.info("找到 邀请勾叉框")
            self.log.info("标志图：%s" % sub_image)
            self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (intx, inty, threshold))
            self.randomClick(point_x=config.invitation.x_click_Invitation,
                             point_y=config.invitation.y_click_Invitation,
                             random_x=config.invitation.random_x,
                             random_y=config.invitation.random_y)
        return

    def back_return(self):
        def findback(_sub_image):
            _intx, _inty, _threshold = self.findpic_helper.find_sub_pic(sub_image_path=_sub_image, threshold=0.9)
            if _intx >= 0 and _inty >= 0:
                self.log.info("找到 返回键")
                self.log.info("标志图：%s" % _sub_image)
                self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (_intx, _inty, _threshold))
                self.randomClick(point_x=_intx, point_y=_inty,
                                 random_x=config.back.random_x, random_y=config.back.random_y)
                return True
            else:
                return False

        def click_return():
            # 找到弹出的返回窗口的确认键
            confirm_check_time = config.back.confirm_check_times
            sub_image = config.back.confirm

            while confirm_check_time > 0:
                self.findpic_helper.get_window_image()
                intx, inty, threshold = self.findpic_helper.find_sub_pic(sub_image_path=sub_image, threshold=0.9)
                if intx >= 0 and inty >= 0:
                    self.log.info("找到 返回窗口确认窗")
                    self.log.info("标志图：%s" % sub_image)
                    self.log.info("坐标值: ( %d, %d)\t匹配值: %f" % (intx, inty, threshold))
                    self.randomClick(point_x=intx, point_y=inty,
                                     random_x=config.back.random_x, random_y=config.back.random_y)
                    # reset confirm_check_time，保证说这几次的checktime都是用来确定已经没有返回的button了，因为响应点击是要时间的
                    confirm_check_time = config.back.confirm_check_times
                else:
                    confirm_check_time = confirm_check_time - 1

        for _ in range(0, config.back.func_loop_times):
            # self.findpic_helper.get_window_image()
            # 找到在战斗界面中的返回键
            back_check_time = config.back.back_check_times
            while back_check_time > 0:
                self.findpic_helper.get_window_image()
                if findback(config.back.story) or findback(config.back.boundary):
                    # reset back_check_time的值，保证说这几次的checktime都是用来确定已经没有返回的button了，因为响应点击是要时间的
                    back_check_time = config.back.back_check_times
                    click_return()
                else:
                    back_check_time = back_check_time - 1

    def blink_border(self):
        self.highLight()
        # time.sleep(1)
        self.noHighLight()
        return


if __name__ == "__main__":
    print(config.resource_dir)
