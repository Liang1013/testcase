from selenium.webdriver.support.select import Select
from common.base import Base
from selenium import webdriver

import time

url = "http://crm.maimiaotech.com/auth/login/"
'''
ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
'''
class LoginPage(Base):

    #登陆定位
    username = ("id","id_username")
    password = ("id","id_password")
    submit = ("css selector"," .btn-large")

    #Select定位界面
    sel = ("name","group_id")
    btn = ("css selector",".btn-success")

    #登陆成功定位
    nick = ("css selector",".nick-name")

    def is_login(self,username,password,value):
        self.driver.get(url) #登陆url
        '''登陆界面'''
        self.sendkyes(self.username,username)
        self.sendkyes(self.password,password)
        self.click(self.submit)

        '''Select界面'''
        ele = self.findelement(self.sel)
        Select(ele).select_by_value(value)
        self.click(self.btn)

    def is_login_text(self,text="*********"):
        '''校验登陆结果'''
        return self.text_to_element(self.nick,text)

    def quit(self):
        '''关闭浏览器'''
        self.driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    loginn = LoginPage(driver)
    loginn.is_login("95")
    t = loginn.is_login_text()
    print("登陆结果：",t)
    time.sleep(3)
    driver.quit()