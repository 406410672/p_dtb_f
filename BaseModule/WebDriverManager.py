#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 17:57
# @Author  : HT
# @Site    :
# @File    : WebDriverManager.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

# -*- coding:utf-8 -*-
import sys,datetime,os
import time
# from Const import *
from selenium import webdriver

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))+'/PublicLibrary').replace('\\','/'))
from BaseModule import Const as C
# import Const as C


class WebDriverManager:
    def __init__(self):
        self._drivers = []

    def getFreeDriver(self):
        driver = None

        # 仅由这个控制可爬的账号数量
        if self._drivers.__len__() >= 5:
            for driver_info in self._drivers:
                if driver_info[C.DRIVER_STATUS] == C.PAUSE_STATUS:
                    driver = driver_info[C.DRIVER]
                    driver_info[C.DRIVER_STATUS] = C.RUNNING_STATUS_NO_COOKIES
                    driver_info[C.LAST_LOGIN_TIME] = datetime.datetime.now()
                    driver_info[C.LAST_REFRESH_TIME] = datetime.datetime.now()
                    break

        else:
            options = webdriver.ChromeOptions()
            options.add_argument(
                'User-Agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"')

            path = 'E:/chromedriver.exe'
            driver = webdriver.Chrome(path, chrome_options=options)
            driver_info = {
                C.LAST_LOGIN_TIME: datetime.datetime.now(),
                C.LAST_REFRESH_TIME: datetime.datetime.now(),
                C.DRIVER: driver,
                C.DRIVER_STATUS: C.RUNNING_STATUS_NO_COOKIES
            }
            self._drivers.append(driver_info)

        return driver

    def _cmd(self,cmd,*contents):
        # assert isinstance(cmd ,basestring),'Cmd must not be empty and type is str'
        if eval(cmd) in (C.G_D_S ,C.G_D_L_T ,C.G_D_R_T):
            assert contents.__len__() > 0,'contents must not be empty'
            driver = contents[0]
            for driver_info in self._drivers:
                if driver_info[C.DRIVER] == driver:
                    if eval(cmd) == C.G_D_S:
                        return driver_info[C.DRIVER_STATUS]
                    elif eval(cmd) == C.G_D_L_T:
                        return driver_info[C.LAST_LOGIN_TIME]
                    elif eval(cmd) == C.G_D_R_T:
                        return driver_info[C.LAST_REFRESH_TIME]
                else:
                    continue

        elif eval(cmd) in (C.I_W):
            w_d = [driver_info for driver_info in self._drivers if driver_info[C.DRIVER_STATUS] != C.PAUSE_STATUS]
            if len(w_d) > 0:
                return True
        else:
            if eval(cmd) == C.G_C:
                return len(self._drivers)
            elif eval(cmd) == C.G_DS:
                drivers = []
                for driver_info in self._drivers:
                    drivers.append(driver_info[C.DRIVER])
                return drivers
        # pass

    # return all drivers


    def setDriverStatus(self, driver, status):
        for driver_info in self._drivers:
            if driver_info[C.DRIVER] == driver:
                driver_info[C.DRIVER_STATUS] = status
                break

    def setDriverLastLoginTime(self, driver, t):

        for driver_info in self._drivers:
            if driver_info[C.DRIVER] == driver:
                driver_info[C.LAST_LOGIN_TIME] = t
                break

    def setDriverLastRefreshTime(self, driver, t):

        for driver_info in self._drivers:
            if driver_info[C.DRIVER] == driver:
                driver_info[C.LAST_REFRESH_TIME] = t
                break

    # ------------------------------------------------------------
    def getDrivers(self):
        d_l = self._cmd( "C.G_DS")
        return d_l

    def count(self):

        count = self._cmd("C.G_C")
        return count

    def getDriverStatus(self,driver):
        s = self._cmd('C.G_D_S', driver)
        return s

    def getDriverLastloginTime(self,driver):
        l_t = self._cmd('C.G_D_L_T' , driver)
        return l_t

    def getDriverLastRfreshTime(self,driver):
        r_t = self._cmd( 'C.G_D_R_T', driver)
        return r_t



    #deprecated
    # def is_Working(self):
    #     i_w = self._cmd( 'C.I_W')
    #     return i_w
    #new
    def existWebDriverWorking(self):
        i_w = self._cmd( 'C.I_W')
        return i_w

    def webFlush(self):
        for driver_info in self._drivers:
            driver = driver_info[C.DRIVER]
            driver.quit()
        del self._drivers[:]

    def webDriverQuit(self, driver):
        for driver_info in self._drivers:
            get_driver = driver_info[C.DRIVER]
            if get_driver == driver:
                break

        if driver_info is not None:
            del self._drivers[driver_info]
            print ('the device has exited ')

    def __repr__(self):
        return '{0._drivers!s}'.format(self)

    def __str__(self):
        return '{0._drivers!s}'.format(self)

if __name__ == '__main__':
    # pass
    d = WebDriverManager()

    for i in range(10):
        e = d.getFreeDriver()
        e.get('https://item.taobao.com/item.htm?id=523745044845')

        if i % 5 == 0:
            time.sleep(15)
        e.quit()
    # e.get('http://www.baidu.com')
    # time.sleep(5)
    # e.delete_all_cookies()
    # e.close
    # e.execute_script("document.getElementsByClassName('header-logout')[0].click()")
    # e.find_elements_by_class_name('header-logout')[0].click()
    # e.find_elements_by_class_name()[0].clear()