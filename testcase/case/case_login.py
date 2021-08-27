from page.login_page import LoginPage
from selenium import webdriver
from common.ExcelUtil import ExcelUtil
import unittest,os,ddt

garderpath  = os.path.dirname(os.path.realpath(__file__)) #获取当前文件父级目录
garder = os.path.dirname(garderpath) #获取父目录的父目录
paths = "/data/chromedriver"

#获取excel表格数据
propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) #获取当前文件父级目录
filepath = os.path.join(propath,"data","excel.xlsx") #获取文件路径
data = ExcelUtil(filepath)
testdatas = data.dict_data()

@ddt.ddt
class CseLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(garder+paths)
        cls.loginn = LoginPage(cls.driver) #引用封装登陆模块

    @classmethod
    def tearDownClass(cls) -> None:
        cls.loginn.quit()

    @ddt.data(*testdatas)
    def test_login_A(self,data):
        '''登陆成测试用例'''
        self.loginn.is_login(data["usernam"],data["password"],data["value"])
        t = self.loginn.is_login_text()
        print("登陆结果：",t)
        self.assertTrue(t)

if __name__ == "__main__":
    unittest.main()