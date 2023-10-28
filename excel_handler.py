import pandas as pd

class ExcelHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.read_excel_file()

    def read_excel_file(self, sheet_name=None):
        if sheet_name is not None:
            self.data = pd.read_excel(self.file_path, sheet_name)
        else:
            self.data = pd.read_excel(self.file_path)
        return True

    def get_data_as_list(self, columns=None):
        data_list = []
        for _, row in self.data.iterrows():
            data_list.append(row.to_dict())
        return data_list
        
