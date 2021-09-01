from common.ExcelUtil import ExcelUtil

import os

class Route():

    def is_route(self):
        garderpath = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件父级目录
        garder = os.path.dirname(garderpath)  # 获取父目录的父目录
        paths = "/data/chromedriver"

        return garder+paths

    def is_excel(self,file):
        # 获取excel表格数据
        propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 获取当前文件父级目录
        filepath = os.path.join(propath,"data",file)  # 获取文件路径
        data = ExcelUtil(filepath)

        return data.dict_data()