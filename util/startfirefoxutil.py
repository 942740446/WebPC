# 导入打开浏览器的包
from selenium import webdriver
# 导入时间包
import time
# 倒入redis
import redis

class FireFox(object):

    # 打开浏览器的方法
    def Start_FireFox(self):

        self.driver = webdriver.Firefox()

        self.driver.maximize_window()

        self.driver.get("https://beta-www.iwanmen.com")

        # 设置休眠时间

        pass

    # 关闭浏览器的方法
    def Close_FireFox(self):
        self.driver.quit()
        pass

    #  静态等待
    def Time_Sleep(self, number):
        time.sleep(number)
        pass

        # 隐式休眠
    def Implicitly_Sleep(self, number):
        self.driver.implicitly_wait(number)

        pass

        #登陆
    def seting(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[3]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[15]/div[2]/div/div[1]/div[2]/div[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[15]/div[2]/div/div[1]/button").click()
        print('选择分类完成')
        time.sleep(3)
        self.driver.find_element_by_class_name('header__header-right--1E9ZL')
        self.driver.find_element_by_class_name('header__sign-in--1X5pu')
        self.driver.find_elements_by_class_name('header__list-sign-in--30tl9')[0].click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div'
                                          '/form/div[1]/div/div/div/input').send_keys('m@qq.com')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]'
                                          '/div[2]/div/form/div[2]/div/div/input').send_keys('1111aaaa')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/form/div[4]/button').click()
        time.sleep(2)
        pass

    # 查找控件
    def FindId(self, id):

        return self.driver.find_element_by_id(id)

        pass

    def FindName(self, name):

        return self.driver.find_element_by_name(name)

        pass

    def FindClass(self, clas):

        return self.driver.find_element_by_class_name(clas)

        pass

    def FindXpath(self, xpath):

        return self.driver.find_element_by_xpath(xpath)

        pass

    def FindLink(self, link):

        return self.driver.find_element_by_link_text(link)

        pass

    def FindPartial(self, partial):

        return self.driver.find_element_by_partial_link_text(partial)

        pass

    def FindCss(self, css):

        return self.driver.find_element_by_css_selector(css)

        pass

    # 查找控件
    def FindTag(self, tag):

        return self.driver.find_element_by_tag_name(tag)

        pass

    # 加上s  一组空间

    def FindIds(self,ID):

        return self.driver.find_elements_by_id(ID)

        pass

    def FindNames(self, name):

        return self.driver.find_elements_by_name(name)

        pass

    def FindClasss(self, clas):

        return self.driver.find_elements_by_class_name(clas)

        pass

    def FindXpaths(self, xpath):

        return self.driver.find_elements_by_xpath(xpath)

        pass

    def FindLinks(self, link):

        return self.driver.find_elements_by_partial_link_text(link)

        pass

    def FindPartials(self, partial):

        return self.driver.find_elements_by_partial_link_text(partial)

        pass

    def FindCsss(self, css):

        return self.driver.find_elements_by_css_selector(css)

        pass

    # 查找控件
    def FindTags(self, tag):

        return self.driver.find_elements_by_tag_name(tag)

        pass

    # 定位页面
    def location_window(self):
        # 当前页面
        current_window = self.driver.current_window_handle
        all_window = self.driver.window_handles
        for window in all_window:
            if window != current_window:
                self.driver.switch_to_window(window)
        pass

    def getRedisIphoneInfo(self, timeout=30, iphone0='12345678901'):
        r = redis.Redis(host="door.wanmen.co", port=32002, decode_responses=True)
        n = 0
        key = ("%s_phone" % (iphone0))
        while n < timeout:
            value = r.get(key)
            if value:
                return value
            n = n + 1
            if n == timeout:
                return ""
        pass













