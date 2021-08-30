from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

'''
Example:
            from selenium.webdriver.support.ui import WebDriverWait \n
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())
'''
class Base():

    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.times = 10
        self.t = 0.5

    def findelement(self,locater):
        element = WebDriverWait(self.driver,self.times,self.t).until(lambda x: x.find_element(*locater))
        return element

    def sendkyes(self,locater,text):
        ele = self.findelement(locater)
        ele.send_keys(text)

    def click(self,locater):
        ele = self.findelement(locater)
        ele.click()

    def text_to_element(self,locator,text):
        try:
            element = WebDriverWait(self.driver,self.times,self.t).until(EC.text_to_be_present_in_element(locator,text))
            return element
        except:
            return False


    def select_by_value(self,locatre,value):
        '''通过value属性'''
        ele = self.findelement(locatre)
        Select(ele).select_by_value(value)
