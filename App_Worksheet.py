import openpyxl

class App_Worksheet:
    WB_NAME = 'My Name Application.xlsx'
    WB = openpyxl.load_workbook(WB_NAME)



    def __init__(self, applicant_name):
        self.name = sheet_name