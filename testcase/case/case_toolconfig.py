from selenium import webdriver
from page.toolconfig_page import ToolConfig
from page.login_page import LoginPage
from common.route import Route

import unittest,ddt

execl = Route().is_excel("tool.xlsx")

@ddt.ddt
class CaseToolConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.rou = Route().is_route()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.lognn = LoginPage(cls.driver)
        cls.tool = ToolConfig(cls.driver)
        cls.lognn.is_login()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @ddt.data(*execl)
    def test_tool_A(self,data):
        '''工具--标题优化--编辑模块'''
        self.tool.is_tool_edit(data["text"])
        t = self.tool.is_tool_text()
        print("编辑结果：",t)
        self.assertTrue(t)

if __name__ == "__main__":
    unittest.main()
