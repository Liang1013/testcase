from selenium import webdriver
from page.toolconfig_page import ToolConfig
from page.login_page import LoginPage

import unittest,os

garderpath  = os.path.dirname(os.path.realpath(__file__)) #获取当前文件父级目录
garder = os.path.dirname(garderpath) #获取父目录的父目录
paths = "/data/chromedriver"

class CaseToolConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(garder+paths)
        cls.lognn = LoginPage(cls.driver)
        cls.tool = ToolConfig(cls.driver)
        cls.lognn.is_login()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_tool_A(self):
        '''工具--标题优化--编辑模块'''
        self.tool.is_tool_edit("免费工具")
        t = self.tool.is_tool_text()
        print("编辑结果：",t)
        self.assertTrue(t)

if __name__ == "__main__":
    unittest.main()
