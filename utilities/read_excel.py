import openpyxl

def get_data():
    workbook=openpyxl.load_workbook("C://Users//pavan//PycharmProjects//Selenium_E26//Demo_Tricentis_Framework//test_data//login_data.xlsx")
    worksheet=workbook["login"]
    data= []

    for row in worksheet.iter_rows(min_row=2,values_only=True):
        data.append(row)

    return data

