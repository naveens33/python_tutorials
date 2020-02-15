from pathlib import Path
import xlrd


def get_data(filename, sheet_name):
    data_list = []
    wb = xlrd.open_workbook(str(Path(__file__).parent) + "\\" + filename)
    sheet = wb.sheet_by_name(sheet_name)
    for i in range(1, sheet.nrows):
        data = {}
        for j in range(0, sheet.ncols):
            data[sheet.cell_value(0, j)] = sheet.cell_value(i, j)
        data_list.append(data)
    return data_list
