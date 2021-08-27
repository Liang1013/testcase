import xlrd,os

garderpath = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件父级目录
garder = os.path.dirname(garderpath)  # 获取父目录的父目录
paths = "/data/excel.xlsx"
class ExcelUtil():
    def  __init__(self,excePath,sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excePath)
        self.table = self.data.sheet_by_name(sheetName)
        #获取第一行做个key值
        self.keys = self.table.row_values(0)
        #获取总行数
        self.rowNum = self.table.nrows
        #获取纵列数
        self.colNum = self.table.ncols
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于等于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                #从第二行取对应的values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r
if __name__ == "__main__":
    print(garder+paths)

    data = ExcelUtil(garder+paths)
    print(data.dict_data())