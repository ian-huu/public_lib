from xlwt import Workbook

def save(file_name_or_filelike_obj, title, data):
    book = Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet 1')
    for idx, val in enumerate(title):
        sheet.write(0, idx, val)
    for idx, row in enumerate(data):
        for idxx, val in enumerate(row):
            sheet.write(idx + 1, idxx, val)
    book.save(file_name_or_filelike_obj)

def load(file_name):
    pass