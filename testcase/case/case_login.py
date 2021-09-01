from page.login_page import LoginPage
from selenium import webdriver
from common.route import Route
import unittest,ddt

#获取excel表格数据
excel = Route().is_excel("excel.xlsx")

@ddt.ddt
class CseLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.rou = Route().is_route()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.loginn = LoginPage(cls.driver) #引用封装登陆模块

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @ddt.data(*excel)
    def test_login_A(self,data):
        '''登陆成测试用例'''
        self.loginn.is_login(data["usernam"],data["password"],data["value"])
        t = self.loginn.is_login_text(data["text"])
        print("登陆结果：",t)
        self.assertTrue(t)

if __name__ == "__main__":
    unittest.main()