from common.base import Base
from page.login_page import LoginPage
from selenium import webdriver

import time

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

class ToolConfig(Base):

    '''工具界面'''
    tool = ("css selector",".nav-tabs>:nth-child(17)>a")
    tool_param = ("id","tool_Param")
    title = ("css selector",".nav-container>div:nth-child(4)")
    operation = ("css selector",".tool-param-table-content>div:nth-child(3)>span:nth-child(7)")

    '''编辑弹窗'''
    toolfreetype = ("id","toolFreeType")
    btn = ("css selector",".btn-primary")
    btn_primary = ("css selector",".mm-popup>div>div:nth-child(3)>button")

    tool_text = ("css selector",".tool-param-table-content>div:nth-child(3)>span:nth-child(5)")

    def is_tool_edit(self,text):

        '''进入标题优化设置界面'''
        time.sleep(5)
        self.move_to_element(self.tool) #浮窗按钮
        self.click(self.tool_param)
        self.click(self.title)
        time.sleep(3)
        self.click(self.operation)

        '''编辑工具'''
        self.select_by_text(self.toolfreetype,text) #Select界面
        self.click(self.btn)
        time.sleep(1)
        self.click(self.btn_primary)

    def is_tool_text(self,text="不消耗积分"):
        return self.text_to_element(self.tool_text,text)


if __name__ == "__main__":

    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    loginn  = LoginPage(driver)
    tool = ToolConfig(driver)

    loginn.is_login()

    tool.is_tool_edit("免费工具")
    t = tool.is_tool_text()
    print(t)

    time.sleep(10)
    driver.quit()


