from common import HTMLTestRunner
from common.send_email import send_email
import unittest,time,os

garderpath  = os.path.dirname(os.path.realpath(__file__)) #获取当前文件父级目录
garder = os.path.dirname(garderpath) #获取父目录的父目录


casepath = "/case"   # 获取用例路径
repertpath = "/report/" #获取测试报报告路径

def create_report():

    discover = unittest.defaultTestLoader.discover(start_dir=garder+casepath, pattern="case*.py")

    # 获取写入报告路
    now = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
    # 获取测试报报告路径
    reportpath = garder+repertpath+ "%s.html"%now
    #reportpath = garder + repertpath + "report.html"
    # 已二进制写入路径下
    fg = open(reportpath, "wb")

    reunner = HTMLTestRunner.HTMLTestRunner(stream=fg,
                                            title="CRM登陆用例",
                                            description="用户名与密码登陆")
    reunner.run(discover)

    #执行发送邮件
    send_email(reportpath) #reportpath 测试报告地址