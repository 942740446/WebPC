# 导入单元测试包
import unittest
# 导入util包
from util import startfirefoxutil
from util import urlutil

import traceback
# 下拉框
from selenium.webdriver.support.select import Select

# 鼠标包
from selenium.webdriver.common.action_chains import ActionChains


class Login(unittest.TestCase):

    @classmethod
    # 所有用例执行之前
    def setUpClass(self):

        self.browe = startfirefoxutil.FireFox()
        self.URL = urlutil.URL()
        pass

    def setUp(self):
        self.browe.Start_FireFox()
        self.browe.Time_Sleep(2)

        pass

    def tearDown(self):
        self.browe.Close_FireFox()
        pass

    # 测试用例
    def test_a(self):

        self.browe.seting()
        self.browe.FindClass('header__header-right--1E9ZL')
        self.browe.FindClass('header__sign-in--1X5pu')
        x = self.browe.FindClasss('header__list-sign-in--30tl9')[0].text
        self.assertNotEqual(x, '登陆')
        print('登陆成功')

        pass
