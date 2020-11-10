# 导入自动化测试报告包
from HTMLTestRunner import HTMLTestRunner
# 导入单元测试包
import unittest
# 导入测试用例包
from case import login

import os



# 实例化测试套件
suit = unittest.TestSuite()
# 将单元测试添加到测试套件里
suit.addTest(unittest.makeSuite(login.Login))
# 自动化测试报告生成的路径
filename = os.getcwd()+"/E.html"
# print(type(filename))
# 自动化测试报告编码格式
files = open(filename, "wb")
# print(type(files))

# 执行自动化测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=files,title="测试报告",description="测试用例")

# 执行用例
runner.run(suit)



